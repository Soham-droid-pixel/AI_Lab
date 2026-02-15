from collections import deque

def run_ai_search_lab():
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    # BFS Implementation
    def perform_bfs(start_node):
        visited = []
        queue = deque([start_node])
        nodes_expanded = 0

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.append(current)
                nodes_expanded += 1
                for neighbor in graph[current]:
                    queue.append(neighbor)
        
        return visited, nodes_expanded

    # DFS Implementation
    def perform_dfs(start_node):
        visited = []
        stack = [start_node]
        nodes_expanded = 0

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                nodes_expanded += 1
                
                for neighbor in reversed(graph[current]):
                    stack.append(neighbor)
        
        return visited, nodes_expanded

    
    print("--- Lab 1: Uninformed Search Results ---")
    
    bfs_order, bfs_count = perform_bfs('A')
    print(f"BFS Order: {bfs_order}")
    print(f"BFS Expanded Nodes: {bfs_count}")
    
    print("-" * 30)
    
    dfs_order, dfs_count = perform_dfs('A')
    print(f"DFS Order: {dfs_order}")
    print(f"DFS Expanded Nodes: {dfs_count}")

run_ai_search_lab()