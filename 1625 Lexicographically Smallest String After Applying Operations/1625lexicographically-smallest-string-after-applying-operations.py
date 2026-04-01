class Solution:
    def findLexSmallestString(self, s, a, b):
        n = len(s)

        stack, min_val, visited = [s], s, {s}

        while stack:
            node = stack.pop(0)

            min_val, str1 = min(min_val,node), ""

            for i in range(n):
                if i%2 == 1:
                    str1 += str((int(node[i])+a)%10) 
                else:
                    str1 += node[i]

            if str1 not in visited:
                stack.append(str1)
                visited.add(str1)

            str2 = node[-b:] + node[:-b]

            if str2 not in visited:
                stack.append(str2)
                visited.add(str2)

        return min_val