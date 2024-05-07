class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        cant= 0
        can = set()
        can.add(primeOne)
        can.add(primeTwo)
        for i in range(1,primeOne*primeTwo):
            if (i-primeOne in can or i-primeTwo in can)or (i in can):
                can.add(i)
            else:
                cant =i
        return cant
        