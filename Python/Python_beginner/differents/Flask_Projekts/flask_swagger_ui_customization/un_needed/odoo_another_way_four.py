
import xmlrpc.client

from flask import jsonify, Flask
from flask_restful import Api, fields
from flask_restful.reqparse import Namespace
from flask_restful_swagger_2 import Resource
from flask_sqlalchemy import SQLAlchemy

#####################  odoo  ############################
app = Flask(__name__)
api = Api()
db = SQLAlchemy()
ns = Namespace("app")

#api.init_app(app)
#api.add_namespace(ns)
#db.init_app(app)

#################################################### odoo ##############################################################


url = "http://xx.xx.xx.xx:xxxx"
database = "xxxxxx"
user = "xxxxxxx"
pwd = "xxxxxxx"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#print("Version Details: ", common.version())

uid = common.authenticate(database, user, pwd, {})
#print(uid)
odoo_db_info = {
    'host': 'http://xx.xx.xx.xx',
    'port': "xxxx",
    'database': 'xxxxxx',
    'username': 'xxxxxx',
    'password': 'xxxxxxxx',
}

########################################################################################################################



# @ns.marshal_list_with(odoo_model)
@app.route("/odoo", methods=["GET"])
def get_odoo_data(*args):
    # Odoo database connection information
    odoo_db_info = {
    'host': 'http://11.11.111.11',
    'port': "8069",
    'database': 'tttttt',
    'username': 'eeeeee',
    'password': 'ffffff',
    }
############################################################# fixed ##############################################
    # Odoo XML-RPC server URL
    odoo_url = 'http://{0}:{1}/xmlrpc/2'.format(odoo_db_info['host'], odoo_db_info['port'])

    # Connect to the Odoo database using XML-RPC
    url = "http://xx.xx.xx.xx:xxxx"
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(odoo_db_info['database'], odoo_db_info['username'], odoo_db_info['password'], {})

    model = 'res.partner'
    # Create an XML-RPC object for the database
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    domain = [[['name', "like", "jobcenter"]]]
    partner_ids = models.execute_kw(database, uid, pwd, model, 'search_read', domain)
    limit = 1
    records1 = models.execute_kw(database, uid, pwd, model, 'search_read', [partner_ids],
                                    {'fields': ['id', 'display_name', 'forename','name',"city", "street","phone"]})



    json_data = jsonify(records1)
    # for key, value in json_data:
    #     x = key,value

    return json_data
################################################# not need #######################################


# Define a model for the Odoo data
odoo_model = api.model("get_odoo_data", {
    "id": fields.Integer,
    "display_name": fields.String,
    "forename": fields.String,
    "nachname":fields.String,
    "city": fields.String,
    "street": fields.String,
    "phone": fields.String,


})

# Define a Flask API endpoint to expose Odoo data
@ns.route('/odoo_data')
class OdooDataResource(Resource):
    @ns.marshal_list_with(odoo_model)
    def get(self):
        # Fetch Odoo data
        json_datas= get_odoo_data()

        return json_datas
