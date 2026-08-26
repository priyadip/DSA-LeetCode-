# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Get length
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head

        size = 1

        while size < n:
            prev = dummy
            curr = dummy.next

            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)

                # Merge left and right
                while left and right:
                    if left.val <= right.val:
                        prev.next = left
                        left = left.next
                    else:
                        prev.next = right
                        right = right.next

                    prev = prev.next

                prev.next = left or right

                while prev.next:
                    prev = prev.next

            size *= 2

        return dummy.next

    def split(self, head, size):
        if not head:
            return None

        for _ in range(size - 1):
            if head.next:
                head = head.next
            else:
                break

        second = head.next
        head.next = None

        return second
        