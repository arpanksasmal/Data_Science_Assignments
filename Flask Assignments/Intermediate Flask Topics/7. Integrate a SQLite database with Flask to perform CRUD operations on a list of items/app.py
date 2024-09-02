from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Ensure the 'uploads' folder exists before creating the tables
if not os.path.exists('items.db'):
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item_name = request.form['item_name']
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = Item.query.get(item_id)
    if request.method == 'POST':
        item.name = request.form['item_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
