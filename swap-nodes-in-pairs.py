# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        if slow is None:
            return head

        fast = head.next

        if fast is None:
            return head

        dummy = ListNode(0)
        curr = dummy

        while True:
            if fast is not None:
                temp = ListNode(fast.val)
                curr.next = temp
                curr = curr.next

            temp = ListNode(slow.val)
            curr.next = temp
            curr = curr.next

            if fast is None or fast.next is None:
                break
            slow = slow.next.next
            fast = slow.next
        return dummy.next
