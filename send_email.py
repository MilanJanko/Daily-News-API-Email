import smtplib
import ssl
import envvar


def send_email(message):

    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    username = envvar.username
    password = envvar.password
    receiver = envvar.receiver

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
