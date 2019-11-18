import rest
from app import app
from flask import render_template
from datetime import datetime

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/login/page')
def login_page():
	return render_template('login.html')
	
@app.route('/signup/page')
def singup_page():
	return render_template('signup.html')
	
@app.route('/about')
def about():
	return render_template('about.html')
		
if __name__ == "__main__":
    app.run()