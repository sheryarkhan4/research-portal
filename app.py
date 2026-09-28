from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

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
   return render_template("index.html")

#GET
#to get all research titles/opportunities
@app.route('/api/researchtitles', methods=['GET'])
def get_research_titles():
    research_list = Research.query.all()
    return jsonify([research.to_dict() for research in research_list])

#to find a specific research title by id
@app.route('/api/researchtitles/<int:id>', methods=['GET'])
def get_research_title(id):
    research = Research.query.get(id)
    if research:
        return jsonify(research.to_dict())
    else:
        return jsonify({'message': 'Research title not found'}), 404



#post
#creates a research title/opportunity
@app.route('/api/researchtitles', methods=['POST'])
def create_research_title():
    data=request.get_json()
    new_researchtitle=Research(
        Research_title=data['Research_title'],
        Research_description=data['Research_description'],
        Research_area=data['Research_area'],
        Faculty_name=data['Faculty_name'],
        Departement=data['Departement'],
        Required_skills=data['Required_skills'],
        Avaliable_positions=data['Avaliable_positions'],
        Application_deadline=data['Application_deadline'],
        status=data['status']
    )
    db.session.add(new_researchtitle)
    db.session.commit()
    return jsonify(new_researchtitle.to_dict()), 201


 #put
 #updates a research title/opportunity
@app.route('/api/researchtitles/<int:id>', methods=['PUT'])
def update_research_title(id):
    research = Research.query.get(id)
    if research:
        data = request.get_json()
        research.Research_title = data['Research_title']
        research.Research_description = data['Research_description']
        research.Research_area = data['Research_area']
        research.Faculty_name = data['Faculty_name']
        research.Departement = data['Departement']
        research.Required_skills = data['Required_skills']
        research.Avaliable_positions = data['Avaliable_positions']
        research.Application_deadline = data['Application_deadline']
        research.status = data['status']
        db.session.commit()
        return jsonify(research.to_dict())
    else:
        return jsonify({'message': 'Research title not found'}), 404


#delete
#deletes a research title/opportunity
@app.route('/api/researchtitles/<int:id>', methods=['DELETE'])
def delete_research_title(id):
    research = Research.query.get(id)
    if research:
        db.session.delete(research)
        db.session.commit()
        return jsonify({'message': 'Research title deleted successfully'})
    else:
        return jsonify({'message': 'Research title not found'}), 404




if __name__ == '__main__':
    app.run(debug=True)