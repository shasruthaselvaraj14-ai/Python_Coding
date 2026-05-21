import socket
 
s = socket.socket()
 
s.settimeout(1)
 
status = s.connect_ex((&quot;127.0.0.1&quot;, 80))

 
if status == 0:
print(&quot;[+] Port 80 is OPEN&quot;)
else:
print(f&quot;[-] Port 80 is CLOSED | Error Code: {status}&quot;)
