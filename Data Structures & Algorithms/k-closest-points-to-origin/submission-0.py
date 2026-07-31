import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i,j in points:
            d = math.sqrt((i - 0)**2 + (j - 0)**2)
            heapq.heappush(dist,(d,[i,j]))

        ans = []
        while k!=0:
            distance,point = heapq.heappop(dist)
            ans.append(point)
            k = k-1
        return ans
        


        