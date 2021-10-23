from pydantic import BaseModel
from typing import Optional


class CreateAccounts(BaseModel):
    email: str
    password: str
    accountType: int


class Accounts(BaseModel):
    username: str
    email: str
    password: str
    ip: Optional[str] = None
    reset_token: Optional[str] = None
    accountType: int


class Tokens(BaseModel):
    accessToken: str
    refreshToken: str
