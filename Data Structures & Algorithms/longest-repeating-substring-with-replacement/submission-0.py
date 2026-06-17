class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_freq = 0
        result = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char,0)+1
            max_freq = max(max_freq, count[char])

            window_size = right - left + 1

            while(window_size-max_freq>k):
                count[s[left]]-=1
                left+=1
                window_size = right - left + 1

            result = max(result, window_size)

        return result
