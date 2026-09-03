class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
            
        s1_count = {}
        window_count = {}
        
        for i in range(len1):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1
            
        if s1_count == window_count:
            return True
            
        for i in range(len1, len2):
            right_char = s2[i]
            window_count[right_char] = window_count.get(right_char, 0) + 1
            
            left_char = s2[i - len1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
                
            if s1_count == window_count:
                return True
                
        return False