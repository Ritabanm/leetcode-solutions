class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # After sorting power[], say M(n) is the selected maximizing sequence for the sub-array containing powers up to power n and sum(M(n)) = S(n).
        # Then  M(n+3) must be [(M(*) with max S(*) up to * <= n), n+3], meaning S(n+3) = max(S(1), ..., S(n)) + n + 3.
        #
        # The search for max(...) can be further simplified by considering only up to values for which are not considered in the previous step.
        # Therefore for the first valid appendable result S(j) from j = n, n-1, ... of the sorted power[], the search range should be bounded to 
		# * such that S(*) >= S(j) - 3.
        # Using this logic, we may iterate up from the smallest element.
        
        # This stores values of S(power(n)). -1 is a placeholder.
        values = [-1] * len(power)
        # Sort power in ascending order.
        power.sort()

        # Set base case: S(power(0))
        values[0] = power[0]

        for i in range(len(power)):
            if i == 0: continue
            
            # We look back from i; j = i-1, i-2,... until we find a j such that power[j] < power[i] - 2
            j = i - 1
            
            considerMax = -1
            
            # Before that, however, in the duplicate case, just carry over the previous result + power.
            if power[j] == power[i]:
                values[i] = values[j] + power[i]
                continue
				
            # Else, do the look-back:
            while j >= 0 and power[j] >= considerMax:
                if power[j] < power[i] - 2:
                    values[i] = max(values[i], values[j] + power[i])
					
				# considerMax (lower bound for j) is set when we find the first appendable element
                    if considerMax == -1:
                        considerMax = power[j] - 3
                j -= 1
            
            if values[i] == -1:
                # If no match, then S(i) is simply power[i] 
                values[i] = power[i]
        return max(values)