class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split()
        m = discount/100
        for i, word in enumerate(s):
            if word[0]=="$" and word[1:].isdigit():
                num = int(word[1:])*(1-m)
                w = "$"+"{:.2f}".format(num)
                s[i]=w
        return " ".join(s)