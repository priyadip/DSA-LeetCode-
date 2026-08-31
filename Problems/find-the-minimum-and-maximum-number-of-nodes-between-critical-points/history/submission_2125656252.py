# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            # Check if curr is a local maximum or minimum
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = curr.next
            pos += 1

        # Fewer than two critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]       