import requests
from bs4 import BeautifulSoup
import time  # Import time module

class PriceTracer:
    def __init__(self,url):
        self.url = url
        self.user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        # Add a sleep here to introduce a delay after making the request
        time.sleep(4)  # Sleep for 3 seconds before making the request
        self.response = requests.get(url = self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response,"lxml")


    def product_title(self):
        title = self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            #return title.text.strip()
            return title.get_text(strip=True)
        else:
            return "Tag Not Found"

    def product_price(self):
        #price = self.soup.find("span", {"class": "a-price-whole"})
        price = self.soup.find("span", {"class": "a-offscreen"})
        if price is not None:
            #return price.text
            return price.get_text(strip=True)
        else:
            return "Tag Not Found"


#device = PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CQYGF1QY/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.MobfHHxc0LwYdAovAMzdoEPS3uGzDKBYHzz7Jwirux0wCpO1TS4reKULXUEaY9r7HgfDSCMy6dRq0zbBH0ZwNL4TW-YgwwjWL8jm7yD6sQjxZR6sUfS4d8V7o1Vp3V4L9roimyz3jPoGcIlU2qwycHEwEcdksybxkQJjTbIfFwnuNx0E-bPWjHuV823QwMxu2i_qkPSL5Gt2wipvq2jpvQBKgUdkoelUqdOcJ1PS9fQXGOWH6OPuHxkMAHCKSN56QA6Cck32_NNFSE7NtA1E9H9wN1aB1w5C2GroB1wo1fI.lSGV232Gi3iUpSMTGkSbR0x3hbHh2-QB4xOWqJ9nGrM&dib_tag=se&qid=1714727353&refinements=p_89%3ASamsung&rnid=3837712031&s=electronics&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&psc=1")
device = PriceTracer(url="https://www.amazon.in/Redmi-Startrail-Storage-MediaTek-Dimensity/dp/B0CNX6WVG5/?_encoding=UTF8&pd_rd_w=oRVJS&content-id=amzn1.sym.c9e0afd1-c827-47cf-a99b-eb12656bac94&pf_rd_p=c9e0afd1-c827-47cf-a99b-eb12656bac94&pf_rd_r=MEFD5VSNXGZHEWDTXTVZ&pd_rd_wg=zjmXq&pd_rd_r=ecf0015c-4f1c-4379-814e-db4489cbe8c5&ref_=pd_hp_d_atf_dealz_pd&th=1")
print(device.product_title())
print(device.product_price())