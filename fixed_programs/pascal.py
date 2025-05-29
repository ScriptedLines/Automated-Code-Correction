# Bug Type: Operator omission
def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = [1]
        for c in range(1, r):
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        row.append(1)
        rows.append(row)

    return rows


"""
Pascal's Triangle
pascal
 


Input:
    n: The number of rows to return

Precondition:
    n >= 1

Output:
    The first n rows of Pascal's triangle as a list of n lists

Example:
    >>> pascal(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""