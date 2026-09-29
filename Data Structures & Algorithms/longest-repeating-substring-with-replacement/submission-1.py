class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = defaultdict(int)
        longest = 0
        l = 0
        for r in range(len(s)):
            alpha[s[r]] += 1
            if r - l + 1 > max(alpha.values()) + k:
                alpha[s[l]] -= 1
                l += 1             
            longest = max(longest, r - l + 1)
        return longest
