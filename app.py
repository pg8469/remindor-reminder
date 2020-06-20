from myproject import app
from background_script import scheduler

    
if __name__ == "__main__":

    
    scheduler.start()
    # app.run(debug=True)
    app.run(use_reloader=False,debug=False)
    
