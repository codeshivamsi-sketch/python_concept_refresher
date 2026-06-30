import json

text = '{"name": "Shivam", "age": 32}'
data = json.loads(text)

print(data["name"])
print(type[data])






data2 = {"name": "Shivam", "age": 25}
text2 = json.dumps(data2)

print(text2)
print(type(text2))
