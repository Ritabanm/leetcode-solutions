class Solution:
    def averageHeightOfBuildings(self, arr: List[List[int]]) -> List[List[int]]:

        average = lambda x, y: x//y if y else 0

        dct_ct, dct_sm, res = defaultdict(int), defaultdict(int), []

        for beg, end, cnt in arr:
            dct_ct[beg]+= 1
            dct_sm[beg]+= cnt   
            dct_ct[end]-= 1
            dct_sm[end]-= cnt

        pts = sorted(dct_ct)
       
        cur_ct, cur_sm = dct_ct[pts[0]], dct_sm[pts[0]]
        pre_beg, pre_ave = pts[0], average(cur_sm, cur_ct)

        for pt in pts[1:]:
            
            cur_ct+= dct_ct[pt]
            cur_sm+= dct_sm[pt]
            ave = average(cur_sm, cur_ct)

            if pre_ave == ave: continue
            if pre_ave:
                res.append([pre_beg, pt, pre_ave])
            pre_beg, pre_ave = pt, ave

        return res