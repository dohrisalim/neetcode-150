class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=-maxsize
            for k in range(i,j+1):
                coins=nums[i-1]*nums[k]*nums[j+1]+solve(i,k-1)+solve(k+1,j)
                maxi=max(maxi,coins)
            dp[i][j]=maxi
            return dp[i][j]
        
        n=len(nums)
        dp=[[-1 for j in range(n+1)] for j in range(n+1)]
        nums.insert(0,1)
        nums.append(1)
        return solve(1,n)