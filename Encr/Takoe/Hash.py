import hashlib

#print(hashlib.algorithms_guaranteed)
hash_object = hashlib.sha1(b'30 01 BF')
hex_dig = hash_object.hexdigest()
print(hex_dig)
