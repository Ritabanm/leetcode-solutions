class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        def areConnected(list1, list2):
            return len(set(list1) & set(list2)) >= k

        def dfs(node: int) -> None:
            stack = [node]

            while stack:
                node = stack.pop()

                for nei in range(n):
                    if nei not in unseen: continue
                    if areConnected(properties[node], properties[nei]):
                        unseen.remove(nei)
                        stack.append(nei)
            return


        n, ans = len(properties), 0
        unseen = set(range(n))

        while unseen:
            ans += 1
            node = unseen.pop()
            dfs(node)

        return ans