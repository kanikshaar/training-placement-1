class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0  # Edge case for x = 0

        left, right = 0, x  # Define search space
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid  # Perfect square case
            elif mid * mid < x:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        
        return right  # `right` will be the integer sqrt of `x`
