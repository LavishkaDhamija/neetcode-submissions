class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        num1 = nums
        for i in range(len(num1)):
            left = i+1
            right = len(num1) - 1
            while left < right:
                sum1 = num1[left] + num1[right]
                if sum1 == -num1[i]:
                    result = [num1[i],num1[left],num1[right]]
                    if result not in ans:
                        ans.append(result)
                    left += 1
                    right -= 1
                elif sum1 < -num1[i]:
                    left += 1
                elif sum1 > -num1[i]:
                    right -= 1
        return ans
                    

        