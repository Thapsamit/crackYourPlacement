class Solution:
    def canCompleteCircuit(self, gas, cost):
        curr = 0
        si = 0
        if sum(gas)<sum(cost):
            return -1
        for i in range(0,len(gas),1):
            curr+=(gas[i]-cost[i])
            if curr<0:
                curr = 0
                si = i+1
        return si
        