from sortedcontainers import SortedList

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        counts = Counter()
        store = SortedList()

        def add(g):
            store.add(g)
            key = width(g)
            counts[key] += 1
        
        def remove(g):
            # print(g)
            # if g not in store:
            #     exit()
            store.remove(g)
            key = width(g)
            counts[key] -= 1
            if counts[key] == 0:
                del counts[key]

        def init():
            i = 0
            groups = []
            while i < len(colors):
                l = i
                while i+1 < len(colors) and colors[i] != colors[i+1]:
                    i += 1
                r = i
                groups.append((l, r))
                i += 1
            if colors[-1] != colors[0] and len(groups) > 1:
                groups[0] = (groups[-1][0], groups[0][1])
                groups.pop()
            for g in groups:
                add(g)
        
        def merge(x):
            if i == 0 and store[i][0] > i:
                i = len(store) - 1
            g1 = store[i]
            g2 = store[(i+1) % len(store)]
            remove(g1)
            remove(g2)
            add((g1[0], g2[1]))
        
        def at(x):
            return colors[x % n]
        
        def group(x):
            x %= n
            i = store.bisect_right((x, inf)) - 1
            return store[i % len(store)]
        
        def width(g):
            l, r = g
            if l > r:
                l -= n
            return (r-l+1)

        init()
        ans = []
        for q in queries:
            # print(colors)
            # print(store)
            if q[0] == 1:
                size = q[1]
                total = 0
                # print(counts)
                for k, v in counts.items():
                    if k == n and n % 2 == 0:
                        total += n
                    elif k >= size:
                        total += v * (k - size + 1)
                ans.append(total)
            else:
                x, c = q[1:]
                if c == at(x):
                    continue
                g = group(x)
                if at(x-1) != at(x) and at(x) != at(x+1):
                    remove(g)
                    add((x, x))
                    if width(g) == n and n % 2 == 0:
                        add(((x+1)%n, (x-1)%n))
                    else:
                        add((g[0], (x-1)%n))
                        add(((x+1)%n, g[1]))
                elif at(x-1) != at(x):
                    g1 = group(x+1)
                    remove(g)
                    if g1 == g:
                        add((x, (x-1)%n))
                    else:
                        remove(g1)
                        add((g[0], (x-1)%n))
                        add((x, g1[1]))
                elif at(x) != at(x+1):
                    g1 = group(x-1)
                    remove(g)
                    if g1 == g:
                        add(((x+1)%n, x))
                    else:
                        remove(g1)
                        add((g1[0], x))
                        add(((x+1)%n, g[1]))
                else:
                    g1 = group(x-1)
                    g2 = group(x+1)
                    remove(g)
                    remove(g1)
                    if g1 == g2:
                        add((0, n-1))
                    else:
                        remove(g2)
                        add((g1[0], g2[1]))
                colors[x] = c
        return ans