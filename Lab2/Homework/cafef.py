from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content, "html.parser")

box = soup.find("div", "cf_ResearchDataHistoryInfo")

table = box.find("table", id="tableContent")

tr_list = table.find_all("tr")

data = []

for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string
        td_content = {
            "content": td
        }
        data.append(td_content)


pyexcel.save_as(records= data , dest_file_name="cafes.xlsx")