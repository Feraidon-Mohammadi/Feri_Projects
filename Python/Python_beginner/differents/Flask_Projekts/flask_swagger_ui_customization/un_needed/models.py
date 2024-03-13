from extensions import db

class Course(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	
	course = db.relationship("Course", back_populates="schulern")
	
	
	
class Schuler(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)
	course_id = db.Columndb(db.ForeignKey("course_id"))
	
	course= db.relationship("Course", back_populates="schulern")
	
	