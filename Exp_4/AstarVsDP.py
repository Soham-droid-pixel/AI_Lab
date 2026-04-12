import numpy as np
import heapq
import time
from functools import lru_cache

cities = {
    0: (5, 8), 1: (1, 1), 2: (9, 2), 3: (7, 5), 4: (2, 9),
    5: (0, 4), 6: (3, 7), 7: (8, 0), 8: (4, 4), 9: (6, 1),
    10: (2, 2), 11: (5, 0), 12: (1, 6), 13: (9, 9), 14: (0, 1),
    15: (7, 8), 16: (3, 0), 17: (8, 4)
}
n = len(cities)

def get_dist(c1, c2):
    return np.linalg.norm(np.array(cities[c1]) - np.array(cities[c2]))

dist_matrix = [[get_dist(i, j) for j in range(n)] for i in range(n)]

def get_mst_weight(nodes):
    if not nodes: return 0
    nodes = list(nodes)
    visited = [False] * len(nodes)
    min_dist = [float('inf')] * len(nodes)
    min_dist[0] = 0
    mst_weight = 0
    for _ in range(len(nodes)):
        u = -1
        for i in range(len(nodes)):
            if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i
        visited[u] = True
        mst_weight += min_dist[u]
        for v in range(len(nodes)):
            d = dist_matrix[nodes[u]][nodes[v]]
            if not visited[v] and d < min_dist[v]:
                min_dist[v] = d
    return mst_weight

@lru_cache(None)
def solve_dp(visited, last_city):
    if len(visited) == n:
        return dist_matrix[last_city][0]
    return min(
        dist_matrix[last_city][next_city] + solve_dp(tuple(sorted(visited + (next_city,))), next_city)
        for next_city in range(n) if next_city not in visited
    )

def solve_astar():
    pq = [(0, 0, (0,), 0)]
    visited_states = {}
    while pq:
        f, curr, visited, g = heapq.heappop(pq)
        if len(visited) == n:
            return g + dist_matrix[curr][0]
        state = (curr, visited)
        if state in visited_states and visited_states[state] <= g:
            continue
        visited_states[state] = g
        unvisited = [i for i in range(n) if i not in visited]
        for next_city in unvisited:
            new_g = g + dist_matrix[curr][next_city]
            remaining_nodes = [i for i in unvisited if i != next_city]
            
            # MST Heuristic: 
            # Remaining path must be at least: MST of unvisited nodes + distance to start
            h = get_mst_weight(remaining_nodes)
            if remaining_nodes:
                h += min(dist_matrix[next_city][r] for r in remaining_nodes)
                h += min(dist_matrix[r][0] for r in remaining_nodes)
            else:
                h += dist_matrix[next_city][0]
                
            new_f = new_g + h
            new_visited = tuple(sorted(visited + (next_city,)))
            heapq.heappush(pq, (new_f, next_city, new_visited, new_g))

print("Running DP...")
start_dp = time.time()
res_dp = solve_dp((0,), 0)
time_dp = time.time() - start_dp

print("Running A* with MST...")
start_astar = time.time()
res_astar = solve_astar()
time_astar = time.time() - start_astar

print("-" * 30)
print(f"DP Result: {res_dp:.2f} | Time: {time_dp:.4f}s")
print(f"A* Result: {res_astar:.2f} | Time: {time_astar:.4f}s")