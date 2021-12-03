'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
'''

def solution(n):
    #the hypothesis is the total number of digits are even. 
    
    string = str(n)
    
    length = len(string)
    l = int(length/2)
    
    first_half = string[:l]
    second_half = string[l:]
    
    def sumfunc(s):
        ans =0
        for char in s:
            ans += int(char)
        return ans
        
    return sumfunc(first_half)==sumfunc(second_half)