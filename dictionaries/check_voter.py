'''
Write a function to check whether voters have voted, return true, else false add to dictionary, print - can vote

Pseudocode
__________
1. Create function check_voter(name):
2. Create dictionary
3. Check if voter exists in dictionary return true, else return voters
'''

def check_voter(name):
    voters = {}
    if voters.get(name): return True
    else:
        voters[name] = True 
        print("Can vote!")
        return voters

result = check_voter("Sam")
print(result)

'''
Time complexity = O(1)
Space complexity = O(n)
'''