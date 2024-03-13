import psycopg2
#from odoo import api, fields, models

########################################################################################################################
import xmlrpc.client
import csv


url = "http://xx.xx.xx.xx:8069"
database = "xxxxx"
user = "xxxxxxxxxxx"
pwd = "xxxxxxxxx"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Version Details: ", common.version())

uid = common.authenticate(database, user, pwd, {})
print(uid)
########################################################################################################################

model = 'res.partner'
model2 = 'de_d.measure'
model3 = 'de_.special'



# Use execute_kw to search and read all records from the specified model
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))



#current_user_id = uid
#entry_name = input("what do you want to search: ")
#entry_name2 = input(f"if you know exact name,  Enter (=) alse Enter (like):")
domain = [[['name', "like", "jobcenter"]]]

# if entry_name2.lower() == '=':
#     domain = [[['name', '=', entry_name]]]
# else:
#     domain = [[['name', 'like', entry_name]]]



#print("Domain before calling execute_kw:", domain)

partner_ids = models.execute_kw(database, uid, pwd, model, 'search_read', domain)
print(f"Here are infos: {partner_ids}")


limit = 1
records1 = models.execute_kw(database, uid, pwd, model, 'search_read', [partner_ids], {'fields': ['street', 'city','user_id',\
                                                                                                  'display_name','forename','date', \
                                                                                                  "name" , "phone", "sex"], "limit": limit})
print(f"\nRecords of some fields: -------->\n {records1}")



# partner_id = int(input("which ID number are looking for: "))
partner_id = 2
record2 = models.execute_kw(database, uid, pwd, model, 'read', [partner_id], {'fields': ['name', 'phone', 'email', 'create_date', 'birthdate']})
print(f"\nits what you exact wanted by id: -----------> {record2}\n")







########################################################################################################################
# alle felder anzeigen lassen ,nur dann wenn break gelöscht wird
fields_info = models.execute_kw(database, uid, pwd, model2, 'fields_get', [], {'attributes': ['string', 'help','vorname','nachname', 'type']})
# Print information about all fields
for field_name, field_data in fields_info.items():
    print(f"Field Name: {field_name}")
    print(f"Field Label: {field_data['string']}")
    print(f"Field Type: {field_data['type']}")
    help_text = field_data.get('help', 'No help available')
    print("-----------------------------")
    #break

# fiel namen in a list
field_names = list(fields_info.keys())
print("Field Names:", field_names)


## field values insid a list
field_values = list(fields_info.values())
print("\nField values:", field_values)




domain = [[['name', "=", "any"]]]
records = models.execute_kw(database, uid, pwd, model, 'search_read', domain, {'fields': list(fields_info.keys())})



# Extract field names from the first record (assuming i want it from the first record)
if records:
    field_names = list(records[0].values())
    print("Field Names:", field_names)
else:
    print("No records found for 'Feraidon'.")

#################################################
# Extract field names for which the value 'Feraidon' is present
field_names_with = []
for record in records:
    for field_name, field_value in record.items():
        if field_value == 'jobcenter':
            field_names_with.append(field_name)

print("Field Names with 'Feraidon':", field_names_with)

#############################################


