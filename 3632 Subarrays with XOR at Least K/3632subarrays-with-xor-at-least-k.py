class Solution:
    def countXorSubarrays(self, nums: List[int], k: int) -> int:

        m = max(1, max(nums + [k]).bit_length())
        # print(m)

        ans = 0

        trie = {}
        sk = bin(k)[2:].zfill(m)

        # larger indicates previous digits already satisfy >= k
        def helper(i, node, larger):
            if not node:
                return 0
            if i == m or larger:
                return node.get('cnt', 0)

            if sk[i] == '1':
                nei = '0' if cur[i] == '1' else '1'
                return helper(i + 1, node.get(nei, {}), larger)
            else:
                return helper(i + 1, node.get('1', {}), larger or cur[i] == '0') + helper(i + 1, node.get('0', {}),
                                                                                        larger or cur[i] == '1')

        prefix = 0
        node = trie
        for _ in range(m):
            node = node.setdefault('0', {})
            node['cnt'] = node.get('cnt', 0) + 1

        for num in nums:

            prefix ^= num
            cur = bin(prefix)[2:].zfill(m)
            ans += helper(0, trie, False)

            node = trie
            for d in cur:
                node = node.setdefault(d, {})
                node['cnt'] = node.get('cnt', 0) + 1
        
        return ans

            