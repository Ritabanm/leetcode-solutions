class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        times = []
        for i in range(len(processorTime)):
            times.append(processorTime[i] + tasks[i*4])
        return max(times)