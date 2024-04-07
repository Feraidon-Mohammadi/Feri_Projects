# all codes in bash


"""

# GET ( all entites)
curl http://127.0.0.1:5000/entities

# post( create new entity)
curl -X POST -H "Content-Type: application/json" -d '{"key": "new_key", "value": "new_value"}' http://127.0.0.1:5000/entities


# put (update entity)
curl -X PUT -H "Content-Type: application/json" -d '{"key": "updated_key", "value": "updated_value"}' http://127.0.0.1:5000/entities/1


# delete entity
curl -X DELETE http://127.0.0.1:5000/entities/1



"""
