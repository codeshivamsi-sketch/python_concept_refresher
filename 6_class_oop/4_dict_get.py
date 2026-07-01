user = {"name": "shivam", "age": 32}

# print(user["city"]) # crashes if key is missing
print(user.get("city")) # returns none instead
print(user.get("city", "bengaluru")) # returns default instead


