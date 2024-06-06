from collections import Counter
class Solution:
    def findCommonResponse(self, response):
        freq = Counter()
        for day in response:
            unique_responses =set(day)
            freq.update(unique_responses)
        return min(freq.items(), key = lambda x:(-x[1], x[0]))[0]