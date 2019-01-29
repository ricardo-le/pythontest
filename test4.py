import requests
from bs4 import BeautifulSoup
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
res = requests.get('https://bookset.me/', headers)
res2 = requests.get('https://book.douban.com/',headers)
soup = BeautifulSoup(res2.text, 'html.parser')
# cards=soup.find_all('div', "card-item")
# name = soup.selector('#cardslist > div:nth-of-type(1) > div > h3 > a ')
name1 = soup.select('#content > div > div.article > div.section.books-express > div.bd > div > div > ul:nth-of-type(2) > li > div.info > div.title > a')
f = open('D://name.txt' , 'w')
print(name1)
for name in name1:
    f.write(name.get_text())
    f.write('\n')
    print(name.get_text())


