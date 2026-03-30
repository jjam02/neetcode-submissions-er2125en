class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        seenS = {}
        seenT = {}
        for i in range(0,len(s)):
            seenS[s[i]] = seenS.get(s[i], 0) + 1
            seenT[t[i]] = seenT.get(t[i], 0) + 1
        return seenS == seenT



