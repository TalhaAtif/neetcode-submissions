class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        for char in s:
            if char in "({[":
                open.append(char)
            if char in ")}]":
                if not open:
                    return False
                curr = open.pop(-1)
                if char == ")" and curr != "(":
                    return False
                elif char == "}" and curr != "{":
                    return False
                elif char == "]" and curr != "[":
                    return False
            
        return len(open) == 0