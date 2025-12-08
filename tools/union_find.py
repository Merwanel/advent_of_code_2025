from collections import Counter

class UnionFind:
    def __init__(self, sz:int) :
        self.root = list(range(sz))
        self.rank = [1] * sz
        self.nb_component = sz

    def find(self, x) :
        if self.root[x] != x :
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y) :
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty : return
        self.nb_component -= 1
        if self.rank[rootx] > self.rank[rooty] : 
            self.root[rooty] = rootx
            self.rank[rootx] += 1
        else : # self.rank[rootx] <= self.rank[rooty]
            self.root[rootx] = rooty
            self.rank[rooty] += 1

    def isConnected(self, x, y) :
        return self.find(x) == self.find(y)

    def updateRoots(self) :
        for x in range(len(self.root)) :
            self.find(x)

    def get_componnent_size(self) :
        self.updateRoots()
        return Counter(self.root)

    def get_nb_componnents(self) :
        self.updateRoots()
        return self.nb_component