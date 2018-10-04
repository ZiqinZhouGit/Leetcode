# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        pointer_A = headA
        pointer_B = headB
        while pointer_A is not pointer_B:
            # pointer_A = headB if pointer_A is None else pointer_A.next
            # pointer_B = headA if pointer_B is None else pointer_B.next
            if pointer_A is None:
                pointer_A = headB
            else:
                pointer_A = pointer_A.next
            if pointer_B is None:
                pointer_B = headA
            else:
                pointer_B = pointer_B.next
            
        return pointer_A
