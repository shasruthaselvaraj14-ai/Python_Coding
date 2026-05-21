import socket
 
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
 
s.connect((&quot;::1&quot;, 80))
 
print(&quot;Connected to local IPv6 Apache server&quot;)
