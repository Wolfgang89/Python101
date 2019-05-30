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
