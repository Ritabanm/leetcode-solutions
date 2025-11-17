class Solution {
    func checkZeroOnes(_ s: String) -> Bool {
        
        var cz = 0
        var co = 0
        
        var mz = 0
        var mo = 0
        
        for c in s {
            
            if c == "0" {
                cz += 1
                co = 0
            }
            else {
                cz = 0
                co += 1
            }
            
            mz = max(mz, cz)
            mo = max(mo, co)
        }
        
        return mo > mz
    }
}