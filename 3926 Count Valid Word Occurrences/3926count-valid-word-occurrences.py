class Solution:
    def countWordOccurrences(self, ch: list[str], q: list[str]) -> list[int]:
        t='qwertyuiopasdfghjklzxcvbnm'
        s=''
        d={}
        f=0
        lst=0
        for st in ch:
            l=len(st)
            j=0
            while j<l:
                c=st[j]
                if c in t:
                    if lst:
                        lst=0
                        s += '-'
                    s += c
                    f=1
                elif c==' ':
                    d[s]=d.get(s,0)+1
                    s=''
                    f=0
                    lst=0
                else:
                    if f:
                        if (j+1)<l and st[j+1] in t:
                            s += '-'
                            j += 1
                            s += st[j]
                            f=1
                        elif (j+1)<l:
                            d[s]=d.get(s,0)+1
                            s=''
                            f=0
                            while (j+1)<l and st[j+1] not in t:
                                j += 1
                        else:
                            lst=1
                            f=0
                    else:
                        d[s]=d.get(s,0)+1
                        while (j+1)<l and st[j+1] not in t:
                            j += 1
                        s=''
                        lst=0
                        f=0
                j += 1
        d[s]=d.get(s,0)+1
        ans=[]
        for i in q:
            ans.append(d.get(i,0))
        return ans

        
