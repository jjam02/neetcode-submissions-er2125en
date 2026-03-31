class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]
        for index,temp in enumerate(temperatures):
            print(index,temp)
            while stack and temp > stack[-1][1]:
                stackIndex,stackTemp = stack.pop()
                res[stackIndex] = index-stackIndex
            stack.append((index,temp))
        return res