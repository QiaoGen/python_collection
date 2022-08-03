# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 基础
print("Hello, world!")
print('stay hungry,', 'stay young')
print('100 + 200 =', 100 + 200)
# name = input()
# print('hello', name)

# 数据类型 变量
intNum = 1
floatNum = 1.1
floatNum1 = 1e10
floatNum2 = 1e-10
hexNum = 0xff
string = 'I\'m \"OK\" \n换行\ttab'
print(string)
print('''line1
... line2
... line3''')
print(r'''line1
line2
line3''')

# 编码
print(ord("A"))
print(chr(65))
# print(ord('可'))
print(b'abc')
print("A".encode('ascii'))
print('中'.encode(('utf8')))
# %d %f %s %x 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)
r = 2.5
s = 3.14 * r ** 2
# print(f'The area of a circle with radius {r} is {s:.2f}')

# 集合list/tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[-1])
classmates.append('JoJo')
print(classmates)
classmates.insert(1, 'Drogon')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
ttt = ('test')
print(ttt)

# 条件判断
age = 16
if age > 18:
    print('age is enough')
elif age > 14:
    print('you can dagong')
else:
    print('too young')

# 循环
sum = 0
for nx in [1,2,3,4,5,6,7,8,9]:
    sum += nx
print(sum)
print(range(5))
sum = 0
n = 99
while n > 0:
    sum = sum + n
    if sum > 1000:
        break
        # continue
    n = n - 2
print(sum)

# 内置字典dict set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d.pop('Michael')
s = set([1, 2, 3])
s.add(4)
s.remove(4)
print(s)
# & 交集 ｜ 并集

# 函数
print(hex(100))
def my_abs(x):
    pass
    return abs(x)


# 高级特性
# 切片 字符串/tuple/list
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 或者 L[:3] L[1:3] 倒数切片L[-2:-1] L[-1:]
print(L[0:3])
# 迭代 str/list/tuple/dict
for ch in 'ABC':
    print(ch)
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)
# 索引-元素对 enumerate函数
for i, k in enumerate(d):
    print(i, k)
# 列表生成式 List Comprehensions
print(list(range(1,11)))
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
# dict => list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])
# 转换大小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
