import smtplib, ssl
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    email : str
    message : str

@app.post("/")
def send_mail():
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "agbatoayo@gmail.com"
    emails = ['agbato.ayooluwa@stu.cu.edu.ng','solomonmarvel@hotmail.com']
    password = "yourpassword"
    message = "New version has been deployed, check it out"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        for receiver_email in emails:
            server.sendmail(sender_email, receiver_email, message)
    print("Done")
    return("Mail sent successfully")

send_mail()
