from collections import deque

capA = 4
capB = 3
goal = 2

start = (0, 0)

def get_next_states(a, b):
    states = []

    # fill
    states.append((capA, b))
    states.append((a, capB))

    # empty
    states.append((0, b))
    states.append((a, 0))

    # pour A -> B
    pour = min(a, capB - b)
    states.append((a - pour, b + pour))

    # pour B -> A
    pour = min(b, capA - a)
    states.append((a + pour, b - pour))

    return states


def bfs():
    q = deque()
    q.append((start, [start]))
    visited = set([start])

    while q:
        (a, b), path = q.popleft()

        if a == goal or b == goal:
            print("Solution path:")
            for s in path:
                print(s)
            return

        for nxt in get_next_states(a, b):
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + [nxt]))

bfs()
