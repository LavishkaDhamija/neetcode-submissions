class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0
        n = len(s)
        
        def expand(left,right):
            while left>=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right -1

        for i in range(n):
            #odd palindrome
            l,r = expand(i,i)
            if r-l+1 > max_len:
                start = l
                max_len = r-l+1
            

            #even palindrome
            l,r = expand(i,i+1)
            if r-l+1 > max_len:
                start = l
                max_len = r-l+1
        
        return s[start:start+max_len]
        


            




        