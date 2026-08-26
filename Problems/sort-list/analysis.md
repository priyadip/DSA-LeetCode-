# 148. Sort List - Solution Analysis

## Problem Understanding
Sort a singly linked list in ascending order. The input is the head node (possibly `None`). The output is the head of the sorted list. The list length is up to 5·10⁴, values range from -10⁵ to 10⁵. An O(n²) algorithm would be too slow; the follow-up asks for O(n log n) time and O(1) extra space, which points to an in-place merge sort.

## Approach
**Bottom-up (iterative) merge sort** on a linked list.  
Brute force would copy values to an array, sort, and rebuild (O(n log n) time, O(n) space). Insertion sort on the list gives O(1) space but O(n²) time. Bottom-up merge sort achieves O(n log n) time and O(1) space by repeatedly merging adjacent sorted sublists of increasing size (1, 2, 4, …). The key insight is that merging two sorted linked lists can be done in-place with only pointer manipulation, and doubling the sublist size each pass guarantees logarithmic passes.

## Algorithm
1. If `head` is `None` or `head.next` is `None`, return `head`.
2. Traverse once to compute the length `n`.
3. Create a dummy node pointing to `head` to simplify head updates.
4. Initialize `size = 1`.
5. While `size < n`:
   a. Set `prev = dummy`, `curr = dummy.next`.
   b. While `curr` is not `None`:
        - `left = curr`.
        - `right = split(left, size)` – cuts off the first `size` nodes, returns head of the next part.
        - `curr = split(right, size)` – cuts off the next `size` nodes, returns head of the following pair.
        - Merge `left` and `right`:
            * While both `left` and `right` exist, attach the smaller node to `prev.next` and advance that list and `prev`.
        - Attach the remaining non-empty list (`left` or `right`) to `prev.next`.
        - Advance `prev` to the end of the merged segment (`while prev.next: prev = prev.next`).
   c. Double `size` (`size *= 2`).
6. Return `dummy.next`.

`split(head, size)` advances `head` by `size-1` steps (or until the end), disconnects the list at that point, and returns the head of the second part.

## Line-by-Line Explanation
- `if not head or not head.next: return head` – base cases: empty or single-node list.
- `n = 0; curr = head; while curr: n += 1; curr = curr.next` – compute list length.
- `dummy = ListNode(0); dummy.next = head` – dummy node avoids special handling of the head.
- `size = 1` – start with sublists of length 1.
- `while size < n:` – outer loop: each pass merges pairs of sublists of current `size`.
- `prev = dummy; curr = dummy.next` – `prev` tracks the tail of the already-merged portion; `curr` is the start of the next pair.
- `while curr:` – inner loop: process each pair of sublists.
- `left = curr` – first sublist of length `size`.
- `right = self.split(left, size)` – split after `size` nodes; `right` becomes the second sublist.
- `curr = self.split(right, size)` – split after another `size` nodes; `curr` becomes the start of the next pair.
- `while left and right:` – standard merge of two sorted lists.
- `if left.val <= right.val: prev.next = left; left = left.next` – attach smaller node.
- `else: prev.next = right; right = right.next` – attach smaller node.
- `prev = prev.next` – advance tail pointer.
- `prev.next = left or right` – attach the remaining sorted tail.
- `while prev.next: prev = prev.next` – move `prev` to the true end of the merged segment.
- `size *= 2` – double sublist size for next pass.
- `return dummy.next` – sorted list head.
- `split` function: advances `head` `size-1` times (or until end), saves `second = head.next`, sets `head.next = None`, returns `second`.

## Dry Run
Example: `head = [4,2,1,3]` (n=4)

| Pass | size | left segment | right segment | curr (next pair) | Merged segment | List after pass |
|------|------|--------------|---------------|------------------|----------------|-----------------|
| 1    | 1    | 4            | 2             | 1                | 2→4            | 2→4→1→3         |
| 1    | 1    | 1            | 3             | None             | 1→3            | 2→4→1→3         |
| 2    | 2    | 2→4          | 1→3           | None             | 1→2→3→4        | 1→2→3→4         |
| 3    | 4    | –            | –             | –                | –              | stop (size ≥ n) |

Final result: `1→2→3→4`.

## Complexity
- **Time:** O(n log n). The outer loop runs ⌈log₂ n⌉ times. Each pass visits every node once during splitting and merging, so O(n) per pass.
- **Space:** O(1). Only a constant number of pointers (`dummy`, `prev`, `curr`, `left`, `right`, `size`, `n`) are used; the list is rearranged in place.

## Edge Cases
- **Empty list:** returns `None` immediately.
- **Single node:** returns the node immediately.
- **All equal values:** merge uses `<=`, so order is preserved (stable).
- **Already sorted / reverse sorted:** still performs log n passes but each merge is linear.
- **Maximum size (5·10⁴):** O(n log n) time fits easily within limits.
- **Negative values / duplicates:** handled correctly by value comparison.

## Possible Improvements
The solution is already optimal for the given constraints (O(n log n) time, O(1) space). A minor constant-factor improvement would be to avoid the final `while prev.next: prev = prev.next` by tracking the tail of the remaining list during the merge, but this does not change the asymptotic complexity and adds code complexity. The current implementation is clean and efficient.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
