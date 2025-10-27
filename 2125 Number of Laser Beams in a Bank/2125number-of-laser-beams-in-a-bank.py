class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0 
        for row in bank: 
            curr = row.count('1')
            if curr: 
                ans += prev * curr
                prev = curr 
        return ans 