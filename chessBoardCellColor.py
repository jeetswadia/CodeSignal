'''
Given two cells on the standard chess board, 
determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.
'''

def solution(cell1, cell2):
    ans1= ''
    ans2= ''
    if cell1[0] in 'ACEG':
        if cell1[1] in '1357':
            ans1 += 'Black'
        else:
            ans1 += 'White'
    elif cell1[0] in 'BDFH':
        if cell1[1] in '2468':
            ans1 += 'Black'
        else:
            ans1 += 'White'
            
    if cell2[0] in 'ACEG':
        if cell2[1] in '1357':
            ans2 += 'Black'
        else:
            ans2 += 'White'
    elif cell2[0] in 'BDFH':
        if cell2[1] in '2468':
            ans2 += 'Black'
        else:
            ans2 += 'White'
            
    return ans1==ans2