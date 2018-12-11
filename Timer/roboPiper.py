import hashlib


filename = '../README.md'
hasher = hashlib.md5()
with open(filename,'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print(hasher.hexdigest())

#728a437926785e3bea25a23f1dc3edc3