class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # map of word to a set of synonyms, including itself
        smap = {}
        for s, t in synonyms:
            if s in smap and t in smap:
                merged = smap[s].union(smap[t])
                for w in merged:
                    smap[w] = merged
            elif s in smap:
                smap[s].add(t)
                smap[t] = smap[s]
            elif t in smap:
                smap[t].add(s)
                smap[s] = smap[t]
            else:
                smap[s] = set([s, t])
                smap[t] = smap[s]

        wl = text.split(' ')
        lines = [wl]
        for i in range(len(wl)):
            word = wl[i]
            if word in smap:
                newLines = []
                for s in smap[word]:
                    if s != word:
                        newLines += [line[:i]+[s]+line[i+1:] for line in lines]
                lines += newLines
        return list(sorted([' '.join(line) for line in lines]))