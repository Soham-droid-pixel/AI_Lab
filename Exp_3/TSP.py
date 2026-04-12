import numpy as np
import random
from functools import lru_cache

cities = {
    0: (5, 8), 1: (1, 1), 2: (9, 2), 3: (7, 5), 4: (2, 9),
    5: (0, 4), 6: (3, 7), 7: (8, 0), 8: (4, 4), 9: (6, 1),
    10: (2, 2), 11: (5, 0), 12: (1, 6), 13: (9, 9), 14: (0, 1),
    15: (7, 8), 16: (3, 0), 17: (8, 4), 18: (6, 6), 19: (4, 2)
}
n = len(cities)

def get_dist(c1, c2):
    return np.linalg.norm(np.array(cities[c1]) - np.array(cities[c2]))

dist_matrix = [[get_dist(i, j) for j in range(n)] for i in range(n)]

def solve_greedy():
    unvisited = list(range(1, n))
    curr, path, total_dist = 0, [0], 0
    while unvisited:
        next_node = min(unvisited, key=lambda x: dist_matrix[curr][x])
        total_dist += dist_matrix[curr][next_node]
        curr = next_node
        unvisited.remove(curr)
        path.append(curr)
    total_dist += dist_matrix[curr][0] 
    return total_dist

@lru_cache(None)
def solve_dp(visited, last_city):
    if len(visited) == n:
        return dist_matrix[last_city][0]
    costs = []
    for next_city in range(n):
        if next_city not in visited:
            new_visited = tuple(sorted(visited + (next_city,)))
            res = dist_matrix[last_city][next_city] + solve_dp(new_visited, next_city)
            costs.append(res)
    return min(costs)

def solve_genetic(attempts=100):
    best_path = random.sample(range(n), n)
    def score(p): return sum(dist_matrix[p[i]][p[(i+1)%n]] for i in range(n))
    for _ in range(attempts):
        test_path = best_path[:]
        i, j = random.sample(range(n), 2)
        test_path[i], test_path[j] = test_path[j], test_path[i]
        if score(test_path) < score(best_path):
            best_path = test_path
    return score(best_path)

print(f"Greedy:  {solve_greedy():.2f}")
print(f"DP:      {solve_dp((0,), 0):.2f}")
print(f"Genetic: {solve_genetic():.2f}")