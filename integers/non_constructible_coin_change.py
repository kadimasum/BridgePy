'''
# Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. 
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

 # For example if you're given coins = [1, 2, 5] then the minimum amount of change that you can't create is 4. 
If you're given no coins, the minimum amount of change that you can't create is 1.

 Sample Input 

coins = [5,  7,  1, 1,  2,  3,  22] 

Sample Output 

 20 
[0,1,2,3,4,5]
[1,2,3,4,5,6]
'''

def nonConstructibleChange(coins):

    if len(coins) == 0: return 1

    coins.sort()

    minimum_amount_of_change = 0 

    for coin in coins:
        if coin > minimum_amount_of_change + 1: return minimum_amount_of_change + 1
        minimum_amount_of_change += coin
    
    return minimum_amount_of_change

result = nonConstructibleChange([1, 2, 5])
print(result)

'''
Time complexity = O(n)
Space complexity = O(1)
'''