class Solution:
    def checkTwoChessboards(self, cordonnes1: str, cordonnes2: str) -> bool:
       return (ord(cordonnes1[0])+ord(cordonnes2[0])+int(cordonnes1[1])+int(cordonnes2[1]))%2==0