class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        copy_set = {}
        copy_set = set(nums)
        max_count = 0
        for i in nums:
            count = 0
            if (i-1) not in copy_set:
                j = i + 1
                count = 1
                while (j) in copy_set:
                    count += 1
                    j = j + 1
            max_count = max(count, max_count)
        return max_count
        