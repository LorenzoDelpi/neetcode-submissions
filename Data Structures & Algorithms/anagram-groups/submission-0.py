class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_parsed: List[dict[str, int]]= []
        
        for word in strs:
            word_parsed: dict[str,int] = {}
            for char in word:
                word_parsed[char] = word_parsed.get(char, 0) + 1
            strs_parsed.append(word_parsed)

        result: List = []
        saw_words = []

        for i, word_parsed in enumerate(strs_parsed):
            group: List[str] = []
            if word_parsed not in saw_words:
                saw_words.append(word_parsed)
                group.append(strs[i])
                for j in range(i+1, len(strs_parsed)):
                    if word_parsed == strs_parsed[j]:
                        group.append(strs[j])
                
    
            if group:
                result.append(group)
            
        
        return result