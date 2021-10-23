

from pymongo import MongoClient

client = MongoClient()

# database
db = client['ted']

# account type table

accountTypeTable = db['accountTypes']
