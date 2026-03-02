

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)   # stores frequency of chars in current window
        left = 0
        max_count = 0              # most frequent character in current window
        res = 0                    # final answer

        for right in range(len(s)):
            # 1️⃣ expand window by including s[right]
            count[s[right]] += 1
            
            # 2️⃣ track the max frequency in current window
            max_count = max(max_count, count[s[right]])
            
            # 3️⃣ if we need to replace more than k characters → shrink window
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            # 4️⃣ update the result (window length)
            res = max(res, right - left + 1)
        
        return res
