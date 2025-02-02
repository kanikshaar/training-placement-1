class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching_bracket = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for index, bracket in enumerate(s): 
            if bracket in ['(','{','[']:
                # new bracket is open, add its index to stack
                stack.append(bracket)
                continue
                
            # new bracket is closed
            if index == 0 or not stack or matching_bracket[stack[-1]] != bracket:
                return False
            stack.pop()
            
        # finished iterating, valid if stack is empty
        return not stack
