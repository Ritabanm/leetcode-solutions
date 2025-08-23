class Solution:
    def longestAwesome(self, s):
        n, dict1, mask, max_len = len(s), {0:-1}, 0, 0 

        for i in range(n):
            mask = mask^(1<<int(s[i]))

            if mask not in dict1:
                dict1[mask] = i 
            else:
                max_len = max(max_len,i-dict1[mask])

            for j in range(10):
                mask1 = mask^(1<<j)
                if mask1 in dict1:
                    max_len = max(max_len,i-dict1[mask1])

        return max_len