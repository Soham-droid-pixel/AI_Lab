# AI Lab Experiments

This repository contains Python implementations of classical Artificial Intelligence search algorithms, focusing on uninformed search strategies like Breadth-First Search (BFS) and Depth-First Search (DFS) applied to various well-known AI problems.

## 📂 Project Structure

Currently, the project contains **Experiment 1 (Exp_1)**, which focuses on Uninformed Search problems.

### `Exp_1/` - Uninformed Search Algorithms & Puzzles
This directory contains several classical AI puzzles and search space traversals:

* **[comparison_dfs_vs_bfs.py](Exp_1/comparison_dfs_vs_bfs.py)**: A baseline implementation comparing the node expansion, time, and traversal differences between BFS and DFS on a sample graph structure.
* **[Dense_dfs_vs_bfs.py](Exp_1/Dense_dfs_vs_bfs.py)**: Evaluating performance differences between BFS and DFS on a denser graph/tree representation.
* **[Missionaries_cannibals.py](Exp_1/Missionaries_cannibals.py)**: Solves the classic Missionaries and Cannibals river-crossing logic puzzle using a Depth-First Search (DFS) approach to safely move across the river without violating constraints.
* **[Water_Jug.py](Exp_1/Water_Jug.py)**: Implements a state-space search algorithm to solve the classical Water Jug measuring problem. 
* **[word_ladder_bfs.py](Exp_1/word_ladder_bfs.py)**: Solves the shortest-path Word Ladder puzzle (transforming one word into another by changing one letter at a time) using Breadth-First Search (BFS) for optimal shortest paths.
* **[word_ladder_dfs.py](Exp_1/word_ladder_dfs.py)**: Solves the Word Ladder puzzle using Depth-First Search (DFS), demonstrating the difference in pathfinding behavior compared to BFS.

## 🚀 Getting Started

### Prerequisites
- Python 3.x is required to run the scripts.
- No external dependencies are currently required (uses standard Python libraries like `collections.deque`).

### Running the Scripts
Navigate into the respective experiment folder and run any of the Python files using:

```bash
cd Exp_1
python comparison_dfs_vs_bfs.py
python Missionaries_cannibals.py
```

## 🧠 Concepts Covered
- **Breadth-First Search (BFS)**: Uses a Queue (FIFO). Explores level by level, guaranteeing the shortest path in an unweighted state-space graph (e.g., Word Ladder BFS).
- **Depth-First Search (DFS)**: Uses a Stack (LIFO) or Recursion. Explores as far as possible along each branch before backtracking (e.g., used heavily in constraint pathfinding like Missionaries & Cannibals).
- **State Space Representation**: Modeling problems as states (e.g., representing jug volumes or people counts) and moving between valid states.
