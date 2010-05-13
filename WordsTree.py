#-*- coding:utf-8 -*-

from TernaryTree import TernaryTree

class WordsTree:
    def __init__(self):
        self.words_map = {}
        
    def add(self, word, target):
        if word[0] not in self.words_map:
            self.words_map[word[0]] = TernaryTree()
        self.words_map[word[0]].add(word, target)
        
    def dump(self):
        print self.words_map
       
    def search(self, word):
        if word[0] in self.words_map:
            return self.words_map[word[0]].search(word)
        return 0, 'not found'
    
    def has_head(self, char):
        return char in self.words_map
        


key_map = {}
max_id = 1

        
if __name__ == '__main__':
    def gen_key(word):
        if word not in key_map:
            global max_id, key_map
            key_map[word] = max_id
            max_id += 1

        return key_map[word]

    words = 'chinese chip as again chain cheap bus bee beat'.split()
    tree = WordsTree()
    for word in words:
        tree.add(word, gen_key(word) )
    for word in words:
        print tree.search(word)
    print tree.search('cccc')            
