class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] += 1
        count = 0
        flag = 0
        while True:
            if flag:
                break
            for i in target:
                if hashmap[i] == 0:
                    flag = 1
                    break
                hashmap[i] -= 1
            count += 1
        return count-1