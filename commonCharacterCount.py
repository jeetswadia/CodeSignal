'''
Given two strings, find the number of common characters between them.
____________________________________________________________________
                            EXAMPLE
--------------------------------------------------------------------
For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''

def solution(s1, s2):
    
    if (s1 in s2) or (s2 in s1):
        return min(len(s1), len(s2))
        
    from collections import Counter
    
    a = dict(Counter(s1))
    b = dict(Counter(s2))
    ans =0
    ans = 0

    for keys in a.keys():
        if keys in b.keys():
            ans += min(a[keys], b[keys])
            
    
    return ans