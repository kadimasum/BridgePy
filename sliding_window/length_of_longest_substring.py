'''
given a string s, find the length of the longest substring
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''



def length_of_the_longest_substring(s):
    if len(s) == 0: return 0
    map = {}
    max_length = start = 0
    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
        else: max_length = max(max_length, i - start + 1)
        map[s[i]] = i

    return max_length

result = length_of_the_longest_substring("abcabcbb")
print(result)