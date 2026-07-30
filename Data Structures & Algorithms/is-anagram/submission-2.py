class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        if len(s) == len(t):
            for word1,word2 in zip(s,t):
                if word1 in s_hash:
                    s_hash[word1] += 1
                else:
                    s_hash[word1] = 1

                if word2 in t_hash:
                    t_hash[word2] += 1
                else:
                    t_hash[word2] = 1

            for item in s_hash:
                if item not in t_hash:
                    return False
                if s_hash[item] != t_hash[item]:
                    return False
        else:
            return False
        
        return True
            

        