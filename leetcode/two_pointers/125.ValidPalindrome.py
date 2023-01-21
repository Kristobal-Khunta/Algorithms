class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        left = 0
        right = len(s) - 1
        while right > left:
            last_el = s[right].lower()
            if not str.isalnum(last_el):
                right -= 1
                continue
            first_el = s[left].lower()
            if not str.isalnum(first_el):
                left += 1
                continue
            if last_el != first_el:
                return False
            left += 1
            right -= 1
        return True


class SolutionNeetcode:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
