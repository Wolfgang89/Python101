
from collections import deque

# 图 中 反映映射关系 使用散列表
#  python 中的缩进必须要严格注意


graph = {}
graph ["you"] = ["alice","bob","claire"]
graph ["bob"] = ["anuj","peggy"]
graph ["claire"]= ["thom","jhon"]
graph ["alice"] = ["peggym","mary","man"]
graph ["thom"] = []
graph ["peggy"] = []
graph ["jhon"] = []
graph ["anuj"] = []
graph ["alim"] = []

# graph = {}
# graph["you"] = ["alice", "bob", "claire"]
# graph["bob"] = ["anuj", "peggy"]
# graph["alice"] = ["peggy"]
# graph["claire"] = ["thom", "jonny"]
# graph["anuj"] = []
# graph["peggy"] = []
# graph["thom"] = []
# graph["jonny"] = []

# search_queue +=  graph['you']

def  person_is_seller(name):
    return name[-1] == 'm'

# def search(name):
#     search_queue = deque() 
#     search_queue += graph[name] 
#     searched = []
#     while search_queue:
#         person = search_queue.popleft() 
#         if person not in searched:
#             if person_is_seller(person):
#                 print (person + " is a mango seller!") 
#                 return True
#             else:
#                 search_queue += graph[person] 
#                 searched.append(person)
#     return False


def search(name):
    search_queue = deque()
    search_queue +=  graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("芒果经销商找到")
                print (person + " is a mango seller!") 
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False        

if __name__ == "__main__":
    search('you')


# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print('芒果经销商找到了')
#         return True
#     else:
#         search_queue += graph[person]
# return False
