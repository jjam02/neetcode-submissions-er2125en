class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # BEST SOLUTION 
        result = {}
        
        for word in strs:
            freqTable = [0]*26
            for char in word:
                freqTable[ord(char)-97]+=1
            key = tuple(freqTable)
            result.setdefault(key, []).append(word)

        return list(result.values())   