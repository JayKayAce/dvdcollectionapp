from flask_mail import Message
from flask import render_template

from app import mail
from app import app

def send_email(subject, sender, recipients, body, html_body):
    msg = Message(subject = subject, 
                  sender=sender, recipients=recipients)
    msg.body = body
    msg.html = html_body
    mail.send(msg)

def send_password_reset_email(user):
    token = user.get_password_reset_token()
    send_email("[Microblog] Reset Your Password",
                sender=app.config["ADMINS"][0],
                recipients = [user.email],
                text_body = render_template("email/reset_password.txt",
                                            user = user, token=token),
                html_body = render_template("email/reset_password.html",
                                            user=user,token=token))