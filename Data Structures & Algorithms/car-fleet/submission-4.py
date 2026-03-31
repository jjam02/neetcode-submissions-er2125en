class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipList = list(zip(position,speed))
        zipList.sort(reverse=True)
        stack = []
        for pos,spd in zipList:
            time = (target-pos)/spd
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)