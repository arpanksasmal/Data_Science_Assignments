from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'app_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}! <a href="/logout">Logout</a>'
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)