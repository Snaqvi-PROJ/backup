from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessThis'

@app.route('/')
def hello() -> str:
    return 'Hello from simple web app'

@app.route('/login')
def do_login() -> str:
    session['loggeed_in'] = True
    return 'You are now logged in'

@app.route('/page1')
def page1() -> str:
    return 'This is page 1'

@app.route('/page2')
def page2() -> str:
    return 'This is page 2'

@app.route('/page3')
def page3() -> str:
    return 'This is page 3'

if __name__ == '__main__':
    app.run(debug=True)