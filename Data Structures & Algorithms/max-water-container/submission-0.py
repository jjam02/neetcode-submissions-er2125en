class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        r = len(heights)-1
        l = 0
        while l < r:
            check = abs(l-r) * min(heights[l],heights[r])
            if check > largest:
                largest = check
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return largest
                   
            

        