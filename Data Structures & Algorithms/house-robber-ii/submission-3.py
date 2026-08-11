class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def rob_case(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * (n)
            dp[0] = nums[0]
            dp[1] = max(nums[1],nums[0])
            for i in range(2,n):
                dp[i] = max(nums[i]+ dp[i-2], dp[i-1])
            return dp[n-1]
        
        if n == 1:
            return nums[0]
        case_1 = rob_case(nums[:-1])
        case_2 = rob_case(nums[1:])
        return max(case_1,case_2)
        