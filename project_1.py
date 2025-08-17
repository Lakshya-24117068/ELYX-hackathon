from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    sno =  db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'{self.name}'

@app.route('/')
def hello_world():
     return render_template('index.html')
 
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile') 
def profile():
    return render_template('profile.html')


@app.route('/Reports')
def reports():
   return render_template('reports.html')
    
@app.route('/Chats')
def chats():
   return render_template('chats.html')

@app.route('/Stats')
def stats():
   return render_template('stats.html')

@app.route('/timeline')
def timeline():
   return render_template('timeline.html')

if __name__ == '__main__':

    
    app.run(debug=True)
