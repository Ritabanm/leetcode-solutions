class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        ans = -1

        for i in range(len(sensor1) - 1):
            if sensor1[i] == sensor2[i]:
                continue
            elif sensor1[i] == sensor2[i + 1] and sensor2[i] != sensor1[i + 1]:
                return 1
            elif sensor2[i] == sensor1[i + 1] and sensor1[i] != sensor2[i + 1]:
                return 2
            else:
                continue

        return ans