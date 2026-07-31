import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        ans = []
        while len(nums) > k:
            heapq.heappop(nums)
        self.numss = nums
        self.kk = k

    def add(self, val: int) -> int:
        heapq.heappush(self.numss,val)
        while len(self.numss) > self.kk:
            heapq.heappop(self.numss)
        return self.numss[0]

        
