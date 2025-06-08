class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = [0, 1]
        
        for _ in range(n - 1):
            tmp = []
            for num in ans:
                tmp.append(2 * num+ 1)
                if num%2 == 1: tmp.append(2 * num)
 
            ans = tmp
        ans = [bin(a)[2:].rjust(n,'0') for a in ans]
        return ans