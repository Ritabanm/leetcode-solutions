class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)
        # Build the max frequency counter for all characters in words2
        for w in words2:
            count_w = Counter(w)
            for c, cnt in count_w.items():
                count_2[c] = max(count_2[c], cnt)

        res = []
        # Check each word in words1 if it meets the requirement
        for w in words1:
            count_w = Counter(w)
            flag = True
            for c, cnt in count_2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            # Append to result outside the character check loop
            if flag:
                res.append(w)
        return res
