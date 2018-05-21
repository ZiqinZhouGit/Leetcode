class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def scan(string, start, end):
            while start >= 0 and end < len(string) and string[start] == string[end]:
                start -= 1
                end += 1
            return string[start + 1: end]
        res = ''
        
        for i in range(len(s)):
            res = max(scan(s,i,i), scan(s,i,i+1), res, key=len)

        return res
