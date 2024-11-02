from collections import defaultdict
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = {char: 0 for word in words for char in word}

        # Build the graph
        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    indegree[c2] += 1
                    break
            else:
                if len(word1) > len(word2):  # Invalid case (e.g., ["abc", "ab"])
                    return ""

        # Topological sorting using Kahn's Algorithm (BFS)
        queue = [char for char in indegree if indegree[char] == 0]
        order = []

        while queue:
            char = queue.pop(0)
            order.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(order) if len(order) == len(indegree) else ""
