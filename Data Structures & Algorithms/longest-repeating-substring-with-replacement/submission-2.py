class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0
        mp = {}
        while right < len(s):
            if s[right] in mp:
                mp[s[right]] += 1
            else:
                mp[s[right]] = 1
                
            max_char = max(mp.values())
            window_len = right - left + 1
            replacements = window_len - max_char
            if replacements > k:
                mp[s[left]] -= 1
                if mp[s[left]] == 0:
                    del mp[s[left]]
                left += 1
            else:
                max_len = max(right - left + 1,max_len)

            right += 1

        return max_len

           

    
