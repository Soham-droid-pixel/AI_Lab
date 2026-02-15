from collections import deque

def findLaddersBFS(start, end, words):
    wordSet = set(words)
    if end not in wordSet:
        return []

    res = []
    queue = deque([[start]])
    visited = set()
    shortest_len = float('inf')

    while queue:
        path = queue.popleft()
        
        if len(path) > shortest_len:
            break
            
        curr = path[-1]
        
        for i in range(len(curr)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_w = curr[:i] + c + curr[i+1:]
                
                if next_w in wordSet:
                    if next_w == end:
                        shortest_len = len(path)
                        res.append(path + [next_w])
                    elif next_w not in visited:
                        queue.append(path + [next_w])

        if not queue or len(queue[0]) > len(path):
            for p in queue:
                visited.add(p[-1])

    return res

print(findLaddersBFS("hit", "cog", ["hot","dot","dog","lot","log","cog"]))