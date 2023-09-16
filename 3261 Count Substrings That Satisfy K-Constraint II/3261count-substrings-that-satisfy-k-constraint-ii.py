class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        q = len(queries)

        num_zero, num_one = 0, 0
        left_indices, right_indices = [], []
        right_prefix_sums = [0]
        left = 0
        for right, ch in enumerate(s):
            if ch == '0':
                num_zero += 1
            if ch == '1':
                num_one += 1
            
            # Adjust the left pointer to maintain the constraint
            while num_zero > k and num_one > k:
                left_indices.append(left)
                right_indices.append(right)
                if s[left] == '0':
                    num_zero -= 1
                if s[left] == '1':
                    num_one -= 1
                left += 1

        # Compute prefix sums for right indices
        for r in right_indices:
            right_prefix_sums.append(right_prefix_sums[-1] + r)

        res = []
        for l, r in queries:
            l_idx = bisect_left(left_indices, l)
            r_idx = bisect_right(right_indices, r)

            num_indices = r_idx - l_idx

            # Calculate the number of invalid substrings
            ans = (r + 1) * num_indices - (right_prefix_sums[r_idx] - right_prefix_sums[l_idx])

            # Total possible substrings
            total = ((r - l + 1) * (r - l + 2)) // 2

            # Subtract invalid substrings from the total
            res.append(total - ans) if l_idx <= r_idx else res.append(total)
        
        return res