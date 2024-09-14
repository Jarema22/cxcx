import smtplib, ssl
import os


def Send_Email(massage):
    host = 'smtp.gmail.com'
    port = 465
    username = "python.test.app228@gmail.com"

    password = os.getenv("PASSWORD")
    receiver = "python.test.app228@gmail.com"
    context = ssl.create_default_context()
    print(massage)
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print(massage)
        server.login(username, password)
        server.sendmail(username, receiver, massage)
        print("dan")
