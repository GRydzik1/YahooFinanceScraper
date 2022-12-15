from bs4 import BeautifulSoup
import requests
import re
stock_data=[]

#Some code in this function used from https://www.youtube.com/watch?v=Xus_Qno_kfg
def get_stock_data(stock_ticker):
    #User agents code taken from https://www.youtube.com/watch?v=90t9WkQbQ2E
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    url = 'https://finance.yahoo.com/quote/' + stock_ticker + '?p=' + stock_ticker
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    price = str(soup.find_all('div', {'class':'D(ib) Mend(20px)'})).replace(',', '')
    # taken from https://www.tutorialspoint.com/Extract-decimal-numbers-from-a-string-in-Python
    cheeseburger = re.findall("\d+\.\d+", price)
    price = float(cheeseburger[0])
    print(str(stock_ticker) + "=" + str(price))
    stock_data.append(price)




