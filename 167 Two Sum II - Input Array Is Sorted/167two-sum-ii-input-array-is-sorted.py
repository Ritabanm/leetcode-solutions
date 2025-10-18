class Solution:
    def twoSum(self, numbers, target):

        #Edge case numbers is empty list
        if not numbers or len(numbers)==0:
            return []
        
        #2 pointers:
        l = 0
        r = len(numbers)-1
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum==target:
                return [l+1, r+1]
            elif sum<target:
                l+=1
            else:
                r-=1
        return [-1,1]

        #T:O(N) since all elements need to be seen.
        #S: O(1) since no extra space.
        