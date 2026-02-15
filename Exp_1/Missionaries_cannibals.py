moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    mr = 3 - m
    cr = 3 - c
    if mr > 0 and cr > mr:
        return False
    return True


def dfs(state, path, visited):
    if state == (0, 0, 1):
        print("Solution:")
        for s in path:
            print(s)
        return True

    m, c, boat = state
    visited.add(state)

    for dm, dc in moves:
        if boat == 0:  # left → right
            new = (m-dm, c-dc, 1)
        else:          # right → left
            new = (m+dm, c+dc, 0)

        if valid(new[0], new[1]) and new not in visited:
            if dfs(new, path + [new], visited):
                return True

    return False


start = (3, 3, 0)
dfs(start, [start], set())
