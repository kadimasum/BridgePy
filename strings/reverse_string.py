'''
Reverse string in place

PSEUDOCODE
-----------
1. Create a function reverseStr(string)
2. Check if len(string) < 2 return string
3. Loop through string
4. Store  character at length - 1 in temp variable
5. Swap  character at length -1 with current character
6. decrement the length of the string
'''


def reverseStr(string):
    if len(string) < 2: return string
    i = 0
    n = len(string) - 1

    myList = list(string)

    while(i < n):
        temp = myList[n]
        myList[n] = myList[i]
        myList[i] = temp
        i += 1
        n -= 1
    
    return ''.join(myList)

result = reverseStr("Welcome")
print(result)

'''
* Time complexity = O(n)
* Space complexity = O(n)

'''
