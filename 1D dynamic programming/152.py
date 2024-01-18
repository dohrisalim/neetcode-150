class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = ans = nums[0]

        for value in nums[1:]:
            max_temp = max_prod * value
            min_temp = min_prod * value

            min_prod = min(max_temp, min_temp, value)
            max_prod = max(max_temp, min_temp, value)
            
            ans = max(ans, max_prod)

        return ans