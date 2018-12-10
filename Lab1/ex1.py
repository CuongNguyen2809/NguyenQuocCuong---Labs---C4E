from pymongo import MongoClient

uri ="mongodb://admin1:admin1@ds129454.mlab.com:29454/c4e24-lab1"
client = MongoClient(uri)

db = client.get_database()

account_colection = db["account"]
 
new_account = {
    "username" : "nguyencuong2",
    "email" : "abcde@gmail.com",
    "phone" : "012345678",
    "password" : "abc12345",
    "yob" : "1998"
}

account_colection.insert_one(new_account)
client.close
