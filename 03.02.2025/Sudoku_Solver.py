class Solution:
    def solveSudoku(self, board):
        # Precompute rows, columns, and subgrids to track used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        empty_cells = []

        # Initialize sets and collect all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))  # Track empty cells
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[(r // 3) * 3 + (c // 3)].add(num)

        # Helper function to check validity
        def is_valid(num, r, c):
            subgrid_idx = (r // 3) * 3 + (c // 3)
            return num not in rows[r] and num not in cols[c] and num not in subgrids[subgrid_idx]

        # Backtracking function
        def backtrack():
            if not empty_cells:
                return True  # Solved

            # Prioritize cell with the fewest possible numbers
            empty_cells.sort(key=lambda x: len(possible_values(x[0], x[1])))
            r, c = empty_cells.pop(0)

            for num in map(str, range(1, 10)):
                if is_valid(num, r, c):
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[(r // 3) * 3 + (c // 3)].add(num)

                    # Continue solving
                    if backtrack():
                        return True

                    # Undo the placement
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    subgrids[(r // 3) * 3 + (c // 3)].remove(num)

            empty_cells.insert(0, (r, c))  # Backtrack to the current cell
            return False

        # Helper function to compute possible values for a cell
        def possible_values(r, c):
            subgrid_idx = (r // 3) * 3 + (c // 3)
            return set(map(str, range(1, 10))) - rows[r] - cols[c] - subgrids[subgrid_idx]

        # Start solving
        backtrack()
