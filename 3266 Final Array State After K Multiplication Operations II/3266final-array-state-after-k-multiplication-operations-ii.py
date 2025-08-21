from typing import List, Tuple
import math
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        c = int(1e9 + 7)
        s = sorted([[nums[i], i] for i in range(len(nums))])
        # print(s)
        i = 0
        h: List[List[int]] = []
        while k > 0 and i < len(s) - 1:
            multiples = []
            items: List[Tuple[int, int]] = []
            total_needed = 0
            heapq.heappush(h, s[i])
            while len(h) > 0 and h[0][0] * multiplier <= s[i + 1][0]:
                num, idx = heapq.heappop(h)
                # figure out how much we need to multiply by until this s[i][0] * multiplier > s[i+1][0]
                times = math.floor(math.log(s[i + 1][0] / num) / math.log(multiplier))
                multiples.append(times)
                items.append((num, idx))
                total_needed += times

            if total_needed > k:
                # ugly situation
                # take advantage that as of now, s[j][0] < s[j+1][0] < ...
                # and distribute our k across all these values
                # print("ugly", total_needed, k, items, multiples, "i", i)
                all_get = k // len(items)
                some_get = k % len(items)
                for num, idx in items:
                    next_num = num * pow(
                        multiplier, all_get + 1 if some_get > 0 else all_get, c
                    )
                    heapq.heappush(h, [next_num, idx])
                    if some_get > 0:
                        some_get -= 1
                k = 0
            else:
                # easy situation, just multiply
                for (num, idx), times in zip(items, multiples):
                    next_num = num * pow(multiplier, times, c)
                    heapq.heappush(h, [next_num, idx])
                k -= total_needed
            i += 1
            # print("now have", s)
        # push remaining
        for j in range(i, len(s)):
            heapq.heappush(h, s[j])

        # print("after all, have", s)
        all_get = k // len(s)
        some_get = k % len(s)
        while len(h) > 0:
            num, idx = heapq.heappop(h)
            nums[idx] = (
                num * pow(multiplier, all_get + 1 if some_get > 0 else all_get, c)
            ) % c
            if some_get > 0:
                some_get -= 1

        return nums