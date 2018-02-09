# generator
# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1
#
#
# for i in countdown():
#     print(i)

# decorator
# def decor(func):
#   def wrap():
#     print("============")
#     func()
#     print("============")
#   return wrap
#
# @decor
# def print_text():
#   print("Hello world!")
#
# print_text()


#lambda
# a = (lambda x: x*(x + 1))(6)
#
# print(a)

#recursion
# def factorial(x):
#   if x==1:
#     return 1
#   else:
#     return x * factorial(x-1)
#
# print(factorial(5))


# itertools
# from itertools import accumulate, takewhile
#
# nums = list(accumulate(range(8)))
# print(nums)
# print(list(takewhile(lambda x: x<= 6, nums)))

# #product permulation
# from itertools import product, permutations
#
# letters = ("A", "B")
# print(list(product(letters, range(3))))
# print(list(permutations(letters)))

# nums = [1, 2, 8, 3, 7]
# res = list(filter(lambda x: x%2 == 0, nums))
# print(res)



# re
# import re
#
# pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# str = "Please contact info.-v@sololearn.com for assistance"
#
# match = re.search(pattern, str)
# if match:
#    print(match.group())

# numpy
# shape 检查矩阵尺寸


# def numpy_test():
#     import numpy as np
#     # mylist = [1, 2, 3]
#     # x = np.array(mylist)
#     # print(x)
#     # m=np.array([[7, 8, 9], [10, 11, 12]])
#     # # find the dimensions of the array.(rows, columns)
#     # print(m.shape)
#     # n=np.arange(0,30,2)# start at 0 count up by 2, stop before 30
#     # return n.reshape(3, 5) # reshape array to be 3x5
#     # o = np.linspace(0, 4, 9)#return 9 evenly spaced values from 0 to 4
#     # o.resize(3,3)#changes the shape and size of array in-place.
#     print("ones",np.ones((3,2)))
#     print("zeros",np.zeros((3,2)))
#     print("eye",np.eye(3))
#     print("diag",np.diag(np.eye((3))))
#     print("array",np.array([1, 2, 3] * 3))
#     print("repeat",np.repeat([1, 2, 3], 3))
#     p = np.ones([2, 3], int)
#     print(p)
#     print("vstack",np.vstack([p, 2*p]))#stack arrays in sequence vertically (row wise).
#     print("hstack",np.hstack([p, 2 * p]))
#     x=np.array([1,2,3])
#     y=np.array([[1],[2],[3]])
#     print("dot",x,y,x.dot(y))
#
#     y = np.array([[1], [2], [3]])
#     print("transpose",y,y.T,y.dtype)    #transpose the matrix
#
#     a = np.array([-4, -2, 1, 3, 5])
#     print("mean","std","argmax argmin",a,a.mean(),a.std(),a.argmax(),a.argmin())
#
#     s = np.arange(13)
#     print("slice",s,s[-4::2])
#
#     r = np.arange(36)
#     r.resize((6, 6))
#
#     print("multiArray slice",r,r[2,2:6])
#     print(r[:2, :-1])
#     print(r[-1, ::2])
#
#     r[r > 30] = 100
#     print(r)
#
#     r2 = r[:3, :3]
#     print(r2)
#     r2[:] = 0   #这里会改变r的值，应该用r2=r.copy()
#     print(r)
#
#     test =np.random.randint(0,10,(4,3))
#     print(test,len(test))
#     for i in range(len(test)):
#         print("ss",test[i])
#     for i, row in enumerate(test):#对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
#         print('row', i, 'is', row)#enumerate多用于在for循环中得到计数
#     test2 = test ** 2
#
#     for i, j in zip(test, test2):
#         print(i, '+', j, '=', i + j)
#
# numpy_test()



# map
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
# def split_title_and_name(person):
#
#     title = person.split()[0]
#     lastname = person.split()[-1]
#     print(person.split(),title,lastname)
#     print('{1} {0}'.format(title, lastname))
#     return '{} {}'.format(title, lastname)
# list(map(split_title_and_name, people))

#
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
# print("{:.2f}".format(3.1415926));


# lambda
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
# def split_title_and_name(person):
#     print(person.split()[0] + ' ' + person.split()[-1])
#     return person.split()[0] + ' ' + person.split()[-1]
# #option 1
# for person in people:
#     print((lambda x: x.split()[0] + ' ' + x.split()[-1])(person))
# #option 2
# list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))


# def times_tables():
#     lst = []
#     for i in range(10):
#         for j in range (10):
#             lst.append(i*j)
#     return lst
#
# times_tables() == [j*i for i in range(10) for j in range(10)]

# lowercase = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
# correct_answer =[a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
# print(correct_answer[:50])
# correct_answer[:50]

# print(type(lambda x: x+1))


# import numpy as np
# from sklearn import linear_model
#
# x = np.array([[0, 1], [1, 1], [2, 1]])
# y = [[0], [2], [5]]
#
# clf = linear_model.LinearRegression()
# clf.fit(x[:, :-1], y)
# print(clf.coef_)
# print(clf.intercept_)
#
# theta = np.ones((2, 1))
# alpha = 0.05
# m = 3
# numIterations = 10
#
#
# def gradientDescent(x, y, theta, alpha, m, numIterations):
#     xTranspose = x.transpose()
#     for i in range(0, numIterations):
#         hypothesis = np.dot(x, theta)
#         #         print("hypothesis",hypothesis)
#         loss = np.sum((hypothesis - y) ** 2) / (2 * m)
#         gradient = np.dot(xTranspose, (hypothesis - y)) / m
#         theta = theta - alpha * gradient
#     #         print("theta",theta)
#     return theta
#
#
# gradientDescent(x, y, theta, alpha, m, numIterations)



# error raise
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
# bar()


# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')



# assert
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
#
# foo('0')

#
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


# with
# with open("_Data/prices.txt","r",encoding="gbk") as f:
#     s=f.read()
#     print(s)

# # StringIO
# from io import StringIO
#
# # write to StringIO:
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())
#
# # read from StringIO:
# f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# BytesIO
# from io import BytesIO
#
# # write to BytesIO:
# f = BytesIO()
# f.write(b'hello')
# f.write(b' ')
# f.write(b'world!')
# print(f.getvalue())
#
# # read from BytesIO:
# data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
# f = BytesIO(data)
# print(f.read())

# pickling
# import json
# d = dict(name="bob",age=20,score=88)
# json.dumps(d)
# print(json.dumps(d))



# itertools
# import itertools
# natuals = itertools.count(1)


# urllib
# GET
# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# # 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。\
# # 例如，模拟iPhone 6去请求豆瓣首页：
#
# with request.urlopen(req) as f:
#     data = f.read()
#     with open(r"C:\Users\vlei002\Desktop\1.txt","w") as file:
#         file.write('Status:')
#         file.write(str(f.status))
#         file.write(f.reason)
#     for k, v in f.getheaders():
#         with open(r"C:\Users\vlei002\Desktop\1.txt", "a") as file:
#             file.writelines('%s: %s' % (k, v))
#     with open(r"C:\Users\vlei002\Desktop\1.txt", "ab") as file:
#         file.write(data)

# POST
# from urllib import request,parse
# print("Login to zhihu...")
# email = input("Emal:")
# password = input("Password:")
# login_data=parse.urlencode([
#     ('username', email),
#     ('password', password),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# HTMLParser
# from html.parser import HTMLParser
# from html.entities import name2codepoint
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print("handle_starttag--",'<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print("handle_endtag--",'</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print("handle_startendtag--",'<%s/>' % tag)
#
#     def handle_data(self, data):
#         print("handle_data--",data)
#
#     def handle_comment(self, data):
#         print("handle_comment--",'<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print("handle_entityref--",'&%s;' % name)
#
#     def handle_charref(self, name):
#         print("handle_charref--",'&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')
#


import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
res=requests.get('http://hu.58.com',headers=headers)
print(res.text)