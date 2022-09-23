'''
A palindrome is a word that is pronounced the same both way
Create a function that determines whether a word is a palindrome
Return true else return false

PSEUDOCODE
------------
1. Create a function isPalindrome(word)
2. Check if len(word) < 2 return true
3. Reverse string
4. Return reversed string == word

'''

def isPalindrome(word):
    if len(word) < 2: return True

    charList = list(word)
    i = 0
    n = len(charList) - 1

    while i < n:
        temp = charList[n]
        charList[n] = charList[i]
        charList[i] = temp
        i += 1
        n -= 1
    
    reverseWord = ''.join(charList)

    return word.lower() == reverseWord.lower()

result = isPalindrome("yOY")
print(result)

'''
* Time complexity = O(n)
* Space complexity = O(n)
'''