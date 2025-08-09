class Solution:
    def equalCountSubstrings(self, s, count):
        def dfs(s,width):
            n, left, dict1, result = len(s), 0, defaultdict(int), 0 

            for right in range(n):
                dict1[s[right]] += 1 

                if right-left+1 > width:
                    dict1[s[left]] -= 1 

                    if dict1[s[left]] == 0:
                        del dict1[s[left]]

                    left += 1 

                if right-left + 1 == width and all([val == count for val in dict1.values()]):
                    result += 1 

            return result 

        total = 0 

        for i in range(1,27):
            total += dfs(s,i*count)

        return total






        