class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        res = [0] * len(barcodes)
        i = 0
        for num,freq in count.most_common():
            for _ in range(freq):
                res[i] = num
                i += 2
                if i >= len(barcodes):
                    i = 1
        return res