class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        candidates.sort()

        def recursion(ind,temp,summ):
            if (summ==target):
                ans.append(temp)
                return 
            elif (summ>target or ind>=len(candidates)):
                return 

            recursion(ind+1,temp+[candidates[ind]],summ+candidates[ind])

            while ((ind+1<len(candidates) and candidates[ind]==candidates[ind+1])):
                ind+=1
        
            recursion(ind+1,temp,summ)


        recursion(0,[],0)
        return ans
