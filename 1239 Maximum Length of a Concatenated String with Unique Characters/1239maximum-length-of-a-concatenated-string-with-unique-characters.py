class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        # Precompute bitmasks, skip strings with duplicate chars
        masks = []
        for s in arr:
            mask = 0
            valid = True
            for c in s:
                bit = 1 << (ord(c) - ord('a'))
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            if valid:
                masks.append((mask, len(s)))
        
        def backtrack(index, current_mask, current_len):
            res = current_len
            for i in range(index, len(masks)):   # iterate over masks, not arr
                mask, length = masks[i]
                if current_mask & mask == 0:
                    res = max(res, backtrack(i + 1, current_mask | mask, current_len + length))
            return res
        
        return backtrack(0, 0, 0)
