class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:

        n = len(nums)
        if n <= 1:
            return n

        div = []
        i=1

        while i*i <= n:

            if n % i == 0:
                div.append(i)

                if i != n//i:
                    div.append(n//i)

            i+=1
     
        def check(k):
            chunk  = n //k 
            mini_max = []

            
            for i in range(chunk):
                start = i * k
                inv = 0
                mini = float("inf")
                maxx = float("-inf")

                for j in range(k):
                    curr = nums[start+j]
                    nexx = nums[start+(j+1)%k]

                    if curr > nexx:
                        inv +=1
                    
                    if inv > 1:

                        return False
                    
                    mini = min(mini,curr)
                    maxx = max(maxx,curr)
                
                mini_max.append([mini,maxx])    

            for i in range(chunk-1):
                if mini_max[i][1] > mini_max[i+1][0]:
                    return False
            
            return True

        ans=0
        for k in div:
            if check(k):
                ans+= k

        return ans
            
        
        