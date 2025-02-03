class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1" #base case
        prev = self.countAndSay(n-1)
        i = 1
        counter = 1
        ans = ""
        while i < len(prev):
            if prev[i-1] == prev[i]:
                counter += 1
            else:
                ans = ans + str(counter) + prev[i-1]
                counter = 1
            i += 1
        return ans + str(counter) + prev[i-1]
