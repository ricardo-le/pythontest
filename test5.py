import urllib.request
from lxml import etree
# request = urllib.request('https://bookset.me/')
# html = urllib.urlopen(request).read()
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = urllib.request.get('https://bookset.me/', headers)
content = etree.HTML(html)
name = content.xpath('//*[@id="cardslist"]/div[2]/div/h3/a')
print(name)
