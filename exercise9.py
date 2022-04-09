class Heap:

    def __init__(self):
        self.heap = []
        self.op = []

    def insert(self, element: int):
        self.heap.append(element)
        self.sift_up(len(self.heap)-1)

    def extract_max(self):
        if len(self.heap) != 1:
            self.op.append(self.heap[0])
            self.heap[0] = self.heap.pop()
            self.sift_down(0)
        else:
            self.op.append(self.heap.pop())

    def sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def sift_down(self, i):
        max_index = i
        size = len(self.heap)
        if self.left_child(i) <= size - 1 and self.heap[self.left_child(i)] > self.heap[max_index]:
            max_index = self.left_child(i)
        if self.right_child(i) <= size - 1 and self.heap[self.right_child(i)] > self.heap[max_index]:
            max_index = self.right_child(i)
        if max_index != i:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self.sift_down(max_index)

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2


heap = Heap()

d = {
    "Insert": heap.insert,
    "ExtractMax": heap.extract_max,
}

for i in range(int(input())):
    operation = [i for i in input().split()]
    if len(operation) == 2:
        d["Insert"](int(operation[1]))
    else:
        d["ExtractMax"]()

print(*heap.op, sep="\n")
