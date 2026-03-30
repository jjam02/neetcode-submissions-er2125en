class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # BEST SOLUTION 
        result = {}
        
        for word in strs:
            freqTable = [0]*26
            for char in word:
                freqTable[ord(char)-ord('a')]+=1
            key = tuple(freqTable)
            result[key] = result.get(key, []) + [word]

        return list(result.values())   