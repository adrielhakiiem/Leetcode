class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        
        for price in prices:
            if price < minprice: # find min price 
                minprice = price 
            elif price - minprice > maxprofit: # find max price
                maxprofit = price - minprice 
            
        return maxprofit 
