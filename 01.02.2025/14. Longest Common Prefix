class Solution(object):
    def longestCommonPrefix(self, strs):

        # find the smallest word and check if it itself /
        # it's prefixes are prefixes of other words
        # this is the largest string of length 201.
        pre = "_" * 201 

        
        # find the smallest word.
        for s in strs:
            if len(s) < len(pre):
                pre = s
        n = len(strs)
        ans = ""
    
        # Iterate every index of prefix word
        for i in range(len(pre)):
            ch = pre[i]

            # check if the same ch is present at that index
            # for all words
            for s in strs:
                if s[i] == ch:
                    continue
                else:
                    return ans # if not, return the ans
            ans += ch # if same ch is at all index, add the ch to ans.
            
        return ans # return ans at last
