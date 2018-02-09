import requests


# GEt请求
req_get = requests.get('https://www.douban.com/',timeout=2.5)
print("status:",req_get.status_code)
print("text:",req_get.text)
# 获得bytes对象
print("content",req_get.content)
print("cookies",req_get.cookies)

# 对于带参数的URL，传入一个dict作为params参数：
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

# 需要传入HTTP Header时，传入一个dict作为headers参数：
# >>> r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

# POST请求
# requests默认使用application/x-www-form-urlencoded对POST数据编码。
# 传入data参数作为POST请求的数据：
url='https://accounts.douban.com/login'
req_post = requests.post(url, data={'form_email': 'abc@example.com', 'form_password': '123456'})
print("status",req_post.status_code)
print("cookies",req_post.cookies)
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON
print('header',r.headers['Content-Type'])
# 在请求中传入cookies,只需准备一个dict传入cookies参数：
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url, cookies=cs)