class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        prefMap = defaultdict(int)
        ans = 0
        for word in words:
            if len(word)<k:
                continue
            
            pref = word[:k]
            prefMap[pref]+=1
            if prefMap[pref]==2:ans+=1
        return ans