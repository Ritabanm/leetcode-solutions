class Solution:
    def destCity(self, paths):

        starts = set()

        for src, dest in paths:
            starts.add(src)
        
        for _,dest in paths:
            if dest not in starts:
                return dest