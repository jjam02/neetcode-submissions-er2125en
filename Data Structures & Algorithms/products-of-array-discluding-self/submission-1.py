


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # SLOW AND CRINGE AND USES IMPORT BAD
        #import math
        # res = []
        # for i in range(len(nums)):
        #     res.append(math.prod(nums[:i]+nums[i+1:]))
        # return res

        # cool optimal approach uses 1 array and prefix suffix

        res = [1]*len(nums) 
        #prefix loop
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix*= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post*= nums[i]
        return res
