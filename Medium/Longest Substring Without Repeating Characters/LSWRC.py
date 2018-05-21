class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        start = 0
        end = 0
        max_length = 0
        
        while end < len(s):
            if len(set(s[start:end + 1])) != len(s[start:end + 1]):
                start += 1
            
            temp_length = end - start + 1
    
            if temp_length > max_length:
                max_length = temp_length
            end += 1
        return max_length
