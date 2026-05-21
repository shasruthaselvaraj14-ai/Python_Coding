import socket
 
try:
target_url = input(&quot;Enter website name: &quot;)
 
target_ip = socket.gethostbyname(target_url)
 
print(f&quot;[+] The IP address of {target_url} is {target_ip}&quot;)
 
except socket.gaierror:
print(&quot;[-] Invalid website or DNS lookup failed&quot;)
