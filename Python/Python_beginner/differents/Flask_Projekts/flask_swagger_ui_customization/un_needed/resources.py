from flask_restx import Resource, Namespace

from app.not_need_now.models import Schuler

ns = Namespace("api")


@ns.route("/home")
class Entities(Resource):
	def get(self):
		# Retrieve entities from the database and return them
		entities = Schuler.query.all()
		return [{"name": entity.name, "course_id": entity.course_id} for entity in entities]