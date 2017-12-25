import requests
r = requests.get('http://www.hm.com')
print(r.encoding)