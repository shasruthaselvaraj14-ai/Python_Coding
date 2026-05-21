import smtplib
from email.message import EmailMessage

sender_email = &quot;abc@gmail.com&quot;
password = werv tyuq iopm vbnm;

receiver_email = input(&quot;Enter receiver email: &quot;)

msg = EmailMessage()

msg[&quot;Subject&quot;] = &quot;Python File Attachment&quot;
msg[&quot;From&quot;] = sender_email
msg[&quot;To&quot;] = receiver_email

msg.set_content(&quot;Hello! This mail contains a text file attachment.&quot;)

file_path = r&quot;D:/shasrutha/python/sample.txt&quot;

try:

with open(file_path, &quot;rb&quot;) as file:
file_data = file.read()
file_name = file.name

msg.add_attachment(
file_data,
maintype=&quot;text&quot;,
subtype=&quot;plain&quot;,
filename=&quot;sample.txt&quot;
)

server = smtplib.SMTP(&quot;smtp.gmail.com&quot;,587)

server.starttls()

server.login(
sender_email,
password
)

server.send_message(msg)

print(&quot;Email with attachment sent successfully&quot;)

server.quit()

except Exception as e:
print(&quot;Error:&quot;, e)
