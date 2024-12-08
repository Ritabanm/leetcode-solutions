class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:

        def isValid(i: int)-> bool:
        
            if fontInfo.getHeight(fonts[i]) > h: return False

            ctr = Counter(text)
  
            return sum(fontInfo.getWidth(fonts[i], 
                         ch)*ctr[ch] for ch in ctr) <= w

        
        left, right = 0, len(fonts)-1
        
        while left <= right:
            mid = (left + right)//2
            
            if isValid(mid): left = mid + 1
            else: right = mid - 1
                
        return fonts[left-1] if left else -1