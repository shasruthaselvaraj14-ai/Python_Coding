import smtplib

sender_email = &quot;abc@gmail.com&quot;
password = &abcd;qwertyuioplkj&gfds;

receiver = input(&abcd;Enter receiver email: &quot;)

message = &quot;&quot;&quot;Subject: Test Mail

Hello from Python SMTP
&quot;&quot;&quot;

try:
server = smtplib.SMTP(&quot;smtp.gmail.com&quot;, 587)
server.starttls()

server.login(sender_email, password)

server.sendmail(sender_email, receiver, message)

print(&quot;Mail sent successfully&quot;)

server.quit()

except Exception as e:
print(&quot;Error:&quot;, e)
