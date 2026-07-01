from typing import Optional
from pydantic import BaseModel

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello stranger"
    return f"Hello {name}"

print(greet())
print(greet("Shivam"))







# One way
email: Optional[str] = None
print(email)
email = "shivam@gmail.com"
print(email)

# Another way, both are same.
phone: str | None = None
print(phone)
phone = "1234567890"
print(phone)








# Inheriting from BaseModel gives automatic validations
class Person(BaseModel):
    name: str
    age: int

class Data(BaseModel):
    people: list[Person]

class QueryResponse(BaseModel):
    status: str
    code: int
    data: Data

r = QueryResponse(
    status="success",
    code=200,
    data={"people": [{"name":"shivam", "age": 32}]}
)
print(r.status)
