class Solution:
    def checkValidString(self, s: str) -> bool:
        left_paren_stack, asterisk_stack = [], []
        
        for i in range(len(s)):
            if s[i] == '(':
                left_paren_stack.append(i)
            elif s[i] == '*':
                asterisk_stack.append(i)
            else:
                if left_paren_stack:
                    left_paren_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False
        
        while left_paren_stack and asterisk_stack:
            if left_paren_stack[-1] > asterisk_stack[-1]:
                return False
            left_paren_stack.pop()
            asterisk_stack.pop()
            
        return not left_paren_stack