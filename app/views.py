from app import app
 
 
@app.route('/')
def home():
    return "Flask says 'Hello world!'"
 
@app.route('/')
def home():
    return "hello world!"
