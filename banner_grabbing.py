import socket
 
s = socket.socket()
 

s.connect((&quot;127.0.0.1&quot;, 80))
 
s.send(b&quot;HEAD / HTTP/1.0\r\n\r\n&quot;)
 
banner = s.recv(1024).decode()
 
print(&quot;[+] Response:&quot;)
print(banner)
 
s.close()

import secrets
import string
alphabet = string.ascii_letters + string.digits + string.punctuation
# Generate a secure 12-character password
password = &#39;&#39;.join(secrets.choice(alphabet) for i in range(12))
print(f&quot;[+] Generated Secure Password: {password}&quot;)
