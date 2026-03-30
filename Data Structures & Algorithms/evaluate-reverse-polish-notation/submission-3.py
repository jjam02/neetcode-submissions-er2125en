class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                left = stack.pop()
                right = stack.pop()
                print(str(left)+"+"+str(right))
                stack.append(left+right)
            elif token =="-":
                left = stack.pop()
                right = stack.pop()
                print(str(left)+"-"+str(right))
                stack.append(right-left)
            elif token == "*":
                left = stack.pop()
                right = stack.pop()
                print(str(left)+"*"+str(right))
                stack.append(left*right)
            elif token =="/":
                left = stack.pop()
                right = stack.pop()
                print(str(right)+"/"+str(left))
                if left == 0:
                    stack.append(0)
                else:
                    stack.append(int(right/left))
            else:
                stack.append(int(token))
        return stack[-1]
            

        