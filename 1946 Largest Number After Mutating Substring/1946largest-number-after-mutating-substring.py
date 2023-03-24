class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        grp = []
        first, last = 0, 0
        for i, el in enumerate(num):
            el = int(el)
            ch = change[el]
            if grp:
                if ch >= el:
                    last = i
                    grp.append(str(ch))
                    continue
                else:
                    break
            if ch > el:
                first = i
                last = i
                grp.append(str(ch))

        return num[:first]+''.join(grp)+num[last+1:] if grp else num
        