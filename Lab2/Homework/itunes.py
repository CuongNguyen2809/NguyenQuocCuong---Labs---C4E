from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")

new_list = []
for li in li_list:
    h3 = li.h3.a
    h4 = li.h4.a
    song = h3.string
    singer = h4.string
    song = OrderedDict({
        "song" : song ,
        "singer" : singer
    })
    
new_list.append(song)
pyexcel.save_as(records=new_list,dest_file_name = "itunes.xlsx")