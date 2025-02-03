class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        signed = 1 if dividend>0 else -1
        signor = 1 if divisor>0 else -1
        sign =signed*signor
        
        if dividend!=-2**31:
            dividend = max(dividend, (-2**31))
        elif dividend == -2**31 and divisor==-1:
            dividend =  -2**31 +1
        else:
            dividend =dividend
        
        divisor = min(divisor, (2**31)-1)
        ans = sign*(abs(dividend)//abs(divisor))
        return(ans)
