class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        list1=[0 for i in range(len(nums))]
        if(nums[0]==1):
            list1[0]=1
            max=1
        for i in range(1,len(nums)):
            if(nums[i]!=1):
                list1[i]=0
                
            else:
                list1[i]=list1[i-1]+1
                if(max<list1[i]):
                    max=list1[i]
        return max