from pydantic import BaseModel


class CreateUsersRequest(BaseModel):
    name: str
    age: int
    sex: str
