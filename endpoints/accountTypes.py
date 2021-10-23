from fastapi import APIRouter

# modals imports
from modals.accountTypes import AccountTypes

# controller imports
from controllers.accountTypesController import controllerAccountType

endpoints = APIRouter()


# get all account types
@endpoints.get('/')
def getAcountTypes() -> list:
    return controllerAccountType()


# create account types
@endpoints.post('/')
def createAccountType(payload: AccountTypes) -> list:
    return payload.dict()


# get update account types
@endpoints.patch('/', summary="Update account type")
def updateAccountType(type_id: str, payload: AccountTypes) -> list:
    return {}


# delete account types
@endpoints.delete('/')
def deleteAccountType(type_id: str) -> list:
    return {}
