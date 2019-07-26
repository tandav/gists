'''
send email using your gmail
'''
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

FROM     = 'example@gmail.com' # your gmail account
TO       = 'example@example.com'
PASSWORD = 'your_google_app_password' # https://myaccount.google.com/apppasswords


message = MIMEMultipart()
message['From'] = FROM
message['To'] = TO
message['Subject'] = "multipart test"
body = "This is an email with attachment sent from Python"

text = '''\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com
'''

html = '''\
Hello, guys!
this is your code

<pre>
with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
    server.starttls(context=ssl.create_default_context())
    server.login(FROM, PASSWORD)
    server.sendmail(FROM, TO, message.as_string())
</pre>
'''

# message.attach(MIMEText(text, 'plain'))
message.attach(MIMEText(html, 'html'))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
    server.starttls(context=ssl.create_default_context())
    server.login(FROM, PASSWORD)
    server.sendmail(FROM, TO, message.as_string())
