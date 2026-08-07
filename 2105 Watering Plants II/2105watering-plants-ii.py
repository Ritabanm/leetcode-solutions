class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        s = 0
        e = len(plants)-1

        # remaining amounts of water
        alice_rem = capacityA
        bob_rem = capacityB
        refills = 0

        while s < e:
            if alice_rem < plants[s]:
                refills += 1
                alice_rem = capacityA
            if bob_rem < plants[e]:
                refills += 1
                bob_rem = capacityB
            alice_rem -= plants[s]
            bob_rem -= plants[e]
            s += 1
            e -= 1
        if alice_rem < plants[s] and bob_rem < plants[s] and (len(plants) % 2):
            refills += 1
        return refills