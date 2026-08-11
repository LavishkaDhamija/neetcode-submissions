class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_arr = [float('-inf')] * n
        min_arr = [float('inf')] * n

        max_arr[0] = nums[0]
        min_arr[0] = nums[0]

        for i in range(1,n):
            x = max_arr[i-1]*nums[i]
            y = min_arr[i-1]*nums[i]
            max1 = max(x,y)
            min1 = min(x,y)

            max_arr[i] = max(max1,nums[i])
            min_arr[i] = min(min1,nums[i])

        return max(max_arr)

