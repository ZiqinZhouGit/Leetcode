class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        i = 0
        while i < len(nums) - 2:
            #########also works#########
            # if i > 0 and nums[i] == nums[i - 1] and i < len(nums) - 2:
            #     i += 1
            #     continue 
            #############################
            while i > 0 and nums[i] == nums[i-1] and i < len(nums) -2:
                i += 1
            j = i + 1
            k = len(nums) - 1
            partial_sum = - nums[i]
            while j < k:
                if nums[j] + nums[k] == partial_sum:
                    results.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -+ 1
                elif nums[j] + nums[k] < partial_sum:
                    j += 1
                else:
                    k -= 1
            i += 1
        return results
