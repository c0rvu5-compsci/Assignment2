grid: list[list[str]] = [
    [" ", "█", "█", "█", "█", "█"],
    [" ", " ", " ", " ", " ", " "],
    [" ", "█", "█", " ", "█", "█"],
    [" ", "█", "█", "B", "█", "█"],
    [" ", "█", " ", " ", "█", "█"],
    [" ", "█", " ", "█", "█", "█"],
    ["A", " ", " ", "█", "█", "█"],
]

dls_grid_explored: list[list[int]] = []
dls_grid_frontier: list[list[int]] = []


def dls_grid(location: list[int], end: str, rows: int, cols: int, depth: int) -> bool:
    dls_grid_explored.append(location)

    if grid[location[0]][location[1]] == end:
        return True

    if depth == 0:
        return False

    directions: list[list[int]] = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for direction in directions:
        next_location = [location[0] + direction[0], location[1] + direction[1]]

        if (
            0 <= next_location[0] < rows
            and 0 <= next_location[1] < cols
            and grid[next_location[0]][next_location[1]] != "█"
            and next_location not in dls_grid_explored
        ):
            dls_grid_frontier.append(next_location)

        if dls_grid_frontier:
            next_location = dls_grid_frontier.pop()
            return dls_grid(next_location, end, rows, cols, depth-1)

    return False


if dls_grid([6, 0], "B", 7, 6, 6):
    print(f"DLS Grid Depth 6: {dls_grid_explored}")
else:
    print("No solution found")
dls_grid_explored.clear()

if dls_grid([6, 0], "B", 7, 6, 10):
    print(f"DLS Grid Depth 10: {dls_grid_explored}")
else:
    print("No solution found")

"""
In theory the two runs should return different answer using DFS with their respective limitations. Based on the DFS search from Q1 that this DLS is based on, it should never
have reached the goal, while the depth 10 search should have. If they both reached the goal (maybe with longer depths) the longer depth search is likely to have a less efficient route to
the shorter depth search because it has more leeway in its path. In comparison to the DFS and BFS searches, this one is more efficient because there's no unnecessary memory use due to the limiter.
"""
