'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving 
the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''

def solution(a):
    b = []
    
    #get all the index where a[i]=-1
    tree_index=[]
    for i in range(len(a)):
        if a[i]==-1:
            tree_index.append(i)
    
    
    for j in range(len(a)):
        if a[j]!=-1:
            b.append(a[j])
        
    b.sort()
    
    for k in tree_index:
        b.insert(k,-1)
    
    return b