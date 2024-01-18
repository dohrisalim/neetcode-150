class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def solve(ind,target):
            if target==0:
                return True
            if ind==0:
                return nums[ind]==target
            if dp[ind][target]!=-1:
                return dp[ind][target]
            not_pick=solve(ind-1,target)
            pick=False
            if target>=nums[ind]:
                pick=solve(ind-1,target-nums[ind])
            dp[ind][target]=pick or not_pick
            return dp[ind][target]
        s=sum(nums)
        if s%2!=0:
            return False
        s//=2
        n=len(nums)
        dp=[[-1 for j in range(s+1)] for i in range(n)]
        return solve(n-1,s)