import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = &quot;0.0.0.0&quot;
port = 5000

server.bind((host, port))
server.listen(1)

print(&quot;Waiting for connection...&quot;)
conn, addr = server.accept()

print(&quot;Connected with:&quot;, addr)

while True:
message = conn.recv(1024).decode()

if message.lower() == &quot;bye&quot;:
print(&quot;Client ended the chat&quot;)
break

print(&quot;Client:&quot;, message)

reply = input(&quot;You: &quot;)
conn.send(reply.encode())

if reply.lower() == &quot;bye&quot;:
break

conn.close()
server.close()
