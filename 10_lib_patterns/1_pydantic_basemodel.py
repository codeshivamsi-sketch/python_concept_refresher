import email
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str


# Valid
u = User(name="Shivam", age=32, email="shivam@gmai.com")
print(u.name)

# Missing field
# u = User(name="Shivam", age=32)

# Wrong type
# Wont throw err, pydantic auto covert "32" to 32.
u2 = User(name="Shivam", age="32", email="shivam@gmail.com")


# Uncovertible
# This will throw error when coversion is impossible
# u3 = User(name="Shivam", age="aaa", email="shivam@gmail.com")







# Convert to dict/JSON 
print(u.model_dump()) # Dict
print(u.model_dump_json()) # Json







