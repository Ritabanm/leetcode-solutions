class Solution:
    def minOperations(self, s1,s2):
        n = len(s1)
        if s1=='1' and s2=='0':
            return -1
        s1 = list(s1)
        s2 = list(s2)

        ans = 0
        for i in range(n):
            if s1[i]==s2[i]:
                continue
            if s1[i]=='0':
                ans+=1
                s1[i]='1'
            else:
                s1[i]='0'
                if i+1<n and s1[i+1]=='1':
                    s1[i+1]='0'
                    ans+=1
                else:
                    ans+=2
        return ans