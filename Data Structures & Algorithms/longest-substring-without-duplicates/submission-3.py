class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substr = ""

        for i,char in enumerate(s):
            print("looking at:",char,"substr:",substr)
            if char not in substr:  
                substr += char
            else:
                print(substr)
                longest = max(len(substr),longest)
                substr = substr[substr.index(char)+1:] + char
            

        return max(len(substr),longest)