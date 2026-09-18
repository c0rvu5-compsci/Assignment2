class treeNode:
    name: str
    l_child: "treeNode | None"
    r_child: "treeNode | None"

    def __init__(self, name: str):
        self.name = name
        self.l_child = None
        self.r_child = None


dfs_frontier: list[treeNode] = []
dfs_explored: list[treeNode] = []

bfs_frontier: list[treeNode] = []
bfs_explored: list[treeNode] = []

b_grid_frontier: list[list[int]] = []
b_grid_explored: list[list[int]] = []

d_grid_frontier: list[list[int]] = []
d_grid_explored: list[list[int]] = []


node_a = treeNode(name="A")
node_b = treeNode(name="B")
node_c = treeNode(name="C")
node_d = treeNode(name="D")
node_e = treeNode(name="E")
node_f = treeNode(name="F")
node_g = treeNode(name="G")

node_a.l_child = node_b
node_b.l_child = node_c
node_b.r_child = node_d
node_c.l_child = node_e
node_d.l_child = node_f


def dfs(node: treeNode, goal: str) -> bool:
    dfs_explored.append(node)
    if node.name == goal:
        return True
    if node.r_child:
        dfs_frontier.append(node.r_child)
    if node.l_child:
        dfs_frontier.append(node.l_child)
    if dfs_frontier:
        next_node = dfs_frontier.pop()
        return dfs(next_node, goal)
    return False


def bfs(node: treeNode, goal: str) -> bool:
    bfs_explored.append(node)
    if node.name == goal:
        return True
    if node.l_child:
        bfs_frontier.append(node.l_child)
    if node.r_child:
        bfs_frontier.append(node.r_child)
    if bfs_frontier:
        next_node = bfs_frontier[0]
        bfs_frontier.remove(bfs_frontier[0])
        return bfs(next_node, goal)
    return False


path = dfs(node_a, "E")

if path:
    print(f"Depth-First Search: {[node.name for node in dfs_explored]}")
else:
    print("No path found for DFS")

path = bfs(node_a, "E")

if path:
    print(f"Breadth-First Search: {[node.name for node in bfs_explored]}")
else:
    print("No path found for BFS")


grid: list[list[str]] = [
    [" ", "█", "█", "█", "█", "█"],
    [" ", " ", " ", " ", " ", " "],
    [" ", "█", "█", " ", "█", "█"],
    [" ", "█", "█", "B", "█", "█"],
    [" ", "█", " ", " ", "█", "█"],
    [" ", "█", " ", "█", "█", "█"],
    ["A", " ", " ", "█", "█", "█"],
]


def dfs_grid(location: list[int], end: str, rows: int, cols: int) -> bool:
    d_grid_explored.append(location)
    if grid[location[0]][location[1]] == end:
        return True
    directions: list[list[int]] = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for direction in directions:
        next_location = [location[0] + direction[0], location[1] + direction[1]]
        if (
            0 <= next_location[0] < rows
            and 0 <= next_location[1] < cols
            and grid[next_location[0]][next_location[1]] != "█"
            and next_location not in d_grid_explored
        ):
            d_grid_frontier.append(next_location)
    if d_grid_frontier:
        next_location = d_grid_frontier.pop()
        return dfs_grid(next_location, end, rows, cols)
    return False


def bfs_grid(location: list[int], end: str, rows: int, cols: int) -> bool:
    b_grid_explored.append(location)
    if grid[location[0]][location[1]] == end:
        return True
    directions: list[list[int]] = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for direction in directions:
        next_location = [location[0] + direction[0], location[1] + direction[1]]
        if (
            0 <= next_location[0] < rows
            and 0 <= next_location[1] < cols
            and grid[next_location[0]][next_location[1]] != "█"
            and next_location not in b_grid_explored
        ):
            b_grid_frontier.append(next_location)
    if b_grid_frontier:
        next_location = b_grid_frontier[0]
        b_grid_frontier.remove(next_location)
        return bfs_grid(next_location, end, rows, cols)
    return False


dfs_grid([6, 0], "B", 7, 6)
bfs_grid([6, 0], "B", 7, 6)
print(f"DFS Grid: {d_grid_explored}")
print(f"BFS Grid: {b_grid_explored}")


"""
Based on the given outputs of BFS / DFS, the differences are clear. BFS will typically find the quicker path, so long as memory allows. That is the main constraint for DFS,
because it is keeping track of more locations, it takes more memory. Meanwhile, DFS will find the first available path which is handy when efficiency of traversal isn't 
a factor that needs considering, for example smaller trees/grids as opposed to BFS with things the scale of Google maps or certain larger grids for chess or crosswords.
"""
