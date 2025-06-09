class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ans = 0
        freq = {}
        for value, label in sorted(zip(values, labels), reverse=True):
            if freq.get(label, 0) < use_limit: 
                ans += value
                num_wanted -= 1
                if not num_wanted: break 
                freq[label] = 1 + freq.get(label, 0)
        return ans 