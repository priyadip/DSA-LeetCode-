class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and assign an index to every L
        start = None
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total_litter = len(litter)

        # No litter to collect
        if total_litter == 0:
            return 0

        full_mask = (1 << total_litter) - 1

        # (row, col, mask, remaining_energy, moves)
        q = deque()
        q.append((start[0], start[1], 0, energy, 0))

        # We need to remember the best energy we've had
        # for each (row, col, mask).
        #
        # If we have already reached the same state with
        # >= energy, reaching it again with less energy is useless.
        best = {}

        best[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, moves = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                if e == 0:
                    continue

                ne = e - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)

                # Reset energy immediately upon entering R
                if classroom[nr][nc] == 'R':
                    ne = energy

                # All litter collected
                if new_mask == full_mask:
                    return moves + 1

                state = (nr, nc, new_mask)

                # Only keep this state if we have more energy
                # than any previous visit with the same position/mask.
                if state not in best or ne > best[state]:
                    best[state] = ne
                    q.append((nr, nc, new_mask, ne, moves + 1))

        return -1


        