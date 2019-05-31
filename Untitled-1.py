# y = 33
# x = y // 2
# while x > 1:
#     if y % x  == 0:
#         print('{} has a factor因子 {}'.format(y,x))
#         break
#     x = x - 1
# else:
#     print('{} is prime质数'.format(y))
# y = 29
# x  = y // 2
# while x > 1:
#     if y % x == 0:
#         print('{} has a factor {}'.format(y,x))
#         break
#     x = x - 1
# else:
#     print('{} is prime质数'.format(y))

# for x in [1,2,3,4,5]:
# for x in 'hello':
# for x in ('i', 'am', 'a', 'teacher'):
    # print(x,end=' ')
# T = [(1, 2), (3, 4), (5, 6)]
# for (a,b) in T :
#     print(a,b)
# D  = {'a':1,'b':22,'c':45}
# for key in D:
    # print(key,'----->',D[key])
# for (key,value) in D.items():
#     print(key,'---->',value)
# 循环迭代的高级技巧 range zip enmuerate
# for x in range(5):
    # print(x,end =',')
# print(list(range(-5,5)))
# 内置函数range在for循环中是最常用的，它提供了一种简单的方法，重复特定次数的动作。在遍历的过程中跳过一些元素
# S = 'abcdefghijklmnjsielpsjhsgsjaka'
# for i in range(0,len(S),2):
#     print(S[i], end=',')
# 间隔 最好用的就是切片
# for c in S[::2]:
    # print(c, end=',')
# zip可以用来并行迭代多个序列
# L1 = [1,2,3,4,5,6,]
# L2 = ['a','v','c']
# for x in zip(L1,L2):
#     print(x, end=',')
# print(list(zip(L1,L2)))

# 使用zip生成字典
# keys = ['A', 'B', 'C']
# vals = [1, 2, 3]
# D = dict(zip(keys,vals))
# print(D)
# S = 'spam'
# print(dict(enumerate(S)))
# for t in enumerate(S):
    # print(t,end='')

#列表解析式和字典解析式
#列表解析式 -- 本质上就是用列表来构建列表，通过对已有列表中的每一项应用一个制定的表达式来构建出一个新的列表
#字典解析式 --  使用字典和列表的数据构建一个新的字典
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [x**2 for x in a if  x % 3 == 0]
# print(b)
# 字典造字典
# D1 = {'a': 1, 'b': 2, 'c': 3}
# D2 = {k:v*2 for (k,v) in D1.items()}
# print(D2)
# 列表 造字典
# D = {c:c*4 for c in ['a',1,'2']}
# print(D)
# 字符串
# s = 'abcdefg'
# print(s[0])
# print(s[-2])
# print(s[1:4])
# bd 2 表示步长 隔2最右边不取 1索引隔2 就是3 4 4不取 取1 3 打出来就是bd
# print(s[1:4:2])
# bcd
# print(s[1:4:1])
#  从-1 到1 最后到1索引 间隔是1 -1是因为是从右边开始算的
# print(s[-1:1:-1])
# print(s[-1:1:-3])
# 字符串的不可修改性
# S1 = 'abcd'
# s [0] = '4' 'str' object does not support item assignment
# S2 = '124'
# S = S1 + S2
# print(S)
# 字符串的赋值 分 深拷贝 和 浅拷贝
#  深拷贝 即 赋值时 两个对象具有相同的值 但是手机在不用的内存片区的对象 浅拷贝 即 等号左右两边的对象实际上被分配的是同一个内存空间
# s = ['abcdefg']
# a = s [:]
# print(a)
# print(s is a)
# s1 = 'abcdefgt'
# s2 = s1
# print(s1 == s2)
# 字符串的遍历 成员测试
# s = 'hacker'
# for c in s:
#     print(c,end= ' ')
# print('k' in 'momonthor')
# s = 'ahsisjahaa'
# print(s.find('ha'))
# print(s.find('zz'))
# print(s.replace('ha','XXX'))
# s = 'Tom,21,USA,UCLA'
# l = s.split(',')
# print(l)
# L = ['s', 'p', 'a', 'm', 'm', 'y']
# s = '-'.join(L)
# print(s)
# s = '   Tom 21 USA UCLA\n\n'
# print(s)
# print(s.strip())
# name = '盘尾'
# age = 29
# school = ['CHXY']
# s = 'name :{},age:{},and graduates form {}'.format(name,age,school)
# print(s)
# template = '{1},{0} and {2}'
# s = template.format('spam','ham','eggs')
# print(s)
# template = '{key1},{key2} and {key3}'
# s = template.format(key1  = 'spam',key2 = 'ham',key3 = 'eggs')
# print(s)
# template = 'float number = {:.2f}'
# s = template.format(10.92625452)
# print(s)
# template3 = 'number ={:b}'
# s = template3.format(2**16 -1)
# print(s)
# 字符转义 \t \n 等 和c一样
# S1 = 's\tname\ne'
# print(S1)
# s = r'c:\new\test.py'
# print(s)
# s = '19'
# i = 3
# print(s+str(i))
# print(float('1.5'),str(4.56))
# print(bin(12))
# print(int('1110',2))
#       字符编码
# 计算机自己能理解的语言是二进制数，最小的信息标识是二进制位，8个二进制位表示一个字节，编码就是把人类使用的这些字符集转换为计算机所能理解的二进制码
# 
Unicode = '编码方式'
# 字符编码和字符编码



