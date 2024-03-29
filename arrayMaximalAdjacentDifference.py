'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
'''

def solution(inputArray):
    
    max_diff = 0
    for i in range(1,len(inputArray)):
        diff = abs(inputArray[i] - inputArray[i-1])
        if diff>max_diff:
            max_diff = diff
    return max_diff
