class Solution:
    def largestAltitude(self, gain):
        if not gain:
            return 0
        
        curr_alt = 0
        highest_point = 0

        for alt in gain:
            curr_alt+=alt
            highest_point = max(curr_alt, highest_point)
        return highest_point

        #T:O(N) {since every altitude needs to be traversed}, S: O(1)