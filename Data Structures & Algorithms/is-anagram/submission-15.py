class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_s: dict[str, int] = {}
        word_t: dict[str, int] = {}

        for i in range(len(s)):
            occurences_s:int = word_s.get(s[i], 0)
            occurences_t:int = word_t.get(t[i], 0)
            word_s[s[i]] = occurences_s + 1
            word_t[t[i]] = occurences_t + 1
        
        # this can also be done with word_t == word_s
        for key, value in word_s.items():
            if not word_t.get(key) == value:
                return False
       

        return True

       
# from collections import Counter
# s_counts = Counter("apple")
# print(s_counts) # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
