# 146. LRU Cache - Solution Analysis

## Problem Understanding
Design a cache with fixed capacity that evicts the least recently used item when full. `get(key)` returns the value and marks the key as recently used; `put(key, value)` inserts or updates a key and marks it as recently used, evicting the LRU key if capacity is exceeded. Both operations must run in O(1) average time. Capacity is positive (1–3000), keys and values are non-negative, and up to 2·10⁵ calls are made.

## Approach
The solution uses a **hash map + doubly linked list** pattern. The hash map (`cache`) provides O(1) key-to-node lookup. The doubly linked list maintains usage order: the dummy `left` node sits before the LRU item, the dummy `right` node sits after the MRU item. Moving a node to MRU or evicting the LRU node are both O(1) pointer manipulations. Brute force (e.g., a list with linear search for LRU) would be O(n) per operation; the chosen structure achieves O(1) for both `get` and `put`.

**Key insight:** A doubly linked list with sentinel nodes lets you remove any known node and insert at the tail in constant time, while the hash map lets you find that node in constant time.

## Algorithm
1. **Initialisation**: Create `cache` dict, dummy `left` (LRU sentinel) and `right` (MRU sentinel) nodes, link them together.
2. **`get(key)`**:
   - If key absent, return -1.
   - Retrieve node from `cache`.
   - Unlink node from its current position (`node.prev.next = node.next; node.next.prev = node.prev`).
   - Insert node just before `right` (MRU position).
   - Return `node.value`.
3. **`put(key, value)`**:
   - If key exists, unlink the existing node from the list (the old node will be garbage-collected).
   - Create a new `Node(key, value)`, store it in `cache[key]`.
   - Insert the new node at MRU position (before `right`).
   - If `len(cache) > capacity`: remove `left.next` (the LRU node) from the list and delete its key from `cache`.

## Line-by-Line Explanation
- `class Node:`: Doubly linked list node storing key, value, prev, next pointers.
- `self.capacity = capacity`: Store the maximum number of entries.
- `self.cache = {}`: Hash map key → Node for O(1) lookup.
- `self.left = Node(); self.right = Node()`: Dummy head (LRU side) and dummy tail (MRU side).
- `self.left.next = self.right; self.right.prev = self.left`: Initialise empty list with sentinels pointing to each other.
- `if key not in self.cache: return -1`: Fast miss path.
- `node = self.cache[key]`: Retrieve the node to promote.
- `node.prev.next = node.next; node.next.prev = node.prev`: Splice node out of its current position.
- `prev = self.right.prev`: Node currently at MRU (just before dummy tail).
- `prev.next = node; node.prev = prev; node.next = self.right; self.right.prev = node`: Insert node as new MRU.
- `return node.value`: Return the stored value.
- `if key in self.cache:`: Key already present → update.
- `node = self.cache[key]`: Get existing node.
- `node.prev.next = node.next; node.next.prev = node.prev`: Remove old node from list.
- `node = Node(key, value); self.cache[key] = node`: Create fresh node and update map reference.
- `prev = self.right.prev; prev.next = node; node.prev = prev; node.next = self.right; self.right.prev = node`: Insert new node at MRU.
- `if len(self.cache) > self.capacity:`: Capacity exceeded after insertion.
- `lru = self.left.next`: The real LRU node (first after dummy head).
- `self.left.next = lru.next; lru.next.prev = self.left`: Unlink LRU node from list.
- `del self.cache[lru.key]`: Remove evicted key from hash map.

## Dry Run
Example from the problem: capacity = 2.

| Step | Op | key | value | cache keys (LRU→MRU) | List (left→right) | Action |
|------|----|-----|-------|----------------------|-------------------|--------|
| 1 | put | 1 | 1 | [1] | left ↔ 1 ↔ right | insert 1 at MRU |
| 2 | put | 2 | 2 | [1, 2] | left ↔ 1 ↔ 2 ↔ right | insert 2 at MRU |
| 3 | get | 1 | – | [2, 1] | left ↔ 2 ↔ 1 ↔ right | move 1 to MRU, return 1 |
| 4 | put | 3 | 3 | [1, 3] | left ↔ 1 ↔ 3 ↔ right | evict LRU (2), insert 3 at MRU |
| 5 | get | 2 | – | [1, 3] | left ↔ 1 ↔ 3 ↔ right | miss, return -1 |
| 6 | put | 4 | 4 | [3, 4] | left ↔ 3 ↔ 4 ↔ right | evict LRU (1), insert 4 at MRU |
| 7 | get | 1 | – | [3, 4] | left ↔ 3 ↔ 4 ↔ right | miss, return -1 |
| 8 | get | 3 | – | [4, 3] | left ↔ 4 ↔ 3 ↔ right | move 3 to MRU, return 3 |
| 9 | get | 4 | – | [3, 4] | left ↔ 3 ↔ 4 ↔ right | move 4 to MRU, return 4 |

## Complexity
- **Time**: O(1) average for both `get` and `put`. Hash map lookup/insert/delete are O(1) average; linked list pointer updates are O(1) worst-case.
- **Space**: O(capacity) for the hash map and the nodes. At most `capacity` nodes exist simultaneously.

## Edge Cases
- **Capacity = 1**: `put` evicts the only existing item on every new insertion; `get` promotes the sole item (no-op). Handled correctly because `left.next` and `right.prev` point to the same node.
- **Repeated `put` on same key**: Old node is unlinked and replaced; map reference updated; no memory leak in Python (old node becomes unreachable).
- **`get` on non-existent key**: Returns -1 without modifying structure.
- **Maximum operations (2·10⁵)**: O(1) per call ensures it fits time limits.
- **Key/value at constraint boundaries (0, 10⁴, 10⁵)**: No special handling needed; integers work as dict keys.

## Possible Improvements
- **Reuse node on update**: In `put`, when `key in self.cache`, update `node.value = value` and move the existing node to MRU instead of allocating a new `Node`. Saves allocations and avoids momentarily having two nodes for the same key in the map (though the old one is immediately orphaned).
- **Extract helper methods**: `_remove(node)` and `_insert_at_mru(node)` would reduce duplication between `get` and `put` and make pointer logic easier to audit.
- **Type hints**: Add `-> None` to `put` and `-> int` to `get` (already present) and `Node` attributes for static analysis.
- The solution is already asymptotically optimal for the given constraints; the above are code-quality refinements, not complexity improvements.

---

_Generated by leetvault using nvidia (nvidia/nemotron-3-ultra-550b-a55b)_
