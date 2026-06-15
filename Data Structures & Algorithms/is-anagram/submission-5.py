class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word:list[str] = list(t)

        for char in s:
            if char in word:
                word.remove(char)
            else:
                return False

        return True
