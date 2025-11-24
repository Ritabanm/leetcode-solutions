class Solution:
    def findDelayedArrivalTime(self, arrival_time, delayed_time):
        return (arrival_time + delayed_time) % 24