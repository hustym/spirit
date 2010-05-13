#-*- coding:utf-8 -*-

#from WordsTree import WordsTree
#from TernaryTree import TernaryTree
#
#class SyntaxTree:
#    def __init__(self):
#        self.key_map = {}
#        self.max_id = 1
#        self.syntax_map = {}
#        
#    def gen_key(self, word):
#        if word not in self.key_map:
#    #        print "insert word:", word, self.max_id
#            self.key_map[word] = self.max_id
#            self.max_id += 1
#    #    print word, self.key_map[word]
#    #    print "get word:", word, self.key_map[word]
#        return self.key_map[word]
#
#    def add(self, words, target):
#        list = []
#        for word in words:
#            list.append( self.gen_key( word ) )
#
#        if list[0] not in self.syntax_map:
#            self.syntax_map[ list[0] ] = TernaryTree()
#
#        self.syntax_map[list[0]].add(list, target)
#        
#    def search(self, words):
#        def combination(pre, words):
#            if len(words) >= 1:
#                if pre == []:
#                    pre.append( [] )
#                    pre.append( [words[0]] )
#                else:
#                    list = pre[:]
#                    for item in list:
#                        pre.append( item + [words[0], ] )
#            if len(words) > 1:
#                return combination(pre, words[1:])
#            else:
#                return pre
#
#        list = []
#        for word in words:
#            list.append( self.gen_key( word ) )
#
#        com = combination([], words)
#
#    #    print list
#        if list[0] not in self.syntax_map:
#            return 0, None
#        
#        pos, target = self.syntax_map[list[0]].search(list)
#        
#        pos_start = 0
#        pos_end = 1
#        while pos_start < len(list):
#            pos_end = pos_start + 1
#            words = list[pos_start : ]
#            if words[0] not in self.syntax_map:
#                pos_start += 1
#                continue
#            pos, target = self.syntax_map[words[0]].search(words)
#            print pos, target, words
#            if target:
#                answer = target
#                length = len(words)
#            left_words = len(words)
#            while left_words > 0:
#                words.pop(pos - 1)
#                if len(words) <= 0:
#                    break
#                _pos, _target = self.syntax_map[words[0]].search(words)
#                print _pos, _target, words
#                if _target:
#                    if len(words) > length:
#                        answer = _target
#                if _pos > pos:
#                    pos
#                    
#        print pos, target
#        return pos, target
                
#if __name__ == '__main__':
    
    
    

#    words = {
#        'steven yang'  : 'myname',
#        'chinese chip' : 'obus',
#        'chinese again': 'tang',
#        'bus bee beat' : 'a b c d',           
#    }
#
# #   words = 'steven chinese chip yang as again chain cheap bus bee beat'.split()
#    tree = SyntaxTree()
#    for word in words:
#        list = word.split()
#        tree.add(list, words[word] )
#    for word in words:
#        list = word.split()
#        print  "%s -- %r " % ( word, tree.search(list) )
##    print tree.search('cccc')       


class SyntaxTree:
    def __init__(self):
  #      self.key_map = {}
  #      self.max_id = 1
        self.syntax_map = {}
        self.cnt = 0
        
    def add(self, words, target):
        self.cnt += 1
  #      print "add:", words, target

        def _add( map, words, target):
  #          print "_add:", map, words, target
            if words[0] in map:
                if len(words) > 1:
                    if type(map[ words[0] ]) != dict:
       #                 print "duplicated key. ", " ".join(words)
                        map[ words[0] ] = target
                    else:
                        map[ words[0] ].update( _add( map[words[0]], words[1:], target ) )
                else:
       #             print "duplicated key. ", words, target
                    map[ words[0] ] = target
            else:
                if len(words) > 1:
                    map[ words[0] ] = _add( {}, words[1:], target )
                else:
                    map[ words[0] ] = target
            return map    

        self.syntax_map = _add( self.syntax_map, words, target )


    def search(self, words):
        def _combination(pre, words):
            if len(words) >= 1:
                if pre == []:
                    pre.append( [] )
                    pre.append( [words[0]] )
                else:
                    list = pre[:]
                    for item in list:
                        pre.append( item + [words[0], ] )
            if len(words) > 1:
                return _combination(pre, words[1:])
            else:
                return pre
        
        def _search( words, map ):
            if len(words) == 0 :
                return None
            
            if words[0] not in map:
                return None
            
            if len(words) == 1:
                if type(map[words[0]]) == dict:
                    return None
                return map[words[0]]
            else:
                if type(map[words[0]]) != dict:
                    return None
                return _search( words[1:], map[ words[0] ] )

 #       print words                
        com = _combination([], words)
 #       print com
        list = []
        for item in com:
            target = _search( item, self.syntax_map )
            if target:
                list.append( ( item, target ) )

        if len(list) == 0:
            return None
        else:
            max = 0
            answer = None
            for item in list:
                if len( item[0] ) > max:
                    answer = item
                    
    #        print answer
            return answer[1]
    
    def from_file(self, filename):
        lines=file(filename, 'r').read().split('\n')     
        a = None
        for l in lines:
            l = l.strip()
            if len(l) == 0:
                continue
            if l[0] == '[' and l[-1] == ']':
                a=l[1:-1]
            else:
                if a is None:
                    print "Error:", l
                else:
                    self.add(a.split(), l)
                    a = None

    def walk(self, dir):
        import os
        for root, dirs, files in os.walk(dir):
            for filename in files:
                self.from_file( os.path.join(root, filename) ) 
           
    def dump(self):
        pass 

t = None

import random

def init():
    
    def random_words():
        l = random.randint(1, 6)
        range = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        list = []
        for i in xrange(l):
            a = ""
            for k in xrange(5):
                a += random.choice(range)
            list.append(a)
            
        return list
        
    global t
    t = SyntaxTree()
    for i in xrange(500000):
        t.add( random_words(), 'abc' )
  #  t.walk('robot_lib')
    
        
import time

if __name__ == "__main__":
    init()
    print t.cnt
  #  print t.syntax_map
    word = raw_input("«Î ‰»Î”Ôæ‰(exit ÕÀ≥ˆ):")
    while word != 'exit':
        t1 = time.time()
        for i in xrange(50000):
            result = t.search(word.split())            
        t2 = time.time()
        print t2 - t1
        print result
        word = raw_input("«Î ‰»Î”Ôæ‰(exit ÕÀ≥ˆ):")
                 