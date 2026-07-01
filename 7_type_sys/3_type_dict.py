from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {
    "name": "Shivam",
    "age": 32
}

print(user["name"])