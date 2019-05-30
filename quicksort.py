
# def quicksork(array):

#     if len(array) < 2:
#         return array
#     else:
#         pv = array[0]
        
#         less = [i for i in array[ 1:] if i <= pv]

#         great = [i for i in array[1:] if i > pv]

#         return quicksork(less) + [pv] + quicksork(great)


# print(quicksork([3,80,6,89,10]))


# L = [1,2,3,4,5,6,7,8]

#左索引 开始是0 结束是0数过去2 个 所以 打印出来是 1 2 省略了开始的0索引 是左索引
# print("切片111",L[:2])
# 最左是0 最右是-1 可以省略左右的终点 -1意思是最右的元素不要了 4 是元素的个数 倒数3个
#负索引的表示法，即从右往左数，最右侧是-1，往左依次减1，即-2，-3以此类推： 所以 就是第三个索引到左边结束 但是不包含
# 左开右闭
# print("负索引切片222",L[3:-1])
# print("省略负索引切片333",L[3:])
# print("正索引省略切片444",L[:3])
# print("正索引不省略切片555",L[0:3])
# 切片 右边开始第一个开始 间隔三
# print(L[0::3])

# 如果对截取出的分片进行修改 ，会影响到原始的列表吗  ？
#实验  如下
# b = L[3:-1]
# print('before change:b={}'.format(b))
# # 修改b的value
# b[0] = 111
# print('after change:b={}'.format(b))
# print('after change:L={}'.format(L))
# # 结论 不影响原来的数组 用变量b获取了L的分片后，实质是获取了L分片的一个新的独立拷贝。因此，你在列表b上做修改，是影响不了L的。

#python的 list的三个优点 1.元素本地可修改 直接在原来的内存地址上修改list对象 不需要做新的拷贝 2. 有序性 可使用切片 访问简单
#3. 可存任何的种类 任意类型的对象 甚至可以嵌套列表 易构性

# 增加元素
# L.append(90)
# print(L)
# L.insert(86,99)
# print(L)
# L.extend([11,22,33])
# print(L)
#  结论 append只是在结尾加入 insert 在任意索引 假如索引大于最大长度 不报错直接加到尾部 extend加入多个元素
# 插入是就地修改 而不是返回修改后的新列表 所以 insert的返回值是none 会彻底失去之前的列表的引用，所以类型错误了
# N = [1,2,3,4,5]
# M = N.insert(6,2)
# print(M)
# #None M是none
# print(N[2])
# #3
# 删除 remove删除元素 del删除切片  pop删除末尾 返回被删除的对象
# L1 = ['aa','bb','cc']
# L = L1.remove('aa')
# print(L)
# none
# print(L1)
#bb cc
# 1-3  3是因为[） 需要加一个索引才能删的干净
# del L1[1:3] 
# print(L1)
# 就剩下aa
# print(L1.pop())
# print(L1)
# 修改 直接修改 和分片赋值 本地排序
# L = [4,5,6,7,8,9]
# L[1:3] = ['aa','bb','cc']
# print(L) 
# [4, 'aa', 'bb', 'cc', 7, 8, 9] 直接替换掉了 5 6  
#分片赋值的本质是先在原列表上删除指定分片，然后在删除的位置插入新的列表，因此左右两边的长度可以不等。
# 本地排序 直接在本地修改 返回也是none
# L = [1,3,11,33,90,5,6,10]
# # 升序
# L.sort()
# print(L)
# # 反转
# L.reverse()
# print(L)

# 字典 字典中的对象是无序的  kv 来反映映射关系 k取v  异构
# 生成 读取 修改

# D = {
#     'name':{
#         'first':'Bob','last':'Smith'
#     },
#     'job':['dev','mgr'],
#     'age':0.5,
#     'addr':'BeiJing'
# }

# D['age'] = 20
# print(D)
# D = {}
# D['name'] = 'gang'
# D['job'] = 'engineer'
# print(D)
# key_list = ['a','b','c','d']
# value_list = [11,22,33,44]
# D = dict(zip(key_list,value_list))
# print(D)
# 元组  合并字典/ cswq  qy'lkjh\
# 字典中的键冲突的话 会无规律的进行覆盖 应该避免
# D1 = dict([('aa',11),('bb',22),('cc',33)])
# D1.update(D)
# print(D1)
# key 不存在
# D = {'a':1,'b':2, 'c':3}
# # KeyError
# print(D['d'])
# D = {'a':1,'b':2}
# print('c' in D)
# if not 'c' in D:
    #  print('missing')
# E = {'a':11,'b':22,'c':'sss'}
# print(E.get('d',0))
# print(list(D.keys()))
# print(list(D.values()))
# print(list(D.items()))
# del D['addr']
# print(D.pop('addr'))
#排序 对Key 只是对key的排序
# print(sorted(D))
# print(sorted( D.keys()))
# 元组
# a,b = (1,2)
# print('a={},b={}'.format(a,b))
# T1 = (1,2,3,4)
# T2 = (5,6,7,8)
# print(T1 + T2)
# T = ('cc','bb','dd','aa')
# print(sorted(T))
#  列表 字典 数组
# 循环  容器遍历 解析

# a = 0
# b= 10
# while a < b:
#     a = a + 1
#     # if a % 2 !=0:
#         # continue
#     if a  == 5:
#         break

#     print(a,end=' ')
# y = 33
# x = y
# while x > 1:
#     if y % x == 0:
#         print('{} has a factor {}'.format(y,x))
#         break
#     x = x - 1
# else:
#     print('{} is prime'.format(y))


# y = 29
# x = y 
# while x > 1:
#     if y % x == 0:
#          print('{} has a factor {}'.format(y,x))
#          break
#     x = x -1
# else:
#     print('{} is prime'.format(y))

# y = 31
# x = y 
# while x > 1:
#     if y % x == 0:
#         print('{} has a factor {}'.format(y,x))
#         break
#     x = x - 1
# else:
#     print('{} is prime'.format(y))

# y = 33
# x = y //2
# while x > 1:
#     if y % x  == 0:
#         print('{} has a factor {}'.format(y,x))
#         break
#     x = x - 1
# else:
#     print('{} is prime'.format(y))