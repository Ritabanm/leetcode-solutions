class Solution:
    def reorderSpaces(self, text: str) -> str:
        b=text.split()
        count=0
        for i in text:
            if i==' ':
                count+=1
        if len(b)>1:
            a=count//(len(b)-1)
        else:
            a=count
        s=''
        j=0
        while j<len(b)-1:
            s+=b[j]
            s+=' '*a
            count-=a
            j+=1
        s+=b[-1]
        s+=' '*count
        return s




        