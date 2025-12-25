class Solution:
    def singleDivisorTriplet(self, nums):
        def valid_triplets(i,j,k):
            s = i+j+k 

            if s%i == 0:
                return s%j != 0 and s%k != 0

            if s%j == 0:
                return s%k != 0

            return s%k == 0

        result, dict1 = 0, Counter(nums)

        for i in range(1,101):
            for j in range(i,101):
                for k in range(j,101):
                    if dict1[i] and dict1[j] and dict1[k] and valid_triplets(i,j,k):
                        if i == j:
                            result += dict1[k]*(dict1[i]*(dict1[i]-1))//2
                        elif j == k:
                            result += dict1[i]*(dict1[j]*(dict1[j]-1))//2 
                        elif i == k:
                            result += dict1[j]*(dict1[i]*(dict1[i]-1))//2
                        else:
                            result += dict1[i]*dict1[j]*dict1[k]

        return 6*result