class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        candidates = set()
        length = 0
        bestLength = 0
        for num in nums:
            if num+1 in nums or num==0:
                candidates.add(num)
        if not candidates:
            return 0
        for num in candidates:
            i=0
            while num+i in nums:
                length+=1
                if length>bestLength:
                    bestLength  =length
                i+=1
            length=0

        return bestLength