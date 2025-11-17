class Solution:
    def scoreOfStudents(self, s, answers):
        dict1 = {}

        def function(s):
            if s.isdigit():
                return {int(s)}

            if s in dict1:
                return dict1[s]

            res = set()

            for i in range(len(s)):
                if s[i] in {"+","*"}:
                    for left in function(s[:i]):
                        for right in function(s[i+1:]):
                            if s[i] == "+" and left + right <= 1000:
                                res.add(left+right)
                            if s[i] == "*" and left*right <= 1000:
                                res.add(left*right)

            dict1[s] = res 

            return res 

        ans, val, total = function(s), eval(s), 0

        for i in answers:
            if i == val:
                total += 5 
            elif i in ans:
                total += 2 

        return total 