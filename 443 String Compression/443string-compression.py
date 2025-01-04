class Solution:
    def compress(self, chars: List[str]) -> int:
        r, i = 0, 0 
        while (i<len(chars)):
            currChar = chars[i]
            curroccr = 0
            while ((i<len(chars)) and (chars[i] == currChar)):
                curroccr+=1
                i+=1
            chars[r] = currChar
            r+=1
            if(curroccr>1):
                curroccrStr = str(curroccr)
                for j in range(len(curroccrStr)):
                    chars[r] = curroccrStr[j]
                    r+=1
        return r