class Solution:
    def capitalizeTitle(self, title: str) -> str:
        output = []
        title = title.split()
        for i in title:
            if len(i)>2:
                i = i.capitalize()
            elif len(i)<=2:
                i  = i.lower()
            output.append(i)
        return ' '.join(output)