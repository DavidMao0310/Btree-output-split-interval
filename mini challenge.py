import pandas as pd
import numpy as np
np.random.seed(0)
dataset = np.random.normal(50, 10, 100)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.list = [self.root_node()]
        self.container = []

    def root_node(self):
        root_node = Node(dataset)
        return root_node

    def split_left_node(self, l):
        self.l=l
        d = (max(l) - min(l)) / 2
        j = 0
        m = []

        for i in dataset:
            if i in l:
                j = j + 1

        for k in l:
            if k < min(l) + d:
                m.append(k)

        return m

    def split_right_node(self, l):
        self.l=l
        d = (max(l) - min(l)) / 2
        j = 0
        m = []

        for i in dataset:
            if i in l:
                j = j + 1

        for k in l:
            if k >= max(l) - d:
                m.append(k)

        return m

    def split(self, d):
        self.d=d
        s = []
        for i in d:
            if i.data is None:
                pass
            elif len(i.data) > 5:
                s.extend([Node(self.split_left_node(i.data)), Node(self.split_right_node(i.data))])
            else:
                pass
        return s

    def maketree(self, d):
        self.d=d
        self.container += d
        if len(d) == 0:
            return "end"
        else:
            return self.maketree(self.split(d))


if __name__ == '__main__':
    tree = Tree()
    tree.maketree(tree.list)
    df = pd.DataFrame(columns=('Node number', 'min value', 'max value', 'number of points'))
    for i in tree.container:
        a = tree.container.index(i)+1
        b = max(i.data)
        c = min(i.data)
        d = len(i.data)
        df = df.append(pd.DataFrame({'Node number': [a], 'min value': [b], 'max value': [c], 'number of points': [d]}))
    df = df.set_index('Node number')
    df.to_excel('/Users/apple/Desktop/PyCharm Project/draft 1/btree output.xlsx')
    print(df)
    print("Done")































