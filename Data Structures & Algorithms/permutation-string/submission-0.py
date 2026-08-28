class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        freq_s1 = {}
        for i in s1:
            if i in freq_s1:
                freq_s1[i] += 1
            else:
                freq_s1[i] = 1
        freq_s2 = {}
        left = 0
        right = 0
        while right < len(s2):
            if s2[right] in freq_s2:
                freq_s2[s2[right]] += 1
            else:
                freq_s2[s2[right]] = 1

            if right - left + 1 > n:
                freq_s2[s2[left]] -= 1
                if freq_s2[s2[left]] == 0:
                    del freq_s2[s2[left]]
                left += 1
            
            if freq_s1 == freq_s2:
                return True

            right += 1

        return False


        