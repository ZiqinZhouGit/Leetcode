class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) < 3:
            return max(nums)
        n = 2
        records = [nums[0], max(nums[0],nums[1])]
        while n < len(nums):
            records.append(max(records[n-1], records[n-2] + nums[n]))
            n += 1
        return records[-1]
