class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        winning = 0
        hashmap ={ Id:[0]*11 for Id in range(n)}
        for Id, color in pick:
            hashmap[Id][color]+=1
        for Id in range(n):
            if (max(hashmap[Id])>Id): winning+=1
        return winning
        