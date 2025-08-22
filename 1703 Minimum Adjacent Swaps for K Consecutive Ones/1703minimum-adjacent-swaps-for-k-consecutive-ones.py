class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # nums has 1s and zeros

        # can swap two adj in one move
        
        # what's the minimum number of moves to get k consec. ones?
        # something something sliding window?

        # move windows of size k around
        #   ............000111011101011101............
        #               ------------------
        #                    have k-7 zeros
        #     

        # simpler example:
        #          ............. 010110 ...........
        #                        ------
        #                           k, 3 zeros
        #     if we know the prior indices of ones, and we want to swap in 1:
        #          > index of first 0 in the window: that's the cost to swap it to the front
        #          > then keep swapping to the location of the prior 1
        #          > so it's firstZeroIdx - lastOneIdx
        #
        #          > repeat for later zeros: the above gets us e.g. 01101 -> 11101
        #              so we need to get to 01111 (swap zero at window idx 3 to front of window), then swap prior one into position
        #                
        #            so it's sum of first z zeros minus sum of prior z one indices
        #     when we move the window by 1: prior z one indices increases if we shifted off a 1
        #     and sum of first z zeros increases potentially if we shift off a zero, otherwise decreases by z

        # that involves O(k) work per shift, too much
        # can we reduce that to O(1)?
        # what if we know the cost to swap each prior 1 into position?

        #   like 11000110100
        #                 1
        #                  2
        # doesn't reall help. We could store the cost of moving k, but that would be O(n*k) dp which is still too expensive
        
        # what about
        #    having a sliding window of k ones | we get the cost to swap those k ones into position. SOME contig. set of 1s
        #    will be the answer b/c it doesn't make sense to swap ones past each other
        #
        #    there are many indices in the window though
        #
        #       1101001010101010001   k==9
        # BUT: to "condense" all the ones, we know the 0s have to get swapped to one side or the other!
        #     to swap left: sum of zero indices minus sum of of where all the zeros would go (l, l+1,...)
        #     to swap right: sum of where all the zeros would go minus sum of zero indices (r, r-1, ...)

        # so we "just" need the sum of zero indices relative to l

        if k == 1: return 0

        # earlier: had a more naive solution what
        #    found windows with k ones
        #       then computed cost to shift all the zeros to the left or right edges
        #       mostly right, except it misses a case like this:
        #
        #     10111111111111111111101
        #  clearly the solution is to swap twice, putting one zero on either side
        #
        # how can we fix this?
        #      we have a 0 close to the left edge: move it left
        #      we have a zero close to the right edge: move it right
        #
        #      zeros start out closest to right edge, then get closer to left as we advance the window
        #      so we gradually "shuffle" indices left
        #      deque stuff!!!

        l = nums.index(1)

        # two deques: left_idxs are indices of zeros where it's cheaper to move that zero to the left edge
        left_idxs = deque()
        lsum = 0
        right_idxs = deque()
        rsum = 0

        ones = 1
        ans = math.inf
        for r in range(l+1, len(nums)):
            if nums[r] == 1:
                ones += 1
                if ones > k:
                    ones -= 1 # drop left-most 1
                    l += 1

                    # TODO: we know all the indices of zeros so we can probably avoid re-iterating
                    while nums[l] == 0: l += 1 # also drop left-most zeros we no longer need
                    while left_idxs and left_idxs[0] < l:
                        lsum -= left_idxs[0]
                        left_idxs.popleft()
                    while right_idxs and right_idxs[0] < l:
                        rsum -= right_idxs[0]
                        right_idxs.popleft()
            else:
                right_idxs.append(r)
                rsum += r

            # cost to move zero left: current index is l, move it to l+num_earlier_zeros
            # b/c after swapping prior zeros into position, the target index advances by the number of zeros

            while right_idxs and right_idxs[0]-l-len(left_idxs) < r-len(right_idxs)+1-right_idxs[0]:
                # less expensive to shift right_idxs[0] left
                lsum += right_idxs[0]
                rsum -= right_idxs[0]
                left_idxs.append(right_idxs.popleft())

            while left_idxs and left_idxs[-1]-l-len(left_idxs)+1 > r-len(right_idxs)-left_idxs[-1]:
                # less expensive to shift left_idxs[-1] right
                lsum -= left_idxs[-1]
                rsum += left_idxs[-1]
                right_idxs.appendleft(left_idxs.pop())

            if ones == k:
                # l cost: move the left zeroes to l..l+len(left_idxs)-1
                lcost = lsum - ((l+len(left_idxs)-1)*(l+len(left_idxs))//2 - (l-1)*l//2)
                # r cost: move right zeros to r-len(left_idxs)+1 .. r
                rcost = r*(r+1)//2 - (r-len(right_idxs))*(r-len(right_idxs)+1)//2 - rsum

                ans = min(ans, lcost + rcost)

        return ans

        ### STILL not quite right

        # I messed up a case like this:
        #    1000000011
        #   it's cheaper to move all the zeros left even though some are closer than right
        #   "easy" way to check: look at the right-most 0
        #      cost to shift left: 1, because
        #         it's like 8 spots above l
        #         but 7 of those prior 8 are also zeros
        #         so we shift idx-l-preceedingZeros == 1
        #      cost to shift right: 2, because
        #         shift right r-idx = 2, minus zero because there are no zeros in the way
        #    so we'd detect that the right-most zero index actually belongs in left_idxs
        #    this property is monotonic, in that if idx is closer to left, then idx' > idx
        #    is either still closer to left, or should now be in right
        #
        #    so we can repair the invariant that all left_idxs shift left, all right_idxs shift right
        #    by looking at the right-most left and left-most right, and moving until the invariant holds again

        # UGHHHH