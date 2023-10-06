class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort()

        #sum the biggest k elements
        result = sum(nums[-k:])
        if(result%2==0): #return if biggest k is even
            return result

        #find smallest odd and even in result sum
        smallestOddInResult = None
        smallestEvenInResult = None
        for num in reversed(nums[-k:]):
            if(num%2):
                smallestOddInResult = num
            else:
                smallestEvenInResult = num
        
        #find biggest even and odd outside result sum
        biggestEvenOutside = None
        biggestOddOutside = None
        for num in nums[:-k]:
            if(num%2):
                biggestOddOutside = num
            else:
                biggestEvenOutside = num
        
        #swap odd in result with even outside result sum
        canSwapOddForEven = smallestOddInResult is not None and biggestEvenOutside is not None
        oddSwappedForEven = result-smallestOddInResult+biggestEvenOutside if canSwapOddForEven else -1
        #swap even in result with odd outside result sum
        canSwapEvenForOdd = smallestEvenInResult is not None and biggestOddOutside is not None
        evenSwappedForOdd = result-smallestEvenInResult+biggestOddOutside if canSwapEvenForOdd else -1
        #return the biggest sum or -1 if there is nothing to swap with
        return max(oddSwappedForEven, evenSwappedForOdd)