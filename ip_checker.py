import socket

target_url = &quot;google.com&quot;
target_ip = socket.gethostbyname(target_url)
print(f&quot;[+] The IP address of {target_url} is {target_ip}&quot;)
