class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        sufix = [1]
        ans = []
        p = 1
        s = 1
        for i in range(1,len(nums)):
            p *= nums[i-1]
            prefix.append(p)
        
        for i in range(len(nums)-2,-1,-1):
            s *= nums[i+1]
            sufix.append(s)

        sufix = sufix[::-1]
        
        for p,s in zip(prefix,sufix):
            ans.append(p*s)
        
        return ans

