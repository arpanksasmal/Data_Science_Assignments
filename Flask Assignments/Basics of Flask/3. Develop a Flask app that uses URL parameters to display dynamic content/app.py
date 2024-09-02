from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, welcome to the dynamic content app!'

@app.route('/greet/<name>')
def greet(name):
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)