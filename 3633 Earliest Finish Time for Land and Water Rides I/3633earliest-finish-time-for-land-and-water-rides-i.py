class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        time = float('inf')
        for lstart, ldur in zip(landStartTime, landDuration):
            lend = lstart + ldur
            for wstart, wdur in zip(waterStartTime, waterDuration):
                wend = wstart + wdur
                time = min(time, min(max(wstart, lend) + wdur, max(lstart, wend) + ldur))
        return time