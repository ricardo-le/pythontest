import requests
from lxml import etree
from bs4 import BeautifulSoup
# request = urllib.request('https://bookset.me/')
# html = urllib.urlopen(request).read()
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get('https://bookset.me/', headers)
content = etree.HTML(html.text)
#获取a中href的值
hrefs = content.xpath('//*[@id="cardslist"]/div/div/h3/a/@href')
titles =content.xpath('//*[@id="cardslist"]/div/div/h3/a/@title')
print(len(hrefs))
for index in range(len(hrefs)):
    # print(names[index].attrib.href)
    print(hrefs[index])
    print(titles[index])
#普通获取
names = content.xpath('//*[@id="cardslist"]/div/div/h3/a')
print(len(names))
for r in range(len(names)):
    print(names[index].attrib)
    print(names[index].text)


