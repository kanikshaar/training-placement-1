class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        self.x = int(a , 2) + int(b , 2)
        # if(self.x == 0):
        #     return "0"
        self.list = list(bin(self.x))
        self.list.remove('0')
        self.list.remove('b')
        return "".join(self.list)
