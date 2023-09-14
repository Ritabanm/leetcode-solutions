class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index):
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        return s

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        # We track the balance: b * (even_count) - a * (odd_count)
        # For each element, let's map: even -> b, odd -> -a
        # Wait, let's look at the inequality: b*x <= a*y  =>  b*x - a*y <= 0
        # Let transformed weight: even -> b, odd -> -a ? Let's verify:
        # Sum of weights for subarray = b*(total evens) - a*(total odds) <= 0 means b*x <= a*y.
        # Let's check with an element: 
        # If element is even, contribution to x is +1, so weight should be b? No, let's use:
        # even -> +b, odd -> -a? Wait: 
        # b*x - a*y <= 0 means sum of (b if even else -a) for elements in subarray.
        # Let's check prefix sums: pref[r+1] - pref[l] <= 0 => pref[r+1] <= pref[l].
        
        transformed = [(b if x % 2 == 0 else -a) for x in nums]
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + transformed[i]
            
        sorted_unique_prefs = sorted(list(set(pref)))
        val_to_rank = {val: i + 1 for i, val in enumerate(sorted_unique_prefs)}
        
        bit = FenwickTree(len(sorted_unique_prefs))
        valid_subarrays = 0
        
        for p in pref:
            rank = val_to_rank[p]
            # We want prefix sums in 'seen' that are >= p because pref[r+1] <= pref[l]
            total_seen = bit.query(len(sorted_unique_prefs))
            strictly_less = bit.query(rank - 1)
            valid_subarrays += (total_seen - strictly_less)
            
            bit.update(rank, 1)
            
        return valid_subarrays