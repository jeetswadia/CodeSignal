'''
Given an array of strings, return another array containing all of its longest strings.
____________________________________________________________________
                            EXAMPLE
--------------------------------------------------------------------
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"]
'''
def solution(inputArray):
    import numpy as np 
    
    arr = np.array(inputArray)
    
    sorted_arr = np.array(sorted(arr,key=len))
    
    ref = len(sorted_arr[-1])
    
    ans=0
    
    for ch in sorted_arr:
        if len(ch)==ref:
            ans+=1
    
    output = sorted_arr[-ans:]
    
    result = output.tolist()
    
    return result