class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.append(0)
        sum1=0
        i=0
        while i<len(prices)-1:
              
              if(prices[i]<prices[i+1]):
              
                    lmin=prices[i]
                    i=i+1
                    while i<len(prices):
                          if(prices[i]>prices[i+1]):
                                lmax=prices[i]
                                sum1=sum1+lmax-lmin
                                i=i+1
                                break
                          else:
                                i=i+1
              else:
              
              
                    i=i+1
        
        return sum1