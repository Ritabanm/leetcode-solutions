class Solution:
    def numSimilarGroups(self, strs):
        parent = {s: s for s in strs}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def are_similar(word1, word2):
            return sum(a != b for a, b in zip(word1, word2)) <= 2

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if are_similar(strs[i], strs[j]):
                    union(strs[i], strs[j])

        return len(set(find(word) for word in strs))
