
from fastapi import FastAPI
from endpoints import (accounts, accountTypes)

server = FastAPI()

server.include_router(accounts.endpoints, tags=["Accounts"], prefix="/accounts")
server.include_router(accountTypes.endpoints, tags=["Accounts Types"], prefix="/accountTypes")