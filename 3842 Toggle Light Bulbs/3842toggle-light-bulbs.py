class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()
        for x in bulbs:
            if x in on:
                on.remove(x)
            else:
                on.add(x)
        return sorted(on)