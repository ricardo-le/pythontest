import urllib.error
import socket
import urllib.request
try:
    response =urllib.request.urlopen('http://httpbin.org/get', timeout =0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('time out')