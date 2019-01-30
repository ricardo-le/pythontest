import requests
from bs4 import BeautifulSoup
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
res = requests.post('https://www.smzdm.com/', headers)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
names = soup.select('#feed-main-list > li > h5 > a')
for name in names:
    print(name.get_text)
