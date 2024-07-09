graph = {}
graph['you'] = ['bob', 'claire', 'yaa']
graph['bob'] = ['anuj','peggy']
graph['yaa'] = ['peggy']
graph['claire']=['Thom','Johnny']
graph['anuj'] = []
graph['Thom'] = []
graph['Johnny'] = []
graph['peggy'] = []
# print(graph)

def person_is_seller(name):
    return name[-1] == ['a']

from collections import deque
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
    if not person in searched:
        if person_is_seller(person):
            print (person + " is a mango seller!")
        return True
    else:
        search_queue += graph[person]
        searched.append(person)
    return False

print(search('you'))