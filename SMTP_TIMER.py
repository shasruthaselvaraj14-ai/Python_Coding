import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

sender_email = &quot;abc@gmail.com&quot;
password = &quot;sgeg fxvo pcvw heoc&quot;

receiver_email = input(&quot;Enter receiver email: &quot;)

print(&quot;Waiting to send mail at 14:10...&quot;)

while True:

current_time = datetime.now().strftime(&quot;%H:%M&quot;)

if current_time == &quot;14:10&quot;:

msg = EmailMessage()

msg[&quot;Subject&quot;] = &quot;Python File Attachment&quot;
msg[&quot;From&quot;] = sender_email
msg[&quot;To&quot;] = receiver_email

msg.set_content(
&quot;Hello! This mail contains a text file attachment.&quot;
)

file_path = r&quot;D:\shasrutha\python\sample.txt&quot;

try:

with open(file_path, &quot;rb&quot;) as file:
file_data = file.read()

msg.add_attachment(
file_data,
maintype=&quot;text&quot;,
subtype=&quot;plain&quot;,
filename=&quot;sample.txt&quot;
)

server = smtplib.SMTP(
&quot;smtp.gmail.com&quot;,
587
)

server.starttls()

server.login(
sender_email,
password
)

server.send_message(msg)

print(&quot;Email sent automatically at&quot;, current_time)

server.quit()

break

except Exception as e:
print(&quot;Error:&quot;, e)
break

time.sleep(30)
