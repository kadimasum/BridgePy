class BestTimeToSellStock:

    '''
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    

    Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


    PSEUDOCODE
    ----------
    funtion(prices):
        right = 1
        left = 0
        max_profit = 0
        while prices[right] < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, (prices[right] - prices[left]))
            else: left = right
            right += 1
        return max_profit
            

    ---------------------------- 
    Time Complexity = O(n)
    Space Complexity = O(1)
    ----------------------------

    '''

    def max_profit(prices: list[int]) -> int:

        '''
        Function calculates and returns maximum profit as an integer

        left: int
        right: int
        max_p: int 

        '''
        left = 0
        right = 1
        max_p = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_p = max(max_p, (prices[right] - prices[left]))
            else: left = right
            right += 1
        return max_p

if __name__ == "__main__":
    result =  BestTimeToSellStock.max_profit( [7,1,5,3,6,4])
    print(result)