class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == "+":
                left = stack.pop()
                right = stack.pop()
                stack.append(left+right)
            elif token == "-":
                left = stack.pop()
                right = stack.pop()
                print(left,"-",right)
                stack.append(right-left)
            elif token == "*":
                left = stack.pop()
                right = stack.pop()
                stack.append(left*right)
            elif token == "/":
                left = stack.pop()
                right = stack.pop()
                if left!=0:
                    stack.append(int(right/left))
                else:
                    stack.append(0)
            else:
                stack.append(int(token))
        return stack[-1]