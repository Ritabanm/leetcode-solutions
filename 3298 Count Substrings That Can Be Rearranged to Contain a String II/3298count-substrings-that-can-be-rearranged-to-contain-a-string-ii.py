class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        res = 0
        mpp = [[0, 0] for _ in range(26)]  # To store frequencies of both words
        l, r = 0, 0
        n = len(word1)
        m = len(word2)
        size = 0
        
        # Count frequency of characters in word2
        for ch in word2:
            mpp[ord(ch) - ord('a')][1] += 1
        
        while r < n:
            # Slide the window while it contains all characters of word2
            while size == m and l <= r:
                res += (n - r + 1)
                mpp[ord(word1[l]) - ord('a')][0] -= 1
                if mpp[ord(word1[l]) - ord('a')][1] > 0 and mpp[ord(word1[l]) - ord('a')][0] < mpp[ord(word1[l]) - ord('a')][1]:
                    size -= 1
                l += 1
            
            # Expand the window
            if mpp[ord(word1[r]) - ord('a')][1] > 0 and mpp[ord(word1[r]) - ord('a')][0] < mpp[ord(word1[r]) - ord('a')][1]:
                size += 1
            mpp[ord(word1[r]) - ord('a')][0] += 1
            r += 1
        
        # Handle remaining valid substrings
        while size == m and l <= r:
            res += (n - r + 1)
            mpp[ord(word1[l]) - ord('a')][0] -= 1
            if mpp[ord(word1[l]) - ord('a')][1] > 0 and mpp[ord(word1[l]) - ord('a')][0] < mpp[ord(word1[l]) - ord('a')][1]:
                size -= 1
            l += 1
        
        return res