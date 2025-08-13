class Solution:
    def countSeniors(self, details: List[str]) -> int:
        snr_ct = 0
        for i in details:
            age = int(i[11:13])
            if age>60:
                snr_ct+=1
        return snr_ct