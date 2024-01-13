class Solution:
    def numberOfPairs(self, nums1, nums2, queries):
        freq = Counter(nums2)
        res = []
        totaloff = 0
        half = len(nums2) // 2

        i = 0
        while i < len(queries):
            q = queries[i]
            if len(q) == 2:
                target, cnt = q[1], 0
                for num in nums1:
                    cnt += freq[target - num + totaloff]
                res.append(cnt)
            else:
                l, r, offset = q[1], q[2], q[3]
                # merge consecutive type-1 queries with same [l, r]
                while (
                    i + 1 < len(queries)
                    and len(queries[i + 1]) == 4
                    and queries[i + 1][1] == l
                    and queries[i + 1][2] == r
                ):
                    offset += queries[i + 1][3]
                    i += 1

                if r - l + 1 > half:
                    totaloff -= offset
                    for j in range(l):
                        freq[nums2[j]] -= 1
                        nums2[j] -= offset
                        freq[nums2[j]] += 1
                    for j in range(r + 1, len(nums2)):
                        freq[nums2[j]] -= 1
                        nums2[j] -= offset
                        freq[nums2[j]] += 1
                else:
                    for j in range(l, r + 1):
                        freq[nums2[j]] -= 1
                        nums2[j] += offset
                        freq[nums2[j]] += 1
            i += 1

        return res