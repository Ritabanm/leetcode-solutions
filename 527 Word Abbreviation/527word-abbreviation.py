from copy import copy

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:

        abbreviate = lambda x: ''.join((x[:level],str(len(x)-level-1),x[-1]))
        d, e, idx  = defaultdict(list), defaultdict(list), dict(map(reversed,enumerate(words)))
        level = 1

        for word in words:                          #   abbreviate all words with length > 3
            if len(word) > 3:                       #   and write to dict w/ abv as keys    
                d[abbreviate(word)].append(word)

        while d:                                    #   iterate as long as abvs are not unique
            level+= 1
            e.clear()

            for abv in d:                           #   if abv is unique, write it to words 
                if len(d[abv]) == 1:
                    word = d[abv][0]
                    words[idx[word]] = abv

                elif len(abv)+1 == len(d[abv][0]):  #   if abv length not less than word length,
                    continue                        #   leave word in words

                else:                               # if not unique, update abvs and iterate again
                    for word in d[abv]:
                        e[abbreviate(word)].append(word)

            d = copy(e)       

        return words