import requests
from bs4 import BeautifulSoup
import smtplib

url='https://www.flipkart.com/samsung-galaxy-s9-midnight-black-64-gb/p/itmf33a69rpszgzn?pid=MOBF2VWVBGCT5QQN&lid=LSTMOBF2VWVBGCT5QQN0ZJFUP&fm=neo%2Fmerchandising&iid=M_ee4d4e81-9b71-4f02-823e-b1dbff9affd8_4.JGRYD3DYW1F6&ssid=ioxilr7onk0000001584802984282&otracker=hp_omu_Top%2BOffers_4_4.dealCard.OMU_Top%2BOffers_JGRYD3DYW1F6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_4_NA_view-all_3&cid=JGRYD3DYW1F6'
headers = {"User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def product():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find('span',attrs={"class":"_35KyD6"}).text
    price=soup.find('div',attrs={"class":"_1vC4OE _3qQ9m1"}).text
    print(title)
    print(price)
    c_price=price.split('₹')[1]
    c_price=int(c_price.replace(',',''))
    if(c_price<20000):
        send_mail()
    else:
        print("Price has not dropped!\n")

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jaiswalaman97@gmail.com','lkwrbetnewbctfhk')

    subject='Price fell down!'
    body='Check the link:\
    https://www.flipkart.com/samsung-galaxy-s9-midnight-black-64-gb/p/itmf33a69rpszgzn?pid=MOBF2VWVBGCT5QQN&lid=LSTMOBF2VWVBGCT5QQN0ZJFUP&fm=neo%2Fmerchandising&iid=M_ee4d4e81-9b71-4f02-823e-b1dbff9affd8_4.JGRYD3DYW1F6&ssid=ioxilr7onk0000001584802984282&otracker=hp_omu_Top%2BOffers_4_4.dealCard.OMU_Top%2BOffers_JGRYD3DYW1F6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_4_NA_view-all_3&cid=JGRYD3DYW1F6'

    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail('Price check','jaiswalamisha25@gmail.com',msg)
    print('Hey Email has been sent!')
    server.quit()

product()
