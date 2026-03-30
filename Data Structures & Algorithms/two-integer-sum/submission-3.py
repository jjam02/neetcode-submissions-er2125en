class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0,len(nums)):
            result = target - nums[i]
            if result in seen:
                retIndex = seen[result]
                return [min(i,retIndex),max(i,retIndex)]
            seen[nums[i]] = i
        return False

            
        