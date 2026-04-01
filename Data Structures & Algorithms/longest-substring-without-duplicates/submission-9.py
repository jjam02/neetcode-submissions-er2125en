class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l=0
        sub = set()
        for i,char in enumerate(s):
            print(sub)
            while char in sub:
                sub.remove(s[l])
                print(sub)
                l+=1
            sub.add(char)
            longest = max(len(sub),longest)
        return longest