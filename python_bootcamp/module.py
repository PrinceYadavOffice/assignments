import requests

url='https://api.github.com/search/repositories'
data =requests.get(url, params={'q': 'requests+language:python'},)

print(data.json()['total_count'])

def http_get(url2):
    data = requests.get(url2)
    print(data.headers)
    print(data.text)

def http1_put(url2):
    url2 = url2 + "/put"
    data = requests.put(url2)
    print(data.headers)

def http_post(url2):
    url2=url2+"/post"
    data = requests.post(url2)
    print(data.headers)
    print(data.status_code)

def http_delete(url2):
    url2 = url2 + "/delete"
    data=requests.delete(url2)
    print(data.headers)
    print(data.status_code)

url2='https://httpbin.org'
http_get(url2)
http_post(url2)
http_delete(url2)
http1_put(url2)
