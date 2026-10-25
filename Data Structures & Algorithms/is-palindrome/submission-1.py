class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for let in s:
            if let.isalnum():
                letters.append(let)
        s = "".join(letters).lower()
        return s == s[::-1]