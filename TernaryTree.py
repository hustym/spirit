#-*- coding:utf-8 -*-

class Node:
    def __init__(self, text, target):
        self.text = text
        self.left, self.center, self.right = None, None, None
        self.target = target

class TernaryTree:
    def __init__(self):
        self.root = None
    
    def add_node(self, string, pos, node, target):
    #   print "add_node ",string[pos] 
        if string[pos] < node.text:
    #       print "add node to left"
            if node.left is None:
                node.left = Node(string[pos], None)
            self.add_node(string, pos, node.left, target)
        elif string[pos] > node.text:
    #       print "add node to right"
            if node.right is None:
                node.right = Node(string[pos], None)
            self.add_node(string, pos, node.right, target)
        else:
            if pos + 1 == len(string):
    #           print "set node end"
                node.target = target
            else:
    #           print "add node to center"
                if node.center is None:
                    node.center = Node(string[pos], None)
                self.add_node(string, pos + 1, node.center, target)
                
    def add(self, string, target):
        if string is None or string == "":
            return
        if self.root is None:
            self.root = Node(string[0], None)
        self.add_node(string, 0, self.root, target)
        
    def search(self, string):
        if string is None or string == "":
            return 0, None
        
        pos = 0
        node = self.root
        while node != None:
            if string[pos] < node.text:
                node = node.left
            elif string[pos] > node.text:
                node = node.right
            else:
                pos += 1
                if pos == len(string):
                    return pos, node.target
                node = node.center

        return pos, None
    
t = None    

def main():
    import time
    from random import randint
    global t
    t = TernaryTree()
    t1 = time.time()
    for i in xrange(1000000):
        t.add( [randint(1, 99999999), ], True )
    t2 = time.time()
    print t2 - t1
    
    t3 = time.time()
    t.search( [randint(1, 99999999), ] )
    t4 = time.time()
    print t4 - t3
   
        
if __name__ == "__main__":
    main()
    