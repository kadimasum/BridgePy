'''
Write a function Solution that, given a string S of length N, returns any palindrome which can be obtained by replacing all the question marks in S by lowercase letters(a - z). If no palindrome can be obtained, the function should return the string "NO".

A palindrome is a string that reads the same both forward and backwards

Examples:
---------
1. Given S = "?ab??a" return "aabbaa"
2. Given S = "bab??a" return "NO"
3. Given S = "?a?" return "aaa" or "zaz" etc.
''' 

def isPossiblePalindrome(S):

    n = len(S)

    for i in range(n // 2):
        if S[i] != '?' and S[n - i - 1] != '?' and S[i] != S[n - i - 1]:
            return "NO"
        
    list_S = list(S)

    for i in range(n):
        if (list_S[i] == '?'):
            if (list_S[n - i - 1] != '?'):
                list_S[i] = list_S[n - i - 1]
            else:
                list_S[i] = list_S[n - i - 1] = 'a'
 

    return "".join(list_S)


result = isPossiblePalindrome("?k?" )
print(result)