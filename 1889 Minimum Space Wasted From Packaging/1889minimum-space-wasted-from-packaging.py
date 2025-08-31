class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        prefix = [0]
        for x in packages: prefix.append(prefix[-1] + x)
        
        ans = inf 
        for box in boxes: 
            box.sort()
            if packages[-1] <= box[-1]: 
                kk = val = 0 
                for x in box: 
                    k = bisect_right(packages, x)
                    val += (k - kk) * x - (prefix[k] - prefix[kk])
                    kk = k
                ans = min(ans, val)
        return ans % 1_000_000_007 if ans < inf else -1 