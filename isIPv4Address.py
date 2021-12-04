'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) 
participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. 
One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
'''

def solution(inputString):
    num = inputString.split('.')
    
    if len(num)!=4:
        return False
    if '' in num:
        return False
    for i in range(4):
        if num[i].isdecimal():
            if int(num[i]) > 255:
                return False
            elif num[i].startswith('0') and len(num[i])>1:
                return False
        else:
            return False
    
    return True