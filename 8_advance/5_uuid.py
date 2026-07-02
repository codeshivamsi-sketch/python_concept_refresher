import uuid

# generate a random unique id
new_id = uuid.uuid4()
print(new_id)
print(type(new_id))





# covert to str
id_str = str(new_id)
print(type(id_str))

# covert str back to uuid
uid = uuid.UUID(id_str)
print(type(uid))
