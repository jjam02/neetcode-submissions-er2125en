class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for word in strs:
            result["".join(sorted(word))] = result.get("".join(sorted(word)), []) + [word]

        return list(result.values())
            