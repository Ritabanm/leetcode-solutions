class Solution:
    def specialPalindrome(self, n: int) -> int:
        store = []
        def build(num):
            a = ''
            mid = ''
            for i in num:
                if int(i)%2==1:
                    a+=i*((int(i) - 1)//2)
                    mid = i
                else:
                    a+=i*(int(i)//2)
            if a=="":
                store.append(int(mid))
            else:
                for p in permutations(a):
                    p = ''.join(p)
                    store.append(int(p+mid+p[::-1]))

        for mask in range(1, 1<<9):
            num = ''
            odd = 0
            digits = 0
            for d in range(1,10):
                if mask&(1<<(d-1)):
                    num+=str(d)
                    digits+=d
                    if d%2==1:
                        odd+=1
                if len(num)>16 or odd>1:
                    break
            if len(num)<=16 and odd<=1:
                if digits==len(str(n)) or digits==len(str(n))+1:
                    build(num)
        store.sort()
        ind = bisect.bisect_left(store, n+1)
        return store[ind]