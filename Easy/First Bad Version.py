class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        else:
            return end
