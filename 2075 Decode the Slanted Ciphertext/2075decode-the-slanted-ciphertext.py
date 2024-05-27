class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText)//rows
        
        res = ""
        
        for i in range(cols):
            idx = i
            for j in range(rows):
                if idx >= len(encodedText):
                    break
                    
                res += encodedText[idx]
                idx += (cols+1)
                
        i = len(res)-1       
        while i >= 0:
            if res[i] !=  " ":
                break
            i -= 1
                
        return res[:i+1]
        