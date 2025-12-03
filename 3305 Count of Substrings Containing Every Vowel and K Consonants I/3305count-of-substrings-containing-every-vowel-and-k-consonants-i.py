class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        v = {'a','e','i','o','u'}
        def at_least(m):
            ans = 0
            i = 0
            cc = 0
            v_counts = Counter()
            for j in range(n):
                if word[j] in v:
                    v_counts[word[j]] += 1
                else:
                    cc += 1
                while len(v_counts) == 5 and cc >= m:
                    if word[i] in v_counts:
                        v_counts[word[i]] -= 1
                        if v_counts[word[i]] == 0:
                            del v_counts[word[i]]
                    else:
                        cc -= 1
                    i += 1
                ans += i

            return ans
        
        return at_least(k) - at_least(k + 1)           