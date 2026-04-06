class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = maxF = res = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            if maxF < count[s[right]]:
                maxF = count[s[right]]
            while (right-l+1) - maxF > k:
                count[s[l]] = count.get(s[l],0) - 1
                l+=1
            res = max(res,(right-l+1))




        return res
