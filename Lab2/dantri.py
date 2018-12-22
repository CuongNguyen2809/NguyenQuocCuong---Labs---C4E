from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#1. Download trang 
url ="https://dantri.com.vn"
#1.1 open a conection to server
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode dataa
page_content = raw_data.decode("utf8")

# print(page_content)

# f = open("dantri.html","wb")
# f.write(raw_data)
# f.close()

#2 Extractt ROI
soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew")
#3 Extract data
li_list = ul.find_all("li")

# for li in li_list:
#     print(li.prettify())
new_list = []
for li in li_list:
    a = li.h4.a
    title = a.string

    link =url + a["href"]   
    
    news = {
        "title" : title,
        "Link" : link
    }   
    new_list.append(news)
    



#4 Save data to excel

pyexcel.save_as(records = new_list , dest_file_name = "dantri.xlsx")

