import sys
from collections import defaultdict

class Node():
    def __init__(self, key = None):
        self.key = key
        self.count = 0
        self.children = {}

class Tries():
    def __init__(self):
        self.head = Node(None)

    def add(self, element):
        now = self.head

        for char in element:
            if char not in now.children:
                now.children[char] = Node(char)

            now = now.children[char]
            now.count += 1

    def delete(self, element):
        now = self.head
        
        for char in element:
            child = now.children[char]
            child.count -= 1
            if child.count == 0: del now.children[char]
            now = child

    def find(self, element):
        now = self.head
        dic = defaultdict(int)

        string = ""
        for char in element:
            if char not in now.children: return dic
            
            string = string + char
            now = now.children[char]
            dic[string] = now.count

        return dic

def input(): return sys.stdin.readline().rstrip()

def query(method, target, element):
    if method == "add": target.add(element)

    if method == "delete": target.delete(element)

    if method == "find":
        n = len(element)
        a_result = A.find(element)
        b_result = B.find(element[::-1])
        
        answer = 0
        for a_len in range(1,n):
            answer += a_result[element[:a_len]] * b_result[element[:a_len-1:-1]]
            
        print(answer)

N = int(input())
A = Tries()
B = Tries()
method, target, element = "", "", ""

for _ in range(N):
    _input = input()
    if _input[:4] == "find": 
        method,element = _input.split()
        query(method, A, element)
        
    else:
        method, target, element = _input.split()
        
        if target == "A": query(method, A, element)
        else: query(method, B, element[::-1])