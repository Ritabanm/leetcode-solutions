class Solution:
    def highFive(self, items):
        d = defaultdict(list)
        for i in items:
            d[i[0]].append(i[1])
        return ([[key, int(sum(sorted(d[key], reverse = True)[:5])/5)]for key in sorted(d.keys())])
        