class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        

        d = dict()

        for i in range(len(nums)):
            subarr = nums[i: i + k]
            d[i] = subarr
        #print(d)
        for kk in d:
            #print(kk)
            if kk + k in d:
                print(d[kk], d[kk + k])
                if len(d[kk]) == len(d[kk + k]):
                    flag = True
                    for i in range(1, len(d[kk])):
                        if d[kk][i - 1] >= d[kk][i]:
                            flag = False
                    for i in range(1, len(d[kk + k])):
                        if d[kk + k][i - 1] >= d[kk + k][i]:
                            flag = False
                    if flag:
                        return True
        return False
                



        
                