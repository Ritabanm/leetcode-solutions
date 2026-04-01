from collections import Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue, seen = {id}, {id}
        for _ in range(level):
            queue = {j for i in queue for j in friends[i] if j not in seen}
            seen |= queue 
        freq = Counter(v for i in queue for v in watchedVideos[i])
        return sorted(freq.keys(), key=lambda x: (freq[x], x))