# Graph Pathfinding Algorithms

This repository contains Python implementations of three powerful and efficient pathfinding algorithms: Uniform Cost Search (UCS), Depth First Search (DFS), and Breadth First Search (BFS). These algorithms are designed to find optimal paths between nodes in a given graph, enabling you to navigate through complex networks and uncover the most efficient routes.

## Features

- **Uniform Cost Search (UCS):** This algorithm explores the graph by considering the cost associated with each edge. It guarantees finding the optimal path with the lowest cumulative cost.
- **Depth First Search (DFS):** DFS explores the graph by traversing as far as possible along each branch before backtracking. It is well-suited for finding paths in unweighted graphs and can be useful in scenarios where exploring deeply is prioritized over finding the shortest path.
- **Breadth First Search (BFS):** BFS explores the graph by systematically visiting all neighboring nodes at the current depth level before moving on to the next level. It guarantees finding the shortest path in unweighted graphs and is particularly effective for finding paths between nodes at close proximity.

## Usage

To utilize the pathfinding algorithms, follow these steps:

1. Clone this repository to your local machine or download the code from the [GitHub repository](https://github.com/zaahidali/ceng3511).
2. Ensure you have Python 3.x installed on your system.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the script `graph_search.py` using the command: `python graph_search.py`.
5. The program will prompt you to enter the start and goal states for pathfinding.
6. After entering the states, the program will execute the three algorithms and present the results.

## Input Format

The input graph is stored in the file `graph.txt`, which provides the foundation for pathfinding operations. The graph is represented using a specific format, where each line corresponds to a node in the graph along with its neighbors and the respective edge weights. The line format is as follows:

```
<Node>: {<Neighbor1>: <Weight1>, <Neighbor2>: <Weight2>, ...}
```

For instance, a line in the file may appear as:

```
A: {A: 0, B: 6, C: 4, D: 3, E: 0, F: 0, G: 0}
```

This line signifies node A, which connects to its neighboring nodes B, C, D, E, F, and G, with the corresponding edge weights.

## Algorithm Results

Upon execution, the program employs the three algorithms to explore the input graph and determines the paths between the specified start and goal states. The paths are presented as a sequence of nodes leading from the start state to the goal state. In cases where no path exists between the two nodes, the program provides appropriate feedback.

## Algorithm Examples

Here are some examples showcasing the usage of each algorithm:

- **Uniform Cost Search (UCS):**
  ```plaintext
  Start State: A
  Goal State: F

  Result: A - C - F
  ```

- **Depth First Search (DFS):**
  ```plaintext
  Start State: A
  Goal State: G

  Result: A - C - F - G
  ```

- **Breadth First Search (BFS):**
  ```plaintext
  Start State: A
  Goal State: E

  Result: A - B - E
  ```

These examples demonstrate the paths found by each algorithm from the specified start state to the goal state within the given graph. The paths are determined based on the characteristics of each algorithm, ensuring optimal or efficient traversal depending on the specific requirements of the problem.

## Repository Structure

This repository encompasses the following files:

- `graph_search.py`: The primary Python script implementing the graph pathfinding algorithms.
- `graph.txt`: The input file containing the graph representation.
- `README.md`: The current file, which offers an overview of the repository, usage instructions, and algorithm examples.

## Contributing

Contributions to this project are highly appreciated! If you identify any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Let's collaborate to enhance the functionality and usability of these pathfinding algorithms.

## License

This project is licensed under the [MIT License](LICENSE), granting you the freedom to use, modify, and distribute the code.

---

Please feel free to reach out if you have any further questions or require additional assistance!
