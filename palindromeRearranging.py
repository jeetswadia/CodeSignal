'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''

def solution(inputString):
    string = list(inputString)
    
    n = len(string)
    s_set= set(string)
    
    from collections import Counter
    
    dic = Counter(string)
    
    k =0 
    
    for char in s_set:
        if dic.get(char)%2!=0:
            k+=1
    
    if k>1:
        return False
    else:
        return True