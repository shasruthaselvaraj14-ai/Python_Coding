import hashlib
 

text = &quot;SecureData123&quot;
 
hashed = hashlib.md5(text.encode()).hexdigest()
 
print(f&quot;[+] MD5 Hash: {hashed}&quot;)
