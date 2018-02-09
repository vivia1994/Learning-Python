import chardet
data = '离离原上草，一岁一枯荣'.encode('gbk')
a = chardet.detect(data)
print(a)

data = '离离原上草，一岁一枯荣'.encode('utf-8')
b = chardet.detect(data)
print(b)