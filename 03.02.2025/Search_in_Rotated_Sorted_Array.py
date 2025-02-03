class Solution(object):
    def search(self, nums, target):
        x=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                continue
            else:
                x=i
                print(x)
                break
        start=0
        end=x
        mid=(start+end)//2
        while start<=mid:
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
            mid=(start+end)//2

        start=x+1
        end=len(nums)-1
        mid=(start+end)//2
        while start<=mid:
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
            mid=(start+end)//2
        return -1
