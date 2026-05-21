import hashlib
text = &quot;SecureData123&quot;
hashed = hashlib.sha256(text.encode()).hexdigest()
print(f&quot;[+] SHA-256 Hash: {hashed}&quot;)
