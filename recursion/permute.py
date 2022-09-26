'''
Permutation is finding all possible results of a value
permutation of "ABC"

CBA
BCA
CAB
ACB
BAC
ABC


'''

def permute(string, pocket=""):
    if len(string)  == 0: print(pocket) 
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

print(permute("ABC", ""))

'''
* Time complexity = O(n)
* Space complexity = O(n)
'''