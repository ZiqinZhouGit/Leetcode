class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # max_list = [1]*len(nums)
        # # print(max_list)
        # for i in range(len(nums)):
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             max_list[i] = max(max_list[j] + 1, max_list[i])
        #             if max_list[i] >= 3:
        #                 return True
        # return False
        
        first = second = float('inf')
        for n in nums:
            if n < first:
                first = n
            elif first<n<second:
                second = n
            elif n > second:
                return True
        return False
