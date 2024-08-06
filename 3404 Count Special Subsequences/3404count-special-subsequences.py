class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0

        fractions_fwd = defaultdict(list)  # Stores lists of q indices for fractions formed by (p, q)
        fractions_bwd = defaultdict(list)  # Stores lists of r indices for fractions formed by (s, r)

        # Generate fractions for (p, q) pairs
        for q in range(2, n):
            for p in range(0, q - 1):
                if q - p > 1:
                    numerator = nums[p]
                    denominator = nums[q]
                    g = gcd(numerator, denominator)
                    reduced_fraction = (numerator // g, denominator // g)
                    fractions_fwd[reduced_fraction].append(q)

        # Generate fractions for (r, s) pairs
        for r in range(0, n - 2):
            for s in range(r + 2, n):
                if s - r > 1:
                    numerator = nums[s]
                    denominator = nums[r]
                    g = gcd(numerator, denominator)
                    reduced_fraction = (numerator // g, denominator // g)
                    fractions_bwd[reduced_fraction].append(r)

        # For each fraction, match q and r indices to count valid subsequences
        for fraction in fractions_fwd:
            if fraction in fractions_bwd:
                q_list = fractions_fwd[fraction]
                r_list = fractions_bwd[fraction]

                # Sort the lists to efficiently count valid pairs
                q_list.sort()
                r_list.sort()

                total_count_f = 0
                j = 0
                len_r = len(r_list)
                for q in q_list:
                    # Move the pointer j to satisfy r > q + 1 (implies r - q > 1)
                    while j < len_r and r_list[j] <= q + 1:
                        j += 1
                    # Count the number of valid r indices for this q
                    total_count_f += len_r - j

                total_count += total_count_f

        return total_count