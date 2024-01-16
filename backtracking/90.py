class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, t):
            ans.append(list(t))
            
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                    
                t.append(nums[i])
                backtrack(i + 1, t)
                t.pop()

        ans = []
        nums.sort()
        backtrack(0, [])
        return ans