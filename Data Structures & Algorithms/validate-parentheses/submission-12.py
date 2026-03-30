class Solution:
    def isValid(self, s: str) -> bool:

        leftFacing = "({["
        bracketMatch = {")":"(","}":"{","]":"["}
        stack = []
        for bracket in s:
            if bracket in leftFacing:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                leftMatch = stack.pop()
                if bracketMatch[bracket]!= leftMatch:
                    return False
        return not stack
        