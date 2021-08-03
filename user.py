from pydantic import BaseModel

class User(BaseModel):
    name: str
    bikou: str
    password: str