from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'{self.name}'

# ---------------- ROUTES ---------------- #
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/chats')
def chats():
    return render_template('chats.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/Reports')
def reports():
    return render_template('reports.html')

# Visuals page (BP chart)
@app.route('/visuals')
def visuals():
    return render_template('visuals.html')

# API to provide BP data
@app.route('/bp_data')
def bp_data():
    df = pd.read_csv("bp_data.csv")   # Make sure bp_data.csv exists in project root
    return jsonify(df.to_dict(orient="records"))

# ---------------- RUN ---------------- #
if __name__ == '__main__':
    app.run(debug=True)
