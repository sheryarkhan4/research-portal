from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///research.db'
db = SQLAlchemy(app)

class Research(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Research_title = db.Column(db.String(100), nullable=False)
    Research_description = db.Column(db.String(100), nullable=False)
    Research_area = db.Column(db.String(100), nullable=False)
    Faculty_name = db.Column(db.String(100), nullable=False)
    Departement = db.Column(db.String(100), nullable=False)
    Required_skills = db.Column(db.String(100), nullable=False)
    Avaliable_positions = db.Column(db.Integer, nullable=False)
    Application_deadline = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Research_title': self.Research_title,
            'Research_description': self.Research_description,
            'Research_area': self.Research_area,
            'Faculty_name': self.Faculty_name,
            'Departement': self.Departement,
            'Required_skills': self.Required_skills,
            'Avaliable_positions': self.Avaliable_positions,
            'Application_deadline': self.Application_deadline,
            'status': self.status
        }

with app.app_context():
    db.create_all()



#create routes
@app.route('/')
def home():
    return "Hello"



if __name__ == '__main__':
    app.run(debug=True)