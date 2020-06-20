import os
FROM_EMAIL_ID=os.environ.get('FROM_EMAIL_ID')
FROM_EMAIL_PASS=os.environ.get('FROM_EMAIL_PASS')
SECRET_KEY=os.environ.get('SECRET_KEY')
DB_URI=os.environ.get('DATABASE_URL')