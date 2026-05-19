class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            if i == '}' or i == ')' or i == ']':
                hasClose = True  
            if i == '}':
                stack.pop()
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if i == ')':
                stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if i == ']':
                stack.pop()
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack and (stack[-1] == '[' or stack[-1] == '(' or stack[-1] == '{'):
            return False
        return True
            


                