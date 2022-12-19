import requests
from bs4 import BeautifulSoup
import bs4
import lxml


class Scrabing:
    def __init__(self):
        self.url = "https://www.amazon.com/dp/B075L7QHCH/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
            "Accept-Language": "en-US,en;q=0.9"}
        response = requests.get(self.url, headers=self.headers)
        self.soup = bs4.BeautifulSoup(response.content, "lxml")

    def Get_Price(self):
        price_number = self.soup.find(name="span", class_="a-offscreen").getText()
        price_without_tag = float(price_number.split("$")[1])
        return price_without_tag

    def Get_Title(self):
        product_title = self.soup.find(id="productTitle").getText()
        return product_title