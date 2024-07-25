class Solution:

    def findPermutation(self, strs: str) -> List[int]:
        length = len(strs)
        self.builds = [idx + 1 for idx in range(length + 1)]
        head, tail = 0, 0
        while tail < length:
            if strs[tail] == "I": 
                tail += 1
                continue
            head = tail
            while tail < length and strs[tail] == "D":
                tail += 1
            self.reverse(head, tail)
            tail += 1
            
        return self.builds
    
    def reverse(self, head: int, tail: int) -> None:
        while head < tail:
            self.builds[head], self.builds[tail] = self.builds[tail], self.builds[head]
            head += 1
            tail -= 1