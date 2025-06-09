class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True

        char_map = {}

        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = [i, i]
            
            char_map[s[i]][1] = i
        
        intervals = []

        for i in range(len(s)):
            if i != char_map[s[i]][0]:
                continue
            
            left, right = i, char_map[s[i]][1]
            isValid = True
            while left < right:
                if char_map[s[left]][0] < i:
                    isValid = False
                    break

                right = max(char_map[s[left]][1], right)
                left += 1
            
            if isValid and (right - i) + 1 < len(s):
                intervals.append([i, right])
        
        intervals.sort(key=lambda x: x[1])
        
        prev_end = -1
        count = 0
        for j in range(len(intervals)):
            if intervals[j][0] > prev_end:
                prev_end = intervals[j][1]
                count += 1
            
            if count >= k:
                return True
        
        return False