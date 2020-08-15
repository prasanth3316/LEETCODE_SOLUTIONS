class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                
                k=0
                for j in range(len(nums)-1,i-1,-1):
                    if(nums[j]>nums[i-1]):
                        k=j
                        break
                    
                nums[i-1],nums[k]=nums[k],nums[i-1]
                nums[i:]=reversed(nums[i:])
                return nums
        return nums.sort()