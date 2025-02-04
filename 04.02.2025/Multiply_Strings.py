class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        c1=len(num1)-1
        c2=len(num2)-1
        r1=r2=0
        for i in num1:
            o1=ord(i)
            r1+=(o1-48)*10**c1
            c1-=1
        for j in num2:
            o2=ord(j)
            r2+=(o2-48)*10**c2
            c2-=1

        return str(r1*r2)
        """
        num1=int(num1)
        num2=int(num2)
        return str(num1*num2)"""
