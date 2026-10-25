class Solution:
    def isValid(self, s: str) -> bool:
        currentOpen = []
        openClose = {")":"(", "]":"[","}":"{"}

        for i in s:
            if i in openClose.values():
                currentOpen.append(i)
            else:
                if len(currentOpen) == 0:
                    return False
                openBracket = currentOpen.pop()
                if openClose[i] == openBracket:
                    continue
                return False
        return len(currentOpen) == 0