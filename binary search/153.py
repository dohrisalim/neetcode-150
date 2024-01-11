class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle]<nums[(middle-1+n)%n] and nums[middle]<nums[(middle+1)%n]:
                return nums[middle]
            elif nums[middle]>nums[right]:
                left=middle+1
            else:
                right=middle-1
        
        return nums[0]