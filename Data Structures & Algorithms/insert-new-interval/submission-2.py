class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        inserted = False
        for i,j in intervals:
            if j < newInterval[0]:
                ans.append([i,j])
            elif i > newInterval[1]:
                if not inserted:
                    ans.append(newInterval)
                    inserted = True
                ans.append([i,j])
            else:
                newInterval[0] = min(i,newInterval[0])
                newInterval[1] = max(j,newInterval[1])

        if inserted == False:    
            ans.append(newInterval)
        return ans
           
