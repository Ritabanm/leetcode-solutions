class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.a=nums1
        self.b=nums2
        self.d = Counter(self.b)
        

    def add(self, index: int, val: int) -> None:
        ele = self.b[index]
        self.d[ele] -= 1
        if self.d[ele] == 0: del self.d[ele]
        self.b[index]+=val
        self.d[self.b[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.d[tot-b] for i,b in enumerate(self.a))