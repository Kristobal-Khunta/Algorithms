class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}  # store existing simbols
        max_count = 0
        left = 0
        answer = 0
        for right in range(len(s)):

            seen[s[right]] = seen.get(s[right], 0) + 1
            max_count = max(max_count, seen[s[right]])

            if (right - left + 1) - max_count > k:
                seen[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)
        return answer
