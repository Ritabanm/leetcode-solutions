class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        n, r1, r2, r3, r4 = len(arr1), [], [], [], []

        for i in range(n):
            r1.append(arr1[i]+arr2[i]+i)
            r2.append(arr1[i]+arr2[i]-i)
            r3.append(arr1[i]-arr2[i]+i)
            r4.append(arr1[i]-arr2[i]-i)

        r1.sort()
        r2.sort()
        r3.sort()
        r4.sort()

        return max([r1[-1]-r1[0],r2[-1]-r2[0],r3[-1]-r3[0],r4[-1]-r4[0]])