class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def transfer(string):
            temp = list(string)       
            temp.sort()
            # print(temp)
            return ''.join(temp)
    
        record = {}
        for s in strs:
            rec_stand = transfer(s)
            if rec_stand in record:
                record[rec_stand].append(s)
            else:
                record[rec_stand] = [s]
        
        res = []
        for rec_key in record:
            res.append(record[rec_key])
        return res
