class Solution(object):
    def searchRange(self, nums, target):
        b=-1
        c=-1
        for i in range(len(nums)):
            if(nums[i]==target):
                b=i
                break
        for j in range(len(nums)-1,-1,-1):
            if(nums[j]==target):
                c=j
                break
        return [b, c]
