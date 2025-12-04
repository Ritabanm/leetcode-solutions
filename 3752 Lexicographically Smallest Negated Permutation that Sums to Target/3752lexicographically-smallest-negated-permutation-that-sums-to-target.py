class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> list[int]:
        cur = n * (n + 1) // 2
        if abs(target) > cur or (cur - abs(target)) % 2 == 1:
            return []
        neg = set()
        for i in range(n, 0, -1):
            if cur - i * 2 >= target: # Greedy pick: Always choose the largest number that we can negate
                cur -= i * 2
                neg.add(i)
        arr = []
        for i in range(1, n + 1):
            if i in neg:
                arr.append(-i)
            else:
                arr.append(i)
        return sorted(arr)