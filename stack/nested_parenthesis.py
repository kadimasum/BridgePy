'''
PROBLEM You are given a string that contains left and right parenthesis char-
acters. Write code to determine whether the parentheses are correctly nested. For
example, the strings "(())" and "()()" are correctly nested but "(()()" and ")
(" are not.
'''
def has_nested(s):
    my_stack = []
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i] == "(":
            my_stack.append(list_s[i])
        elif list_s[i] == ")" and len(my_stack) > 0:
            my_stack.pop()
        else: return False

    return len(my_stack) == 0

result = has_nested("(())()")
print(result)

'''
Time complexity = O(n)
Space complexity = O(n)
'''