class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            longest = max(longest, right - left + 1)

        return longest