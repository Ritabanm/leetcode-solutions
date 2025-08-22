class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        str=" ".join(sentence)+" "
        valid_space=0
        for i in range(rows):
            valid_space+=cols
            if str[valid_space%len(str)]==" ":
                valid_space+=1
            else:
                while valid_space>0 and str[valid_space%len(str)-1]!=" ":
                    valid_space-=1
        return valid_space//len(str)