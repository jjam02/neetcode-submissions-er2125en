class Solution:
    def isValid(self, s: str) -> bool:

        leftFacing = "({["
        rightFacing = ")}]"
        bracketMatch = {")":"(","}":"{","]":"["}
        stack = []
        for bracket in s:
            if bracket in leftFacing:
                stack.append(bracket)
            elif bracket in rightFacing:
                if not stack:
                    return False
                leftMatch = stack.pop()
                if bracketMatch[bracket]!= leftMatch:
                    return False
        return True and not stack
        