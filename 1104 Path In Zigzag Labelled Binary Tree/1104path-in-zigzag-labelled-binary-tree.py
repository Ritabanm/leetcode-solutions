class Solution:
    
    def pathInZigZagTree(self, label: int) -> List[int]:
        rows = [(1, 0)] #row represented by tuple (min_element_in_row, is_neg_order)
        while rows[-1][0]*2 <= label:
            rows.append((rows[-1][0]*2, 1 - rows[-1][1]))
            
        power, negOrder = rows.pop()
        
        res = []
        while label > 1:
            res.append(label)
                
            if negOrder:
                # adjust label position and find parent with division by 2
                # a, b - range of current row 
                a, b = power, power*2 -1
                label = (a + (b - label))//2
            else:
                # divide label by 2 and adjust parent position
                # a, b - range of previous row
                a, b = power//2, power - 1
                label = b - (label//2 - a)
                
            power, negOrder = rows.pop()
            
                          
        res.append(1)
                          
        return res[::-1]