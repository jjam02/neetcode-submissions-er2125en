class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = {}  # val -> index
        nums.sort()
        seen_trip = set()
        target = 0
        res = []
        for i, n in enumerate(nums):
            indices[n] = i
        for i, n in enumerate(nums):
            
            for j in range(i+1,len(nums)):
                
                diff =  -(n+nums[j])
                #print(diff,"=","-(",n,"+",nums[j],")")
                if diff in nums and (indices[diff]!= j and indices[diff]!=i):
                    triplet = [nums[j],n,diff]
                    #print(tuple(sorted(triplet)),"in ", seen_trip)
                    if tuple(sorted(triplet)) in seen_trip:
                        #print("been there done that")
                        continue
                    #print("UNIQUE TRIP",n,diff,nums[j])
                    res.append([n,nums[j],diff])
                    seen_trip.add(tuple(sorted(triplet)))
                   
        return list(res)
            
        

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indices = {}  # val -> index

#         for i, n in enumerate(nums):
#             indices[n] = i

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in indices and indices[diff] != i:
#                 return [i, indices[diff]]