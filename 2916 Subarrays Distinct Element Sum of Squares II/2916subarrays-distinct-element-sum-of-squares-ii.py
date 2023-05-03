class SegmentTree:
    def __init__(self, arr: list[int], l: int, r: int):
        self.lazy = 0
        self.l, self.r = l, r
        if l == r:
            self.left = self.right = None
            self.sum = arr[l]
            self.squareSum = arr[l] * arr[l]
        else:
            mid = (r + l) // 2
            self.left = SegmentTree(arr, l, mid)
            self.right = SegmentTree(arr, mid + 1, r)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum
    
    def getSquareSum(self, l: int, r: int):
        if l <= self.l and self.r <= r:
            return self.squareSum
        elif self.l > r or self.r < l:
            return 0
        else:
            return self.left.getSquareSum(l, r) + self.right.getSquareSum(l, r)
    
    def add(self, l: int, r: int, k: int):
        # pending update
        if self.lazy > 0:
            selfK = self.lazy
            self.lazy = 0
            self.add(self.l, self.r, selfK)

        if l <= self.l and self.r <= r:
            self.squareSum += (2 * k * self.sum + k * k * (self.r - self.l + 1))
            self.sum += k * (self.r - self.l + 1)
            
            # lazy propagation
            if self.left != None:
                self.left.lazy += k
            if self.right != None:
                self.right.lazy += k
        elif self.l > r or self.r < l:
            return
        else:
            self.left.add(l, r, k)  
            self.right.add(l, r, k)
            self.sum = self.left.sum + self.right.sum
            self.squareSum = self.left.squareSum + self.right.squareSum

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        m = 1000000007
        # range query
        root = SegmentTree([0] * len(nums), 0, len(nums) - 1)
        # last occurance
        lastSeen = {}

        # consider the subarrays ending at i.
        # for any j < i, if arr[i] has not occured previously, it will contribute +1 to all prev subarrays ending at i - 1 for distinct element count in subarrays [j..i]
        # [1] -> [1]
        # [1, 2] -> [2, 1] 
        # [1, 2, 3] -> [3, 2, 1]
        # But if arr[i] has pccured previously then it will not contribute to the subarrays where it creates duplicates.
        # [1, 2, 3, 2] -> [3, 2, 2, 1]
        # the problem boiles down to finding last occurance and range update.
        for i in range(len(nums)):
            st = 0
            if nums[i] in lastSeen:
                st = lastSeen[nums[i]] + 1
            # range update with lazy propagation
            root.add(st, i, 1)
            ans = (ans + root.getSquareSum(0, len(nums) - 1)) % m
            lastSeen[nums[i]] = i

        return ans