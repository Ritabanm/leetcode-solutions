class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nameMinK = dict()
        res = []
        for name in names:
            if name not in nameMinK:
                res.append(name)
                nameMinK[name]=0
            else:
                k =nameMinK[name]+1
                tmp = name + '(' + str(k) + ')'
                while tmp in nameMinK:
                    k+=1
                    tmp = name + '(' + str(k) + ')'
                
                res.append(tmp)
                nameMinK[name] = k
                nameMinK[tmp] = 0
        return res