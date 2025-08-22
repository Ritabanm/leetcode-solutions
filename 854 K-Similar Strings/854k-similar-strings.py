class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        ans = 0
        seen = {s1}
        queue = deque([s1])
        while queue: 
            for _ in range(len(queue)): 
                s = queue.popleft()
                if s == s2: return ans 
                for i in range(len(s)): 
                    if s[i] != s2[i]: 
                        for j in range(i+1, len(s)): 
                            if s[j] != s2[j] and s[j] == s2[i]: 
                                ss = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                                if ss not in seen: 
                                    seen.add(ss)
                                    queue.append(ss)
                        break
            ans += 1