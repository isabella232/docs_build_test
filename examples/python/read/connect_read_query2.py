# Start Connection
from pymongo import MongoClient
from pprint import pprint
from bson import SON
import json

connection_string = "mongodb://testuser:<PASSWORD>@localhost:27017/test?authSource=admin"
client = MongoClient(connection_string)
# End Connection

# Start DatabaseBind
db = client.test
# End DatabaseBind

# End InsertMany

cursor = db.inventory.find(
    {"size": SON([("h", 14), ("w", 21), ("uom", "cm")])})

for inventory in cursor:
  pprint(inventory)

client.close()
