class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        ans = [-1, -1]
        min_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = [left, right]
                
                window[s[left]] -= 1
                
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        l,r = ans
        return "" if min_len == float("inf")else s[l:r +1]
