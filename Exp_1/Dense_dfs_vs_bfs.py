import time
import tracemalloc
import random
import string
from collections import deque
import sys

sys.setrecursionlimit(2000)

# --- YOUR BFS CODE (Unchanged) ---
def findLaddersBFS(start, end, words):
    wordSet = set(words)
    if end not in wordSet: return []
    res = []
    queue = deque([[start]])
    visited = set()
    shortest_len = float('inf')
    
    while queue:
        path = queue.popleft()
        if len(path) > shortest_len: break
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
            for p in queue: visited.add(p[-1])
    return res

# --- YOUR DFS CODE (Unchanged) ---
def find_all_word_paths_dfs(start_word, target_word, word_list):
    word_pool = set(word_list)
    if target_word not in word_pool: return []
    final_results = []
    active_path_words = {start_word}

    def explore_paths(current_word, current_path):
        if len(final_results) >= 5: return 

        if current_word == target_word:
            final_results.append(list(current_path))
            return

        for position in range(len(current_word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:position] + letter + current_word[position+1:]
                if new_word in word_pool and new_word not in active_path_words:
                    active_path_words.add(new_word)
                    explore_paths(new_word, current_path + [new_word])
                    active_path_words.remove(new_word)

    explore_paths(start_word, [start_word])
    return final_results

# --- SIMPLER GENERATOR (Guarantees Connections) ---
def generate_connected_list(start, end, size):
    """
    Creates a small list of words that actually connect start to end.
    """
    # 1. Start with the known path for 6 words
    base_path = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    if size <= 6:
        return base_path[:size] + [end] if end not in base_path[:size] else base_path[:size]

    # 2. Add random variations of base words to fill up to 'size'
    generated = set(base_path)
    generated.add(end)
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    while len(generated) < size:
        # Pick an existing word and change 1 letter
        base = random.choice(list(generated))
        pos = random.randint(0, 2)
        char = random.choice(alphabet)
        new_w = base[:pos] + char + base[pos+1:]
        generated.add(new_w)
            
    return list(generated)

def run_benchmark():
    start, end = "hit", "cog"

    # Test Sizes (Small & Safe)
    test_sizes = [6, 12, 20]

    print(f"{'Size':<5} | {'Algo':<5} | {'Time (sec)':<10} | {'Memory (KB)':<15}")
    print("-" * 45)

    for size in test_sizes:
        word_list = generate_connected_list(start, end, size)
        
        # --- TEST BFS ---
        tracemalloc.start()
        t0 = time.time()
        findLaddersBFS(start, end, word_list)
        t1 = time.time()
        _, peak_bfs = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"{size:<5} | {'BFS':<5} | {t1 - t0:.6f}     | {peak_bfs / 1024:.4f}")

        # --- TEST DFS ---
        tracemalloc.start()
        t0 = time.time()
        find_all_word_paths_dfs(start, end, word_list)
        t1 = time.time()
        _, peak_dfs = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"{size:<5} | {'DFS':<5} | {t1 - t0:.6f}     | {peak_dfs / 1024:.4f}")
        print("-" * 45)

if __name__ == "__main__":
    run_benchmark()