import psycopg2
#from odoo import api, fields, models

########################################################################################################################
import xmlrpc.client
import csv

from flask import jsonify

url = "http://xx.xx.xx.xx:8069"
database = "xxxxxx"
user = "xxxxxxxxxx"
pwd = "xxxxxxxxx"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Version Details: ", common.version())

uid = common.authenticate(database, user, pwd, {})
print(uid)


########################################################################################################################
model = 'res.partner'
# Use execute_kw to search and read all records from the specified model
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
domain = [[['name', "like", "jobcenter"]]]
partner_ids = models.execute_kw(database, uid, pwd, model, 'search_read', domain)
#print(f"Here are infos: {partner_ids}")
limit = 1
records1 = models.execute_kw(database, uid, pwd, model, 'search_read', [partner_ids],
                             {'fields': ['street', 'city','user_id',
                            'display_name','forename','date',
                            "name" , "phone", "sex"], "limit": limit})
x = (records1)
# odoo_limit_data = jsonify(records1)
# print(f"dat {odoo_limit_data}")
# # print(f"\nRecords of some fields: -------->\n {odoo_limit_data}")
# print(f"\nRecords of some fields: -------->\n {records1}")

########################################################################################################################

























