import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")

my_db = my_client["firstTime"]

my_collection = my_db["firstTimeCollection"]
print(my_collection.count_documents({}))
# FILTER and FIND documents by putting in value of key taht you want to search by
# example: my_collection.delete_one({"__id":0})
# UPDATE - by finding with a parameter then using set
# example: my_collection.update_one({"__id":5},{"$set:":{"key":"value"}})