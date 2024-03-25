import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

class Node():
    def __init__(self, key):
        self.key = key
        self.children = {}
    
class Tries():
    def __init__(self):
        self.head = Node(None)

    def insert(self, path):
        now = self.head
        directories = path.split("\\")

        for directory in directories:
            if directory not in now.children:
                now.children[directory] = Node(directory)

            now = now.children[directory]

    def dfs(self, now : Node, depth):
        if now.key is not None:
            for _ in range(depth):
                print(" ", end="")
            print(now.key)

        now_children = list(now.children.keys())
        now_children.sort()

        for child in now_children:
            self.dfs(now.children[child], depth+1)

    def display_all(self):
        now = self.head
        self.dfs(now, -1)

tries = Tries()

for _ in range(N):
    path = input()
    tries.insert(path)

tries.display_all()