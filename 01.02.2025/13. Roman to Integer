class Solution(object):
    def romanToInt(self, s):
        D={'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        r=0
        for i in range(len(s)-1):
            curr=D[s[i]]
            if curr>=D[s[i+1]]:
                r+=curr
            else:
                r-=curr
        r+=D[s[-1]]
        return r
