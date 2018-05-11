class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.value = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.value.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        del self.value[-1]
        # self.value.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.value[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.value)
