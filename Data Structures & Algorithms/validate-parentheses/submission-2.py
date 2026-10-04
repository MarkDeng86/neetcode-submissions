class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]":"[", "}":"{"}
        stack = []

        for i in s:
            if i not in Map:
                stack.append(i)
            elif not stack:
                return False
            else:
                check = stack.pop()
                if Map[i] != check:
                    return False
        return not stack
                
