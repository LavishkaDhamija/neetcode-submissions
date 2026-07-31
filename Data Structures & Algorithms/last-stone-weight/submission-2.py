import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = []
        for stone in stones:
            nums.append(-stone)

        heapq.heapify(nums)

        while len(nums) > 1:
            l1 = -(heapq.heappop(nums))
            l2 = -(heapq.heappop(nums))
            if l1 == l2:
                continue
            elif l1 > l2:
                heapq.heappush(nums,-(l1-l2))
        if nums == []:
            return 0
        return -(nums[0])
