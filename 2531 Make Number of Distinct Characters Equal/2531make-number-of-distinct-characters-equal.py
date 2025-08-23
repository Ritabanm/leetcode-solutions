class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1,c2=Counter(word1),Counter(word2)
        num1,num2=len(c1),len(c2)
        for k1,v1 in c1.items():
            for k2,v2 in c2.items():
                cur1,cur2 =num1,num2
                if v1==1 and k1!=k2:
                    cur1-=1
                if v2 == 1 and k1 !=k2:
                    cur2-=1
                if k1 not in c2:
                    cur2+=1
                if k2 not in c1:
                    cur1 +=1
                if cur1 ==cur2:
                    return True
        return False