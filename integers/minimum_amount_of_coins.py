'''
https://leetcode.com/problems/coin-change/



'''

def coin_change(coins, amount):
     max = amount + 1 
     minimum_amount_of_coins = [max] * (amount + 1)
     minimum_amount_of_coins[0] = 0
     
     for i in range(1 , amount + 1):     
          for coin in coins:
               if coin <= amount:
                    minimum_amount_of_coins[i] = min(minimum_amount_of_coins[i], 1 + minimum_amount_of_coins[i - coin])
               
               
     return -1 if minimum_amount_of_coins[amount] > amount else minimum_amount_of_coins[amount]

result = coin_change([1,2,5],20)
print(result)

'''
Time complexity = O(n * m)
Space complexity = O(n)
'''