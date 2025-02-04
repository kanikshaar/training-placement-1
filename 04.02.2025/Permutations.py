class Solution(object):
    def permutation(self, a, nums, res):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for choice in nums:
            if (choice not in a):
                a.append(choice)
                if (len(a) == len(nums)):
                    res.append(a[:])
                else:
                    self.permutation(a, nums, res)
                a.remove(choice)
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = []
        res = []
        self.permutation(a, nums, res)
        return res
