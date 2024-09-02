from flask import Flask, render_template

app = Flask(__name__)

# Handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to simulate a 500 internal server error
@app.route('/500')
def simulate_internal_server_error():
    # Simulate a 500 error by raising an exception
    raise Exception("This is a simulated 500 Internal Server Error.")

# Handler for 500 errors
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Run the Flask app without debug mode
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
