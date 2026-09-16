class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        indices1 = defaultdict(list)
        for i, num in enumerate(nums1):
            indices1[num].append(i)

        indices2 = defaultdict(list)
        for i, num in enumerate(nums2):
            indices2[num].append(i)

        n = len(nums1)
        # matches[i] is the number of matches after i rotations
        matches = [0] * n
        for num in indices1:
            for i1 in indices1[num]:
                for i2 in indices2[num]:
                    matches[(i2 - i1) % n] += 1

        return max(matches)