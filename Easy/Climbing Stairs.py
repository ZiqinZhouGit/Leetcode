class Solution(object):
    def climbStairs(self, n):
        return self.construct(n)
        
    def construct(self, n):
        record = [1, 1]
        i = 2
        while i <= n:
            record.append(record[i-1] + record[i-2])
            i += 1
        return record[n]
