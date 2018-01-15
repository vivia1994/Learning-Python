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


