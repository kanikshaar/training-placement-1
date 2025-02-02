class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        c=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[c]=nums[i]
                c=c+1
        return c
