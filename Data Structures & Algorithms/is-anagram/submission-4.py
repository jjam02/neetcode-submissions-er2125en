class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            else:
                 s_chars[char] =s_chars[char]+1
        for char in t:
            if char not in t_chars:
                t_chars[char] = 1
            else:
                t_chars[char] =t_chars[char]+1
        return s_chars == t_chars

