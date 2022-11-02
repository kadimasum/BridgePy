'''
PROBLEM You are given a string that contains left and right parenthesis char-
acters. Write code to determine whether the parentheses are correctly nested. For
example, the strings "(())" and "()()" are correctly nested but "(()()" and ")
(" are not.
'''

def check_nesting(s):
    if len(s) % 2 != 0: return False
    counter = 0
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i] == "(":
            counter += 1
        elif list_s[i] == ")":
            counter -= 1
            if counter < 0: return False
    return counter == 0

result = check_nesting("((()))")
print(result)

'''
Time complexity = O(n)
Space complexity = O(n)
'''