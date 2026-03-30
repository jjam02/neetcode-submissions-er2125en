class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        res = []
        
        # product of all non-zero numbers
        mult = 1
        for num in nums:
            if num != 0:
                mult *= num
        
        for num in nums:
            if zero_count > 1:
                res.append(0)          # two zeros means everything is 0
            elif zero_count == 1:
                if num == 0:
                    res.append(mult)   # only the zero slot gets the product
                else:
                    res.append(0)      # everyone else multiplies by the zero
            else:
                res.append(int(mult / num))  # no zeros, safe to divide
        
        return res