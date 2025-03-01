class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:

        d = defaultdict(list)
        ctr = Counter(s).items()                        # <-- 1)    
        
        for ch, k in ctr:                               # <-- 2)    
            d[k].append(ch)
        
        ans = max(d, key = lambda x: (len(d[x]), x))    # <-- 3) 

        return ''.join(d[ans])                          # <-- 4) 