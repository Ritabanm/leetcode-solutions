from typing import List 
class Solution:
    def medianSlidingWindow(self, nums:List[int], k:int)->List[float]:

        window = SortedList()
        result = []
        for i in range(len(nums)):
            window.add(nums[i])
            if i>=k:
                window.remove(nums[i-k])
            if i>=k-1:
                if k%2==1:
                    result.append(float(window[k//2]))
                else:
                    result.append((window[k//2-1]+window[k//2])/2)
        return result 
