class Solution:
    def getSum(self, nums: List[int]) -> int:
        #using manachars algorithm

        #step 1 making the array length to odd by adding 0
        arr = []
        for i in nums:
            arr.append(0)
            arr.append(i)
        arr.append(0)

        #step 2 to store the max palindrom len from left and right
        p = [0]*len(arr)

        #step 3 calculating the len of palindrom
        l = -1
        r = -1

        for i in range(len(arr)):
            #if i lies in the bound box
            if i < r:
                mirror = r - i + l
                left = i - p[mirror]
                right = i + p[mirror]
                p[i] = min(r - i , p[mirror])
            else:
                left = i
                right = i

            while left >= 0 and right < len(arr) and arr[left] == arr[right]:
                p[i] += 1
                left -= 1
                right += 1

            #updating the bound box
            if p[i] + i > r:
                r = p[i] + i
                l = i - p[i]

        prefix_sum = []
        prev = 0

        for i in arr:
            prev += i
            prefix_sum.append(prev)


        res = float('-inf')
        for i in range(1,len(arr)):
            ss = prefix_sum[i + p[i] - 1] - prefix_sum[i-1]
            res =max(res,(ss-arr[i])*2 + arr[i])

        return res


        

        
            


                








        