from math import sqrt
class Solution:
    def smallestValue(self, n: int) -> int:
        def returnPrimeFactor(n):
            res = 0
            while n % 2 == 0:
                res += 2
                n = n // 2
            
            for i in range(3,int(sqrt(n)+1),2):
                while n % i == 0:
                    res += i
                    n = n // i

            if n > 1:
                res += n
            return res

        def primeFactor(num):
            sieveList = [True for _ in range(num+1)]
            sieveList[0] = sieveList[1] = False
            p = 2

            while p * p <= num:
                if sieveList[p]:
                    for i in range(p*p,num+1,p):
                        sieveList[i] = False
                p += 1

            numList = []
            for i in range(len(sieveList)):
                if sieveList[i] == True:
                    numList.append(i)

            return numList
        
        listOfFactors = primeFactor(n)
        print(listOfFactors)

        if n in listOfFactors:
            return n
        else:
            ans = n
            while ans not in listOfFactors:
                newAns = returnPrimeFactor(ans)
                if ans == newAns:
                    return ans
                ans = newAns
                
            return ans


# s = Solution()
# print(s.smallestValue(4))