import smtplib, ssl


def Send_Email(massage):
    host = 'smtp.gmail.com'
    port = 465
    username = "Doglaucher@gmail.com"
    password = "uhqlfjgiqjjgfkhw "
    receiver = "Doglaucher@gmail.com"
    message1 = "noooooob"
    context = ssl.create_default_context()
    print(massage)
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print(massage)
        server.login(username, password)
        server.sendmail(username, receiver, massage)
        print("dan")



