class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==1):
            return [strs]
        
        result = []
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams.keys():
                
                anagrams[sorted_word] +=[word]
            else:
                anagrams[sorted_word] = anagrams.get(sorted_word,[word])
        return anagrams.values()

        