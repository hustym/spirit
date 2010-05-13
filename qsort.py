#-*- coding:utf-8 -*-

from random import randrange, randint       

def qsortlist(list):
    def qsort(list):
        if list == []: 
            return []
        else:
            pivot = list.pop(randrange(len(list)))
            lesser = qsort([l for l in list if l < pivot])
            greater = qsort([l for l in list if l >= pivot])
            return lesser + [pivot] + greater
    return qsort(list[:])

def search(list, find):  
    low = 0   
    high = len(list)  
    if find > list[-1] or find < list[0]:
        return None
    while(low < high):  
        mid = (low + high)/2  
        if(list[mid]==find):
            return mid
        else:  
            if(list[mid] > find):  
                low = mid + 1  
            else:  
                high = mid - 1  
    return None   

if __name__ == "__main__":
    list = []
    for i in xrange(1000000):
        list.append( randint(1, 99999999) )
        
    print list[0:20]
    find = list[0]
    import time
    t1 = time.time()
    list2 = qsortlist(list)
    t2 = time.time()
    print list2[0:20]
    print t2 - t1
    t3 = time.time()
    search(list2, find)
    t4 = time.time()
    print t4 - t3
    