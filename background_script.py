#################################################
##############  SCHEDULER #######################
#################################################
import time,atexit
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime,timedelta
from myproject.models import User,Event
from myproject import db
from myproject.email_script import send_email_of_1_hour,send_email_of_5_mins
import pytz

def background_func():
    events=Event.query.all()
    for event in events:
        # Check for 5 min remaining 
        time_now=datetime.now(pytz.timezone('Asia/Calcutta'))
        time_5_min_from_now=time_now+timedelta(minutes=5)
        
        if time_5_min_from_now>=event.scheduler_time and event.five_min_reminded == False:
            user_name=event.user_of_this_event.name
            # print(f'{user_name}, your task {event.title} is in 5 mins   notified at {time_now}')
            if send_email_of_5_mins(event.user_of_this_event,event):
                event.five_min_reminded=True
            
        # Check for 1 hour remaining 
        time_now=datetime.now(pytz.timezone('Asia/Calcutta'))
        time_1_hour_from_now=time_now+timedelta(hours=1)
        
        if time_1_hour_from_now>=event.scheduler_time and event.one_hour_reminded == False:
            user_name=event.user_of_this_event.name
            # print(f'{user_name}, your task {event.title} is in 1 hour  notified at {time_now}')
            if send_email_of_1_hour(event.user_of_this_event,event):
                event.one_hour_reminded=True
            
    db.session.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(func=background_func,trigger='interval',seconds=3)

atexit.register(lambda: scheduler.shutdown())