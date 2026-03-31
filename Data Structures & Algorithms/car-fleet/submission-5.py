class Solution:
    


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipList = list(zip(position,speed))
        zipList.sort(reverse=True)
        stack = []
        for pos,speed in zipList:
            time = (target-pos)/speed
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            

        return len(stack)

