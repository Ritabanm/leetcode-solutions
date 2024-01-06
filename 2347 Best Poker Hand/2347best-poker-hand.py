class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits))==1:
            return "Flush"
        
        count = Counter(ranks)
        count = dict(sorted(count.items(), key = lambda x:x[1], reverse = True))
        print(count)
        for k, v in count.items():
            if v>2:
                return "Three of a Kind"
            if v>1:
                return "Pair"
            if v==1:
                return "High Card"