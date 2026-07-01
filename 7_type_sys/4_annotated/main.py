from typing import Annotated
from pydantic import BaseModel, Field

age: int
# add extra metadata to a type hint 
age2: Annotated[int, "must be positive"]

# no err, not enforced by Python at runtime — they're just hints for the editor
age = "aa"
age2 = "dksfn"



class User(BaseModel):
    age: Annotated[int, Field(gt=0, lt=120)] # must be between 0 and 120

User(age=150) # validation error, Pydantic enforces it