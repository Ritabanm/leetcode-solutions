class Solution:
    def search(self, L: int, a: int, MOD: int, n: int, nums: List[int]) -> str:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # Compute the hash of the substring S[:L].
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % MOD
              
        # Store the already seen hash values for substrings of length L.
        seen = collections.defaultdict(list)
        seen[h].append(0)
        
        # Const value to be used often : a**L % MOD
        aL = pow(a, L, MOD) 
        for start in range(1, n - L + 1):
            # Compute the rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % MOD
            if h in seen:
                # Check if the current substring matches any of the previous substrings with hash h.
                current_substring = nums[start : start + L]
                if any(current_substring == nums[index : index + L] for index in seen[h]):
                    return start
            seen[h].append(start)
        return -1
        
    def longestDupSubstring(self, S: str) -> str:
        # Modulus value for the rolling hash function to avoid overflow.
        MOD = 10**9 + 7
        
        # Select a base value for the rolling hash function.
        a = 26
        n = len(S)
        
        # Convert string to array of integers to implement constant time slice.
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        
        # Use binary search to find the longest duplicate substring.
        start = -1
        left, right = 1, n - 1
        while left <= right:
            # Guess the length of the longest substring.
            L = left + (right - left) // 2
            start_of_duplicate = self.search(L, a, MOD, n, nums)
            
            # If a duplicate substring of length L exists, increase left and store the
            # starting index of the duplicate substring.  Otherwise decrease right.
            if start_of_duplicate != -1:
                left = L + 1
                start = start_of_duplicate
            else:
                right = L - 1
        
        # The longest substring (if any) begins at index start and ends at start + left.
        return S[start : start + left - 1]