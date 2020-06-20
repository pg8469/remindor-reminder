import smtplib
from email.message import EmailMessage
from myproject.models import User,Event
from smtplib import SMTPServerDisconnected
import myproject.vars as vars
print('smtp started')
my_smtp=smtplib.SMTP(host='smtp.gmail.com',port=587,timeout=None)
my_smtp.ehlo()
my_smtp.starttls()
my_smtp.login(vars.FROM_EMAIL_ID,vars.FROM_EMAIL_PASS)
print('smtp ended')

email=EmailMessage()
email['from']='Remindor Reminder'

def send_email_of_5_mins(user,event):
    
    
    
    del email['to']
    del email['subject']
    email['to']=user.email
    email['subject']='Task Reminder'
    cont = f'{user.name}, this is a reminder that your task "{event.title}" is in 5 mins\nScheduled Time: {event.scheduler_time.hour}:{event.scheduler_time.minute}'
    email.set_content(cont)
    try:
        my_smtp.send_message(email)
        return True
    except :
        print('Disconnection occured')
        my_smtp.connect(host='smtp.gmail.com',port=587)
        my_smtp.ehlo()
        my_smtp.starttls()
        my_smtp.login(vars.FROM_EMAIL_ID,vars.FROM_EMAIL_PASS)
        return False
    
    
def send_email_of_1_hour(user,event):
    
    # my_smtp.connect()
    del email['to']
    del email['subject']
    email['to']=user.email
    email['subject']='Task Reminder'
    cont = f'{user.name}, this is a reminder that your task "{event.title}" is in 1 hour\nScheduled Time: {event.scheduler_time.hour}:{event.scheduler_time.minute}'
    email.set_content(cont)
    try:
        my_smtp.send_message(email)
        return True
    except :
        print('Disconnection occured')
        my_smtp.connect(host='smtp.gmail.com',port=587)
        my_smtp.ehlo()
        my_smtp.starttls()
        my_smtp.login(vars.FROM_EMAIL_ID,vars.FROM_EMAIL_PASS)
        return False
