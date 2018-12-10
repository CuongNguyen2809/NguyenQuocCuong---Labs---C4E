from pymongo import MongoClient

uri ="mongodb://admin1:admin1@ds129454.mlab.com:29454/c4e24-lab1"
client = MongoClient(uri)

db = client.get_database()
post_colection = db["posts1"]

new_post = {
    "Name" : "Hạnh Phúc Khi Có Em",
    "Singer" : "Phúc Bồ",
    "Kind" : "Young music",
    "Year" : "unknown"
}

post_colection.insert_one(new_post)
client.close