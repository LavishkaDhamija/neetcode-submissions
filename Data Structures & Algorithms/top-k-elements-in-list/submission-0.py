class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        dict = sorted(dict, key = dict.get,reverse = True)
        return dict[:k]
    