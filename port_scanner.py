import socket
s = socket.socket()
s.settimeout(1)
# connect_ex returns 0 if the port is open
status = s.connect_ex((&quot;127.0.0.1&quot;, 80))
print(&quot;[+] Port 80 is OPEN&quot; if status == 0 else &quot;[-] Port 80 is CLOSED&quot;)
