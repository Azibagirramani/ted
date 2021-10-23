from fastapi import APIRouter

# account modal import
from modals.accounts import (Accounts, CreateAccounts)

# router instance declaration
endpoints = APIRouter()


# fetch all accounts
@endpoints.get('/', response_description="Get all accounts on database")
def getAccounts() -> list:
    return []


# create user account
@endpoints.post('/', response_description="Create user accounts")
def createAccounts(payload: CreateAccounts) -> str:
    return payload.dict()


# update user account
@endpoints.patch('/', response_description="Update user accounts")
def updateAccounts(account_id: str) -> dict:
    return {}


# delete user account
@endpoints.delete('/', response_description="Delete user accounts")
def deleteAccounts(account_id: str) -> str:
    return {}