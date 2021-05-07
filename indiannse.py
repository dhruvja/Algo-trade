import mysql.connector
import bs4 
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup 
from datetime import datetime
import functools 
import operator
db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'password', database = 'stocks')
print(db)
mycursor = db.cursor()
stock = input("Enter the name of the stock")
numberofstocks = input("Enter the number of stocks")
try:
    r = requests.get('https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r. text,'lxml')
    price = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
except AttributeError:
    print("Wrong Stock Sybmol, try again")
mycursor.execute("CREATE TABLE IF NOT EXISTS `" + stock + "` ( `id` INT NOT NULL AUTO_INCREMENT , `trackorder` FLOAT NULL , `buyprice` FLOAT NULL DEFAULT '0' , `buytime` VARCHAR(255) NULL , `soldprice` FLOAT NULL DEFAULT '0' , `soldtime` VARCHAR(255) NULL , `algoprofit` FLOAT NULL DEFAULT '0' , `traderprofit` FLOAT NULL DEFAULT '0' , PRIMARY KEY (`id`))")
mycursor.execute("SELECT trackorder FROM `" + stock + '` ORDER BY id DESC LIMIT 1')
orderid = 0
myresult = mycursor.fetchall()
for c in myresult:
    orderid = c
    orderid = functools.reduce(operator.add, (orderid))
orderid += 1
threshold = 20
g = 0
l = 0
x = 0
currenttime = "0"
startprice = 0
buyprice = 0
profit = 0
def parsePrice():
    #stock = 'BTC-INR'
    #r = requests.get('https://finance.yahoo.com/quote/'+stock+'?p='+ stock+'&.tsrc=fin-srch')
    try:
            r = requests.get('https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch')
            soup = bs4.BeautifulSoup(r. text,'lxml')
            price = soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    except ConnectionError:
        price = 0,000,00
    return price

while True:
    try:
        stkprice = parsePrice()
    except AttributeError:
        stkprice = parsePrice()
    now = datetime.now().time()
    stkprice = float(stkprice.replace(',',''))
    numberofstocks = float(numberofstocks)
    #stkprice = float(stkprice)
    stkprice *= numberofstocks
    print("The Price of "+ str(numberofstocks) +" shares of "+ str(stock) +" at " + str(now) + " is: " + str(stkprice))
    if g-stkprice > threshold and x == 1:
        print("Sold")
        effectiveprice = stkprice - startprice
        profit = profit + (stkprice - buyprice)
        print("profit: " + str(profit))
        print("Opponent profit: "+ str(effectiveprice))
        print("Start price: " + str(startprice))
        now = datetime.now()
        now = str(now)
        print(currenttime)
        sql = "UPDATE `" + stock + "` SET soldprice = %s, soldtime = %s, algoprofit = %s , traderprofit = %s WHERE buytime = %s"
        val = (stkprice,now,profit,effectiveprice,currenttime)
        mycursor.execute(sql, val)
        db.commit()
        x = 0
        l = stkprice
    elif stkprice - l > threshold and x == 0:
        buyprice = stkprice
        if l == 0:
            startprice = stkprice
        print("Bought") 
        orderid = float(orderid)
        now = datetime.now()
        now = str(now)
        currenttime = now
        sql = "INSERT INTO `" + stock + "` (trackorder,buyprice,buytime) VALUES(%s,%s,%s)"
        val = (orderid,stkprice,now)
        mycursor.execute(sql, val)
        db.commit()
        x = 1
        g = stkprice
    if stkprice > g and x == 1 :
        g = stkprice
    elif stkprice < l and x==0 :
        l = stkprice