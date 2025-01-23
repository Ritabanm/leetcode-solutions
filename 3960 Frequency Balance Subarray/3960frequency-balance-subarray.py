class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            ele_count = Counter()
            freq_count = Counter()
            for j in range(i, n):
                val = nums[j]
                
                old_freq = ele_count[val]
                new_freq = old_freq + 1
                
                ele_count[val] = new_freq

                if old_freq > 0:
                    freq_count[old_freq] -= 1
                    if freq_count[old_freq] == 0:
                        del freq_count[old_freq]
                
                freq_count[new_freq] += 1

                if len(freq_count) == 1:
                    if j==i or len(ele_count)==1:
                        res = max(res, j-i+1)
                elif len(freq_count) == 2: 
                    freq = sorted(freq_count.keys())
                    
                    if freq[1] == freq[0] * 2:
                        res = max(res, j-i+1)
                    
        return res