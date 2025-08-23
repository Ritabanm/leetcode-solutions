class Solution:
    def amountPainted(self, paint):
        dict1, result = {}, []
        
        def find(x):
            if x not in dict1:
                return x 
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        def union(x,y):
            a, b = find(x), find(y)

            if a != b:
                dict1[a] = b 

            return b

        for s,e in paint:
            painted_area, cur = 0, find(s) 

            while cur < e:
                cur = union(cur,cur+1)
                painted_area += 1 

            result.append(painted_area)
            
        return result 