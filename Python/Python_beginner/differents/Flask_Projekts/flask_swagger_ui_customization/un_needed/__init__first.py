from flask import Flask
from app.not_need_now.resources import ns
from app.not_need_now.extensions import api, db

def create_app():
	app= Flask(__name__)
	


	# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
	app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@FeraidonM/feri"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	# need to install  migrate to migrate database --- > pip install Flask-Migrate
	
	api.init_app(app)
	db.init_app(app)
	
	
	api.add_namespace(ns)
	return app





#create_app().run(debug=True)

# if __name__=="__main__":
# 	create_app().run(debug=True)

