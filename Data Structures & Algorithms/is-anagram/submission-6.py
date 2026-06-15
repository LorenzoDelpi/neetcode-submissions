class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_s: dict[str, int] = {}
        word_t: dict[str, int] = {}
        for char in t:
            occurences = word_t.get(char)
            if occurences is None:
                word_t.update({char: 1})
            else:
                 word_t.update({char: occurences+1})


        for char in s:
            occurences = word_s.get(char)
            if occurences is None:
                word_s.update({char: 1})
            else:
                 word_s.update({char: occurences+1})
        
        for key, value in word_s.items():

            if not word_t.get(key) == value:
                return False
       

        return True
