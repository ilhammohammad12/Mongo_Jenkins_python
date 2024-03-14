from pymongo import MongoClient

uri = "mongodb://root:123@192.168.56.200:27017/"

client = MongoClient(uri)
print(client)
# use the database object
db = client['myapp']
# use the collection
collection = db['Records']
document = {"name":"mehans","age": 33}
result = collection.insert_one(document)
print("inserted_one:", result.inserted_id)
allrecords = collection.find()
print(allrecords)
for all in allrecords:
    print(all)

client.close()