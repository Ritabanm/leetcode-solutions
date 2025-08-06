class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:  
        result = 0
        for hour in hours:
            if hour >= target:
                result+=1
        return result