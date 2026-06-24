class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        def count(n):
            if n < 0: 
                return 0
            s = str(n)
            length = len(s)
            
            # dp[len][digit] = total valid paths of 'length' starting with 'digit'
            dp = [[0] * 10 for _ in range(length + 1)]
            for d in range(10):
                dp[1][d] = 1
                
            for i in range(2, length + 1):
                for d in range(10):
                    low, high = max(0, d - k), min(9, d + k)
                    dp[i][d] = sum(dp[i - 1][low : high + 1])
            
            # Count all numbers with FEWER digits than n
            total = 1  # Include 0
            for i in range(1, length):
                total += sum(dp[i][1:])  # Can't start with a leading zero
            
            # Count numbers with SAME number of digits, prefix-matching 's'
            for i in range(length):
                curr = int(s[i])
                start = 1 if i == 0 else 0
                
                for d in range(start, curr):
                    if i == 0 or abs(d - int(s[i - 1])) <= k:
                        rem_len = length - i - 1
                        total += dp[rem_len + 1][d]
                        
                if i > 0 and abs(curr - int(s[i - 1])) > k:
                    break
            else:
                total += 1  # 'n' itself is valid
                
            return total
            
        return count(r) - count(l - 1)