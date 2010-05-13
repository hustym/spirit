#-*- coding:utf-8 -*-

# [1,2,3,4,5] = 'aaa'

# map = { 1 : { 2 : {3 : { 4 : { 5 : 'aaa'}}}} }


def add( map, words, target):
#    print "_add:", map, words, target
    if words[0] in map:
        if len(words) > 1:
            map[ words[0] ].update( add( map[words[0]], words[1:], target ) )
        else:
            print "duplicated key. ", words, target
            map[ words[0] ] = target
    else:
        if len(words) > 1:
            map[ words[0] ] = add( {}, words[1:], target )
        else:
            map[ words[0] ] = target
    return map    

def search(words, map):
    if len(words) == 0 :
        return None
    
    if words[0] not in map:
        return None
    
    if len(words) == 1:
        if type(map[words[0]]) == dict:
            return None
        return map[words[0]]
    else:
        return search( words[1:], map[ words[0] ] )

def trans_gbk( string):
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
                
def trans_utf8(string):
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

    
if __name__ == "__main__":
    a= '中国 人们 大家', 1
    print a
    print trans_utf8('中国 人们 大家'.decode('gbk').encode('utf8'))
#    map = {}
#    words = [[1, 2, 3, 4, 5], [1, 2, 4], [2, 3, 4], [3, 4, 5] ]
#    targets = ["12345", "124", "234", "345"]
#    for i in xrange( len(words) ):
#        map = add( map, words[i], targets[i] )
#
#    for i in xrange( len(words) ):
#        print search( words[i], map )
#    print search( [1,2,3], map )    