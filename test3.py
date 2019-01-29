import requests
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# res = requests.get('https://bookset.me/',headers)
res= requests.get('https://www.google.com', headers)
try:
    print(res.text)
except TimeoutError:
    print('连接超时')