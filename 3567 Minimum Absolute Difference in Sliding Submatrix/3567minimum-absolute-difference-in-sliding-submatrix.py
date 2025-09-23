class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        # Create initial window
        windowList = SortedList()
        for idx in range(k):
            for jdx in range(k):
                val = grid[idx][jdx]
                windowList.add(val)

        # Given a sorted subarray window, find the minimum absolute difference by using two pointers
        def computeAbsDiff(windowList):
            W = len(windowList)
            if W == 1:
                # Only one value, so can't have two distinct
                return 0
                
            lowestDiff = inf
            firstVal = secondVal = windowList[0]
            valIdx = 0
            while valIdx < W:
                while secondVal == firstVal:
                    # Search for distinct secondVal
                    valIdx +=1
                    if valIdx == W:
                        break
                    secondVal = windowList[valIdx]

                if valIdx < W:
                    # Found distinct second val
                    absDiff = secondVal - firstVal
                    lowestDiff = min(lowestDiff, absDiff)
                firstVal = secondVal
                
            if lowestDiff == inf:
                # No distinct
                return 0
            else:
                return lowestDiff

        # Move window
        ans = [[-1 for _ in range(N-k+1)] for _ in range(M-k+1)]
        for idx in range(0, M-k+1):
            initialList = windowList.copy() # Copy the list to reset after all jdx is done
            for jdx in range(0, N-k+1):
                
                ans[idx][jdx] = computeAbsDiff(windowList)
                
                # Move right one col
                if (jdx+k) == N:
                    # Can't move right anymore
                    break
                for removeIdx in range(idx, idx+k):
                    # Remove everything in left col
                    windowList.remove(grid[removeIdx][jdx])

                    # Add the new right col
                    windowList.add(grid[removeIdx][jdx+k])

            # Move down one row
            if (idx+k) == M:
                # Can't move down anymore
                break

            windowList = initialList.copy() # Reset windowList from the previous right shifts
            jdx = 0 # Reset jdx so we can clear starting from beginning of row

            for removeJdx in range(jdx, jdx+k):
                # Remove everything in first row
                windowList.remove(grid[idx][removeJdx])
                
                # Add the new last row
                windowList.add(grid[idx+k][removeJdx])
        return ans