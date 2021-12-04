'''
Two arrays are called similar if one can be obtained from another 
by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
'''



def solution(a, b):
    
    if sorted(a) != sorted(b):
        return False
    elif a==b:
        return True
    else:
        i=0
        while i<len(a):
            if a[i]==b[i]:
                a.pop(i)
                b.pop(i)
            else:
                i += 1
        
        if len(a)!=2:
            return False
        b.reverse()
        
        if a==b:
            return True
        else:
            return False