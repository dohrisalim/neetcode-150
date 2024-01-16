class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsetGenerator(i,nums,l,ans):
            if i==len(nums):
                if l not in ans:
                    ans.append(l)
                return

            subsetGenerator(i+1,nums,l+[nums[i]],ans)
            subsetGenerator(i+1,nums,l,ans)
            return ans

        return subsetGenerator(0,nums,[],[])