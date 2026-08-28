class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        interval = [intervals[0][0],intervals[0][1]]
        ans = []
        for i in range(1,len(intervals)):
            if interval[1] < intervals[i][0]:
                ans.append(interval)
                # ans.append(intervals[i])
                interval = intervals[i]
            else:
                interval[0] = min(interval[0],intervals[i][0])
                interval[1] = max(interval[1],intervals[i][1])
        
        ans.append(interval)
        return ans




        