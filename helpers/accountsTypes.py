from configuration.database import accountTypeTable
from fastapi.encoders import jsonable_encoder


# Helper method for getting all account types
def getAllAccountTypes():
    types = accountTypeTable.find()
    content = []
    for x in types:
        content.append(x)
    return content
