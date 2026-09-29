class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcdecfbd
        l = 0
        alpha = set()
        longest = 0
        for char in s:
            if char in alpha:
                longest = max(longest, len(alpha))
                while s[l] != char:
                    alpha.remove(s[l])
                    l += 1
                alpha.remove(s[l])
                l += 1
            alpha.add(char)
        longest = max(longest, len(alpha))
        return longest

