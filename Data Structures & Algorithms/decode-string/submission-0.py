class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append(curr_num)
                curr_num = 0
            elif ch == ']':
                segment = ''
                while not isinstance(stack[-1], int):
                    segment = stack.pop() + segment
                num = stack.pop()
                stack.append(segment * num)
            else:
                stack.append(ch)
        
        return "".join(stack)