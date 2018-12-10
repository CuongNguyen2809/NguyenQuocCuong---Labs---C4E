from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customer = db['customers']
eve_counts = 0
wom_counts = 0
adv_counts = 0
for refence in customer.find():
    if refence['ref'] == "events":
        eve_counts += 1
    elif refence['ref'] == "wom":
        wom_counts += 1
    elif refence['ref'] == 'ads':
        adv_counts +=1

ref_counts = [eve_counts, wom_counts, adv_counts]

pyplot.pie(ref_counts, labels = ["Eve"," Wom","ADV"], autopct = "%.1f%%",shadow = True,explode=[0,0.1,0.1])
pyplot.title('Events Advertisements and Worth of month')
pyplot.axis("equal")
pyplot.show()

client.close