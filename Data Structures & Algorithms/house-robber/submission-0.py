class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n #Here we will use top down approach
        
        def solve(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            rob = nums[i] + solve(i-2)
            skip = solve(i-1)
            dp[i] = max(rob, skip)
            return dp[i]
        return solve(n-1)