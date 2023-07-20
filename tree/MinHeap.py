# Completed Binary Tree
import heapq
from math import inf


class MinHeap:
    def __init__(self):
        self.tree = [-inf]
        self.size = 0

    def isLeaf(self, idx):
        return idx > self.size / 2

    def leftChild(self, idx):
        return 2 * idx

    def rightChild(self, idx):
        return 2 * idx + 1

    def parent(self, idx):
        return idx // 2

    def swap(self, a, b):
        self.tree[a], self.tree[b] = self.tree[b], self.tree[a]

    def heapfy(self, idx):
        if self.isLeaf(idx):
            return
        # if have right child
        left = self.leftChild(idx)
        swap = left
        if self.rightChild(idx) < self.size:
            right = self.rightChild(idx)
            if self.tree[left] >= self.tree[right]:
                swap = right
        if self.tree[swap] < self.tree[idx]:
            self.swap(swap, idx)
            self.heapfy(swap)

        pass

    def pop(self):
        self.swap(1, self.size)
        self.size -= 1
        self.tree.pop()
        self.heapfy(1)

    def push(self, val):
        self.size += 1
        idx = self.size
        self.tree.append(val)
        while idx > 0:
            p = self.parent(idx)
            if self.tree[p] > self.tree[idx]:
                self.swap(idx, p)
                idx = p
            else:
                break

    def getMin(self):
        return self.tree[1]

    def __len__(self):
        return self.size


if __name__ == '__main__':
    h = MinHeap()
    h.push(2)
    h.push(4)
    h.push(1)
    h.push(9)
    h.push(8)
    while h:
        print("----------")
        print(h.getMin())
        h.pop()
