class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        s=0
        curr=0
        for i in range(len(gas)):
            curr+=gas[i]-cost[i]
            if curr<0:
                s=i+1
                curr=0
        return s