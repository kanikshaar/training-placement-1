class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0
        farthest = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums) - 1):
            farthest = max(farthest,i+nums[i]) # if we are in i plus nums[i] is how far we can jump
            
            if i == current_end: # jump again
                jumps+=1
                current_end = farthest # update our current end

            if current_end >= len(nums) - 1: # we have reached our destination
                return jumps
