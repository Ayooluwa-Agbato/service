# from email import message
import smtplib, ssl
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email : str
    message : str
    first_name : str
    last_name : str

@app.post("/")
def send_mail(user:User):
    def password():
        return ("Yourpassword")
    doctors = ["agbato.ayooluwa@stu.cu.edu.ng"]
    full_name = user.last_name + " " +user.first_name
    customer_email = user.email
    text = (user.message) + ("\n    Sent by {} \n Via {}".format(full_name,customer_email))
    subject = "Consultation Request"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "agbatoayo@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password())
        for receiver_email in doctors:
            server.sendmail(sender_email, receiver_email, message)
    return("Mail sent successfully")
