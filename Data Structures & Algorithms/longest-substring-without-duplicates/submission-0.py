class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        right = 0
        max_len = 0
        n = len(s)
        while right < n:
            if s[right] not in mp or mp[s[right]] == 0:
                mp[s[right]] = 1
            elif s[right] in mp:
                while s[right] in mp and mp[s[right]] != 0:
                    mp[s[left]] -= 1
                    left += 1
                mp[s[right]] = 1

            max_len = max(max_len,right-left+1)
            right += 1

        return max_len
                

            
            

        
        