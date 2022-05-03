import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        
        btn_delete = tk.Button(toolbar, text='Удалить позицию', bg='#d7d8e0', bd=0,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID_zak', 'date', 'quantity', 'com'), height=15, show='headings')

        self.tree.column('ID_zak', width=30, anchor=tk.CENTER)
        self.tree.column('date', width=365, anchor=tk.CENTER)
        self.tree.column('quantity', width=150, anchor=tk.CENTER)
        self.tree.column('com', width=100, anchor=tk.CENTER)

        self.tree.heading('ID_zak', text='код_заказа')
        self.tree.heading('date', text='дата_заказа')
        self.tree.heading('quantity', text='количество')
        self.tree.heading('com', text='выполнено')

        self.tree.pack()

    def records(self, date, quantity, com):
        self.db.insert_data(date, quantity, com)
        self.view_records()

    def update_record(self, date, quantity, com):
        self.db.c.execute('''UPDATE orders SET date=?, quantity=?, com=? WHERE ID_zak=?''',
                          (date, quantity, com, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM orders''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM orders WHERE id_zak=?''', (self.tree.set(selection_item, '#1')))
        self.db.conn.commit()
        self.view_records()

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Заказы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Дата:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Количество:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Выполнено:')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=80)

        self.combobox = ttk.Combobox(self, values=[u'0', u'1'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                    
                                                                       self.entry_money.get(),
                                                                       self.combobox.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Редактировать')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          
                                                                          self.entry_money.get(),
                                                                          self.combobox.get()))

        self.btn_ok.destroy()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('zakaz.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS orders (
    id_zak  INTEGER  PRIMARY KEY
                         NOT NULL,
    date DATETIME NOT NULL,
    quantity  INTEGER  NOT NULL,
    com   BOOLEAN NULL);''')
        self.conn.commit()
#OTVET
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Otvet (
    код_ответственного         PRIMARY KEY
                               NOT NULL,
    Фамилия            VARCHAR NOT NULL,
    Имя                VARCHAR NOT NULL,
    Отчество           VARCHAR NOT NULL,
    Пол                VARCHAR NOT NULL,
    дата_рождения      DATE    NOT NULL,
    дата_приёма        DATE    NOT NULL);''')
        self.conn.commit()
#CLIENTS
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Clients (
    код_клиента INTEGER NOT NULL
                        PRIMARY KEY,
    название    VARCHAR NOT NULL,
    телефон     VARCHAR NOT NULL,
    адрес       VARCHAR NOT NULL,
    категория   INTEGER NOT NULL);''')
        self.conn.commit()
#GOODS
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Goods (
    код_товара   INTEGER PRIMARY KEY
                         NOT NULL,
    наименование VARCHAR NOT NULL,
    группа       INTEGER NOT NULL,
    [на складе]  INTEGER NOT NULL);''')
        self.conn.commit()

#zakaz tovarov
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS zakaz_tovarov (
    заказ        INTEGER NOT NULL
                         PRIMARY KEY
                         REFERENCES orders (код_заказа),
    клиент       INTEGER REFERENCES Clients (код_клиента) 
                         NOT NULL,
    ответсвенный INTEGER REFERENCES Otvet (код_ответственного) 
                         NOT NULL,
    товар        INTEGER REFERENCES Goods (код_товара) 
                         NOT NULL);''')
        self.conn.commit()
    def insert_data(self, date, quantity, com):
        self.c.execute('''INSERT INTO orders(date, quantity, com) VALUES (?, ?, ?)''',
                       (date, quantity, com))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Заказы")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
