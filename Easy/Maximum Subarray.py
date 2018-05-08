class Solution(object):
    def maxSubArray(self, nums): 
        if len(nums) < 2:
            return nums[0]
        else:
            i = 1
            records = [nums[0]]
            while i < len(nums):
                if records[i-1] >= 0:
                    records.append(records[i-1] + nums[i])
                else:
                    records.append(nums[i])
                i += 1
        return max(records)
