class Solution(object):
    def pourWater(self, H, V, K):
        for _ in range(V):
            for d in (-1, 1):
                i = best = K
                while 0 <= i+d < len(H) and H[i+d] <= H[i]:
                    if H[i+d] < H[i]: best = i+d
                    i += d
                if best != K:
                    H[best] += 1
                    break
            else:
                H[K] += 1
        return H