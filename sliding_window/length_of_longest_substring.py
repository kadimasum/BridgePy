'''
given a string s, find the length of the longest substring
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''



# def length_of_the_longest_substring(s):
#     if len(s) == 0: return 0
#     map = {}
#     max_length = start = 0
#     for i in range(len(s)):
#         if s[i] in map and start <= map[s[i]]:
#             start = map[s[i]] + 1
#         else: max_length = max(max_length, i - start + 1)
#         map[s[i]] = i

#     return max_length

# result = length_of_the_longest_substring("abcabcbb")
# print(result)

'''
'abcbc'
"pwwkew"

Time Complexity = O(n)
Space complexity = O(n)

'''
def longest_substring(s: str):
    longest = 0
    charset = set()
    a_pointer = 0
    b_pointer = 0
    while b_pointer < len(s):
        if s[b_pointer] not in charset:
            charset.add(s[b_pointer])
            b_pointer += 1
            longest = max(len(charset), longest)
        else:
            charset.remove(s[a_pointer])
            a_pointer += 1
    return longest

result = longest_substring("pwwkew"
)
print(result)