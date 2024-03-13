import sys

def input(): return sys.stdin.readline()

class Node():
    def __init__(self, key):
        self.key = key
        self.children = {} # 딕셔너리 선언

class Tries():
    def __init__(self):
        self.head = Node(None)

    def insert(self, informations):
        cur_node = self.head
        
        for info in informations:
            # 만약 자식 노드들 중에서 char가 없을 경우 새로운 노드를 만듬
            if info not in cur_node.children:
                cur_node.children[info] = Node(info)

            cur_node = cur_node.children[info]

    def search_all(self):
        cur_node = self.head
        stack = [[cur_node, 0]]
            
        while stack:
            cur_node, depth = stack.pop()

            if cur_node.key != None:
                if depth == 1: print(cur_node.key)
                else:
                    for _ in range((depth-1)*2): print("-", end="")
                    print(cur_node.key)
            
            for key in sorted(list(cur_node.children.keys()), reverse = True):
                stack.append([cur_node.children[key], depth+1])

        
N = int(input())
tries = Tries()

for _ in range(N):
    info = input().split()[1:]
    tries.insert(info)
    
tries.search_all()