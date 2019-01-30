import requests
from bs4 import  BeautifulSoup
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
res= requests.get('https://bookset.me/', headers)
soup= BeautifulSoup(res.text,'html.parser')
names = soup.select('#cardslist > div > div > h3 > a')
names1 = soup.select('#cardslist > div:nth-of-type(2) > div > h3 > a')
print(names1)