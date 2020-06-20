##################################################
############ BASIC FLASK #########################
#################################################

from flask import Flask,url_for
app=Flask(__name__)

import myproject.vars as vars



######################################################
##############  DATABASE CONFIG ######################
#####################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = vars.DB_URI

# Secret key for forms
app.config['SECRET_KEY']=vars.SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# Create a database object and connect it to the Flask app
db=SQLAlchemy(app)

# Migration for setting up database and update the schema of database
from flask_migrate import Migrate

# Connection application to database for migration
Migrate(app,db)

#####################################################
################ Login Management ###################
####################################################

from flask_login import LoginManager
login_manager=LoginManager()
login_manager.init_app(app)

#Where(which view) to go when user has to login
login_manager.login_view='core.login'

###################################################
##############  ROUTING ##########################
##################################################


from myproject.views import core
app.register_blueprint(core)
