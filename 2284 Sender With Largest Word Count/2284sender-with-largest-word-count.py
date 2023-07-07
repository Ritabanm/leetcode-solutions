class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counts = {}
        for m, s in zip(messages, senders):
            counts[s]= counts.get(s,0) + m.count(' ') + 1
        return max(counts.items(), key = lambda x:(x[1], x[0]))[0]