class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                diff = target-nums[i]-nums[j]
                print("DIFF:",target,"-",i,"-",j,"=",diff)
                if diff == 0:
                    return [i,j]
        return [0,0]
        