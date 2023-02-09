

def is_valid(s):
    if len(s) % 2 != 0: return False
    stack = []
    parenthesis_map = { '{':'}', '(':')', '[':']' }
    for char in s:
        if char in parenthesis_map:
            stack.append(parenthesis_map[char])
        elif not stack or stack[-1] != char:
            return False
        else: stack.pop()

    return len(stack) == 0

print(is_valid('[(}]'))