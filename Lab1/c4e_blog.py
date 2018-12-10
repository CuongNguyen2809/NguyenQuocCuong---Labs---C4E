from pymongo import MongoClient


#1. kết nối datebase server
uri ="mongodb://admin1:admin1@ds129454.mlab.com:29454/c4e24-lab1"
client = MongoClient(uri)


#2. chọn datebaseI()
db = client.get_database()


#3.chọn colection 
post_colection = db["posts"]
for post in post_colection.find():
    print(post)

# #4. Tạo document
# new_document = {
# "title": "Hom nay khong muon code",
# "post": "Minh met "
# }


# #5. Đưa document vào trong colection
# post_colection.insert_one(new_document)

#6.Ngắt kết nôi
client.close