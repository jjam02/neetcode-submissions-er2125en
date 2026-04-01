class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        sub = ""
        for i,char in enumerate(s):
            if char not in sub:
                sub+=char
                
            else:
                sub = sub[sub.index(char)+1:]+char
            longest = max(len(sub),longest)
        return longest