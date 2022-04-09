import heapq
from collections import Counter


class Node:

    def __init__(self, left=None, right=None):
        if left:
            self.left_child = left
        if right:
            self.right_child = right

    def look_tree(self, code=""):
        if self.left_child:
            if not isinstance(self.left_child, str):
                self.left_child.look_tree(code+"0")
            else:
                num[self.left_child] = code+"0"
        if self.right_child:
            if not isinstance(self.right_child, str):
                self.right_child.look_tree(code+"1")
            else:
                num[self.right_child] = code+"1"


word = input()
char_frequency = Counter(word)
if len(char_frequency) == 1:
    print(1, len(word))
    print(f"{word[0]}: 0")
    print("0"*len(word))
else:
    mas = [tuple([j, i]) for i, j in char_frequency.items()]
    num = {}
    nodes = {}
    heapq.heapify(mas)
    current_node = None

    while len(mas) != 1:
        elem1 = heapq.heappop(mas)
        elem2 = heapq.heappop(mas)
        heapq.heappush(mas, (elem1[0] + elem2[0], elem1[1] + elem2[1]))
        current_node = Node(nodes.get(elem1[1], elem1[1]), nodes.get(elem2[1], elem2[1]))
        nodes[elem1[1] + elem2[1]] = current_node

    current_node.look_tree()
    string = ""
    for i in word:
        string += num[i]
    print(len(char_frequency), len(string))
    for i in num:
        print(f"{i}: {num[i]}")
    print(string)