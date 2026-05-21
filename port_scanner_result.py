import socket
import os
 
s = socket.socket()
 
s.settimeout(5)
 
status = s.connect_ex((&quot;127.0.0.1&quot;, 80))
 
if status == 0:
print(&quot;[+] Port 80 is OPEN&quot;)
else:
print(f&quot;[-] Port 80 is CLOSED&quot;)
print(f&quot;Error Code : {status}&quot;)
    print(f&quot;Reason : {os.strerror(status)}&quot;)
