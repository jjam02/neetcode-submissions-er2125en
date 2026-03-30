class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        count = 1
        longest = 0
        for number in nums:
            if number-1 in nums:
                continue
            else:
                while number+1 in nums:
                    count +=1
                    number+=1
            if count > longest:
                longest=count
            count=1
        return longest 