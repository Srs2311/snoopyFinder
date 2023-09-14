import bs4
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
HAWEBHOOK = os.getenv('WEBHOOK')



def requestSite(url,headers):
    res = requests.get(url, headers=headers)
    return res.text

def snoopyCheck():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    reqTxt = requestSite("https://www.ae.com/us/en/p/women/loungewear-pjs/pajamas-pj-sets/ae-peanuts-fall-plush-pj-set/0575_2946_143?menu=cat4840004",headers)
    snoupy = bs4.BeautifulSoup(reqTxt,'html.parser')
    stockHTML = snoupy.select('.product-oos-label')
    if (len(stockHTML) != 0):
        print("out of stock")
    else:
        requests.post(HAWEBHOOK)

#main loop
while(True):
    snoopyCheck()
    time.sleep(300)