class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        mx = max(damage)
        if mx>=armor:
            return sum(damage)-armor+1
        else:
            return sum(damage)-mx+1