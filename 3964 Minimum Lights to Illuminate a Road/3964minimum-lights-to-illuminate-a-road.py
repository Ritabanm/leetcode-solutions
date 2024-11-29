class Solution:
    def minLights(self, lights: list[int]) -> int:


        # cnt = 0
        ran = []
        for i in range(len(lights)):

            if lights[i] != 0:
                ran.append((max(0, i - lights[i]), min(len(lights), lights[i] + i)))


        # print(ran)
        updated = []

        ran.sort()

        if ran:
            prev = ran[0]
            for j in range(1, len(ran)):
                if ran[j][0] <= prev[1]:
                    
                    prev = (min(prev[0], ran[j][0]), max(prev[1], ran[j][1]))
                    # print(j, prev)
                else:
                    updated.append(prev)
                    prev = ran[j]

            updated.append(prev)
                        
        print(updated)
        updated.sort()

        start = 0
        end = len(lights)
        cnt = 0
        sm = 0
        for i, j in updated:
            sm = 0
            if start < i:
                sm += (i - start)
            start = j + 1
            cnt += math.ceil(sm / 3)
                
        cnt += math.ceil((end - start) / 3)
        return (cnt)
            