import numpy as np
import heapq

cities = {0: (0, 0), 1: (1, 5), 2: (4, 1), 3: (3, 3), 4: (5, 5)}
n = len(cities)

def get_dist(c1, c2):
    return np.linalg.norm(np.array(cities[c1]) - np.array(cities[c2]))

dist_matrix = [[get_dist(i, j) for j in range(n)] for i in range(n)]

def solve_astar():
    pq = [(0, 0, (0,), 0)]
    
    while pq:
        f, curr, visited, g = heapq.heappop(pq)

        if len(visited) == n:
            return g + dist_matrix[curr][0]

        for next_city in range(n):
            if next_city not in visited:
                new_g = g + dist_matrix[curr][next_city]
                remaining = [i for i in range(n) if i not in visited and i != next_city]
                h = min([dist_matrix[next_city][r] for r in remaining]) if remaining else dist_matrix[next_city][0]
                new_f = new_g + h
                new_visited = tuple(sorted(visited + (next_city,)))
                heapq.heappush(pq, (new_f, next_city, new_visited, new_g))

print(f"A* Result: {solve_astar():.2f}")