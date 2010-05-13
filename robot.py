# -*- coding:utf-8 -*-

from WordsTree import WordsTree
from SyntaxTree import SyntaxTree

class Robot:
    def __init__(self):
        self.map = {}
        self.word_tree = WordsTree()
        self.syntax_tree = SyntaxTree()
        self.mistake_map = {}
    
    def trans_gbk(self, string):
        list = []
        high= 0
        for s in string:
            if high != 0:
                list.append( (high << 8) + ord(s) )
                high = 0
            else:
                if ord(s) > 0x80:
                    high = ord(s)
                else:
                    list.append( ord(s) )
        if high:
            print "trans_gbk ERROR. omit"
        return list
        
 #   def pre_process(self, words):
        
        
    def trans_utf8(self, string):
        list = []
        high = 0
        for s in string:
            if ord(s) < 0x80:
                if high:
                    list.append( high )
                    high = 0
                list.append( ord(s) )
            else:
                if ord(s) & 0x40:
                    if high:
                        list.append( high )
                    high = ord(s)
                else: 
                    high = (high << 8) + ord(s)
        if high:
            list.append( high )
        return list
        
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
                    self.add_question(a, l)
                    a = None

    def walk(self, dir):
        import os
        for root, dirs, files in os.walk(dir):
            for filename in files:
                self.from_file( os.path.join(root, filename) ) 
        
    def add_question(self, quest, answer):
        self.map[quest] = answer
        
    def analyse(self):
        list = []
        for word in self.map:
            list += word.split()
        list = set(list)
        for item in list:
  #          print "add_item", item
            self.word_tree.add( self.trans_gbk(item), True )
        
        for key, value in self.map.items():
  #          print "begin to insert to syntax tree:", key.split(), '---', value
            self.syntax_tree.add( map(tuple, map(self.trans_gbk, key.split() ) ), value)
            
    def ask(self, quest):
        words = self.split_word(quest)
 #       print words
        return self.syntax_tree.search( map(tuple, words) )
    #    print self.syntax_tree.syntax_map

    def split_word(self, quest):
        sentence = self.trans_gbk(quest)
        words = []
        pos_start = 0
        pos_end = pos_start + 1
        length = len( sentence )
    #    print sentence
        while pos_start <  length:
            word = None
            pos_end = pos_start + 1
    #        print "reset pos-end", pos_start, pos_end
            pos, target = self.word_tree.search(sentence[ pos_start : pos_end ])
            if pos > 0:
     #           print "found start:", sentence[ pos_start : pos_end ], pos
                if target:
                    word = sentence[pos_start : pos_end]
      #              print "found match.", word
                for i in xrange( pos_end + 1, len( sentence ) + 1, 1 ):
       #             print "begin to search:", i, len(sentence), sentence[ pos_start : i ]
                    _pos, _target = self.word_tree.search( sentence[ pos_start : i ]  )
                    if _pos > pos:
        #                print "re-found start:", sentence[ pos_start : i ], _pos
                        pos = _pos
                        if _target:
                            word = sentence[pos_start : i]
                            pos_end = i
         #                   print "re-found match.", word
                    else:
          #              print "break"
                        break
                if word:
                    pos_start = pos_end
           #         print "reset start", pos_start
                    words.append( word )
                else:
                    pos_start += 1
                 
            else:
            #    print "restart.", pos_start
                pos_start += 1
        return words
        
if __name__ == "__main__":
    r = Robot()
    r.add_question('中国 国家', '中国是一个美丽的国家')       
    r.add_question('你 谁', '我是可爱的小精灵')
    r.add_question('你 好', '你好啊，欢迎你')
    r.walk('robot_lib')
    r.analyse()
    print r.ask('你是谁啊')
    print r.ask('中国是一个什么样的国家')
    print r.ask('你你谁好啊')

    import time
    word = raw_input("请输入语句(exit 退出):")
    while word != 'exit':
        result = r.ask(word)            
        print result
        word = raw_input("请输入语句(exit 退出):")

    
        