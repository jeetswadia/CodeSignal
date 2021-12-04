'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

picture = ["abc","ded"]

the output should be
solution(picture) = ["*****",
                    "*abc*",
                    "*ded*",
                    "*****"]
'''

def solution(picture):
    n = len(picture)
    n_element = len(picture[0])

    layer = (n_element+2)*'*'

    final_print = [layer]
    
    for i in range(n):
        picture[i]= '*'+picture[i]+'*'
        
    for element in picture:
       final_print.append(element)
    
    final_print.append(layer)    
    return final_print