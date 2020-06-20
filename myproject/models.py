from myproject import db,login_manager
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
from datetime import datetime

# This sets the callback for reloading a user from the session. The function you set
# should take a user ID (a unicode) and return a user object, or None if the user 
# does not exist.
# Allows to do stuff like if user.isauthenticated and more
# Will never use it directly, will get called by Flask whenever required

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    


# Inherit from db.model so that a table(in database) can be created of the class
# UserMixin for authentication, can call login_user on object of this class
class User(db.Model,UserMixin):
    
    __tablename__='users'
    
    # Columns or attributes in database table named __tablename__
    id=db.Column(db.Integer,primary_key=True) # Primary key and will auto increment
    email=db.Column(db.String(128),unique=True,index=True,nullable=False)
    name=db.Column(db.String(128),nullable=False)
    contact_no=db.Column(db.String(20),default='0')
    password_hash=db.Column(db.String(512),nullable=False)
    
    # First argument is the name of class model to which it will reference
    # backref is the name of the relation
    # backref is a simple way to also declare a new property on the 'BlogPost' class
    # It is a one to many relationship by default
    events=db.relationship('Event',backref='user_of_this_event',lazy=True)
    #If you would want to have a one-to-one relationship you can pass uselist=False to relationship()
    
    
    def __init__(self,email,name,password,contact_no=None):
        self.email=email
        self.name=name
        self.contact_no=contact_no
        self.password_hash=generate_password_hash(password)
        
    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    # Returns the string representaion of the class object
    def __repr__(self):
        return f'User mail: {self.email}'
    
    
class Event(db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    
    # Creating the foreign key (<tablename>.<attributename>)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    event_creation_time=db.Column(db.DateTime,nullable=False,default=datetime.now())
    scheduler_time=db.Column(db.DateTime,nullable=False)
    title=db.Column(db.String(512),nullable=False)
    five_min_reminded=db.Column(db.Boolean,default=False)
    one_hour_reminded=db.Column(db.Boolean,default=False)
    
    def __init__(self,title,scheduler_time,user_id):
        self.title=title
        self.scheduler_time=scheduler_time
        self.user_id=user_id
        
    def __repr__(self):
        return f'Event Title: {self.title}, 5_min_rem={self.five_min_reminded}'
    
    # For sorting
    def __lt__(self, other):
         return self.scheduler_time < other.scheduler_time
        
    
    
