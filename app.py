from myproject import app
from background_script import scheduler

    
if __name__ == "__main__":

    
    scheduler.start()
    # app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,use_reloader=False)
    
    
