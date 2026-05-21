from datetime import datetime
from email.message import EmailMessage
import os
import shutil
import smtplib
import time
sender_email = &quot;abc@gmail.com&quot;
password = &asdf;wert yuio asdf ghjk&vbnm;
receiver_email = &quot;aaa@gmail.com&quot;
source_dir = r&quot;D:\shasrutha\python\DAY 1&amp;2&quot;
temp_today_dir = r&quot;D:\shasrutha\python\today_files&quot;
today = datetime.now().strftime(&quot;%Y-%m-%d&quot;)
zip_output_base = rf&quot;D:\shasrutha\python\{today}&quot;
file_to_send = rf&quot;D:\shasrutha\python\{today}.zip&quot;
TARGET_TIME = &quot;15:08&quot;
already_sent_today = False
current_day = datetime.now().strftime(&quot;%Y-%m-%d&quot;)
print(
f&quot;Automation Active.\n&quot;
f&quot;Monitoring files and sending ZIP at {TARGET_TIME}&quot;
)

while True:
now = datetime.now()

current_time = now.strftime(&quot;%H:%M&quot;)
today_date = now.strftime(&quot;%Y-%m-%d&quot;)
if today_date != current_day:
current_day = today_date
already_sent_today = False
zip_output_base = rf&quot;D:\shasrutha\python\{today_date}&quot;
file_to_send = rf&quot;D:\shasrutha\python\{today_date}.zip&quot;
if current_time == TARGET_TIME and not already_sent_today:
print(
&quot;\nTime matched:&quot;,
current_time
)
try:
if os.path.exists(
temp_today_dir
):
shutil.rmtree(
temp_today_dir
)
os.makedirs(
temp_today_dir
)
files_found_today = 0
for item in os.listdir(
source_dir

):
item_path = os.path.join(
source_dir,
item
)
if os.path.isfile(
item_path
):
file_time = os.path.getmtime(
item_path
)
file_date = datetime.fromtimestamp(
file_time
).strftime(
&quot;%Y-%m-%d&quot;
)
if file_date == today_date:
shutil.copy(
item_path,
temp_today_dir
)
files_found_today += 1
if files_found_today &gt; 0:
print(
f&quot;{files_found_today} files found&quot;

)
shutil.make_archive(
zip_output_base,
&quot;zip&quot;,
temp_today_dir
)
print(
&quot;ZIP created:&quot;,
file_to_send
)
msg = EmailMessage()
msg[&quot;Subject&quot;] = (
f&quot;Daily Report {today_date}&quot;
)
msg[&quot;From&quot;] = sender_email
msg[&quot;To&quot;] = receiver_email
msg.set_content(
&quot;Today&#39;s files attached.&quot;
)
with open(
file_to_send,
&quot;rb&quot;
) as file:
file_data = file.read()

msg.add_attachment(
file_data,
maintype=&quot;application&quot;,
subtype=&quot;zip&quot;,
filename=f&quot;{today_date}.zip&quot;
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
server.send_message(
msg
)
server.quit()
print(
&quot;Email Sent Successfully&quot;
)
else:
print(
&quot;No files created today&quot;

)
if os.path.exists(
temp_today_dir
):
shutil.rmtree(
temp_today_dir
)
already_sent_today = True
except Exception as e:
print(
&quot;Error:&quot;,
e
)
time.sleep(30)
