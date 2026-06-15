class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # --- 1. Feasibility Check (Prefix Sum) ---
        # Used to prune impossible queries immediately
        bad = [0]
        pv = -1
        p = 0
        for x in nums:
            v = x % k
            p += (v != pv)
            bad.append(p)
            pv = v

        # --- 2. Discretization & Mo's Setup ---
        # Map values to 1-based ranks for BIT
        # Normalize values to x // k for calculation
        vals = [x // k for x in nums]
        sorted_vals = sorted(list(set(vals)))
        rank_map = {v: i for i, v in enumerate(sorted_vals, 1)}
        m = len(sorted_vals)
        
        # Sort queries to minimize pointer movement (Block size approx n / sqrt(q))
        block_size = max(1, n // int(len(queries)**0.5 or 1))
        # Store queries as (block_index, right, left, original_index)
        sorted_queries = [(s // block_size, t, s, i) for i, (s, t) in enumerate(queries)]
        # Standard Mo's sorting order with odd/even optimization
        sorted_queries.sort(key=lambda x: (x[0], x[1] if x[0] & 1 else -x[1]))

        # --- 3. Fenwick Tree (BIT) & State ---
        cnt_bit = [0] * (m + 1) # Frequency BIT
        sum_bit = [0] * (m + 1) # Value Sum BIT
        curr_cnt = 0
        curr_sum = 0
        
        def update(i, delta):
            nonlocal curr_cnt, curr_sum
            v = vals[i]
            rank = rank_map[v]
            
            # Update global state
            val_delta = delta * v
            curr_cnt += delta
            curr_sum += val_delta
            
            # Update BITs
            while rank <= m:
                sum_bit[rank] += val_delta
                cnt_bit[rank] += delta
                rank += rank & -rank

        # --- 4. Process Queries ---
        ans = [-1] * len(queries)
        l, r = 0, -1 # Current window [l, r]
        highest_bit = 1 << (m.bit_length() - 1) # For binary lifting

        for _, q_end, q_start, q_idx in sorted_queries:
            # Pruning: Skip impossible queries entirely
            # This is the key optimization allowing Python to pass in ~3s
            if bad[q_end + 1] - bad[q_start + 1]:
                continue
            
            # Adjust window
            while l > q_start:
                l -= 1
                update(l, 1)
            while r < q_end:
                r += 1
                update(r, 1)
            while l < q_start:
                update(l, -1)
                l += 1
            while r > q_end:
                update(r, -1)
                r -= 1
            
            # Find Median via Binary Lifting on BIT
            # We look for the largest prefix index where count <= total_count / 2
            idx = 0
            prefix_cnt = 0
            prefix_sum = 0
            mask = highest_bit
            target = curr_cnt >> 1
            
            while mask:
                next_idx = idx + mask
                if next_idx <= m and prefix_cnt + cnt_bit[next_idx] <= target:
                    idx = next_idx
                    prefix_cnt += cnt_bit[idx]
                    prefix_sum += sum_bit[idx]
                mask >>= 1
            
            # Calculate Cost
            # median value is at sorted_vals[idx] (0-indexed logic from BIT 1-based)
            median = sorted_vals[idx]
            
            # Left part: elements <= median rank (accumulated during lifting)
            # Right part: total - left
            suf_sum = curr_sum - prefix_sum
            suf_cnt = curr_cnt - prefix_cnt
            
            # Cost = (Sum_Right - Median * Count_Right) + (Median * Count_Left - Sum_Left)
            ans[q_idx] = (suf_sum - median * suf_cnt + median * prefix_cnt - prefix_sum)

        return ans