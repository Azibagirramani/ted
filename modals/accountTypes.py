
from pydantic import BaseModel


class AccountTypes(BaseModel):
    name: str
    description: str

