from myproject import app,db
from flask import render_template,Blueprint,redirect,url_for,flash,request
from myproject.forms import AddEventForm,RegistrationForm,LoginForm,AddEventForm
from myproject.models import User,Event
from flask_login import login_required,login_user,logout_user,current_user
import operator
from datetime import datetime
import pytz

core=Blueprint('core',__name__)

timezone=pytz.timezone('Asia/Calcutta')


@core.route('/',methods=['GET','POST'])
def home():
    if current_user.is_authenticated:
        events=current_user.events
        events.sort()
        return render_template('home.html',events=events,event_count=str(len(events)),timezone=timezone)
    else:
        return render_template('home.html')


@core.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    
    if form.validate_on_submit():
        if form.contact_no.data=='':
            user=User(form.email.data,form.name.data,form.password.data,'-1')
        else:
            user=User(form.email.data,form.name.data,form.password.data,form.contact_no.data)
        
        db.session.add(user)
        db.session.commit()
        # flash('Successful')
        
        return redirect(url_for('core.login'))
    # flash('First time register')
    flash(form.errors)
    return render_template('register.html',form=form)

@core.route('/listusers')
def list_users():
    users=User.query.order_by(User.id).all()
    return str(users[0])

@core.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        # Query the user
        user=User.query.filter_by(email=form.email.data).first()
        
        if user.validate_password(form.password.data) and user is not None:
            login_user(user)
            
            # If user was trying to visit a page that requires login, then after login redirect to that page
            next = request.args.get('next')
            if next==None or not next[0]=='/':
                next=url_for('core.home')
                
            return redirect(next)
        
    flash(form.errors)
    return render_template('login.html',form=form)

@core.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.home'))


@core.route('/addevent',methods=['GET','POST'])
@login_required
def add_event():
    form=AddEventForm()
    form.scheduler_time.data=datetime.now(pytz.timezone('Asia/Calcutta'))
    
    if form.validate_on_submit():
        event=Event(form.title.data,timezone.localize(form.scheduler_time.data),current_user.id)
        
        db.session.add(event)
        db.session.commit()
        # flash('Successful')
        
        return redirect(url_for('core.home'))
    # flash('First time register')
    flash(form.errors)
    return render_template('add_event.html',form=form)

@core.route('/deleteevent/<int:event_id>')
@login_required
def delete_event(event_id):
    event=Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('core.home'))


@core.route('/viewevents')
@login_required
def list_events():
    pass
