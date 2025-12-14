# Problem Idea Development: Stellar Highways

## Initial Concept
I wanted to create a problem that combines **modular arithmetic** with **shortest path** algorithms on a scale that prohibits standard BFS/DFS. 

**Rejected Idea 1:** A simple grid pathfinding where cells are blocked based on $(x+y) \% K$. 
*Reason for rejection:* Too standard. A simple BFS would solve it if the grid is small, or a pattern analysis if large.

**Rejected Idea 2:** Traveling Salesman variant with modulo constraints.
*Reason for rejection:* NP-hard, likely requires small $N$ bitmask DP, which is too recognizable.

## The Core Twist
The final concept introduces a dependency between the *current state* (total distance covered so far) and the *allowed moves* (available intervals).
- You can only start an interval of type $i$ if your current position $x$ satisfies $x \equiv R_i \pmod K$.
- This creates a graph where nodes are remainders $0 \dots K-1$.
- Since the target distance $M$ is huge ($10^{18}$), this transforms a pathfinding problem into a **Matrix Exponentiation** or **Binary Lifting** problem over the $(\max, +)$ semiring.

## Why it fools AI
1.  **Greedy Trap:** AI models tend to prioritize "longest interval first" or "interval that gets closest to target". They often miss that a shorter interval might land you on a remainder that unlocks a massive interval next.
2.  **Scale Trap:** The problem asks for minimum steps for a huge $M$. AI often defaults to BFS ($O(M)$) or simple DP arrays, which will Memory Limit Exceeded (MLE) or Time Limit Exceeded (TLE).
3.  **Semiring Confusion:** Models often confuse standard Matrix Exponentiation (counting paths) with the $(\max, +)$ variation required here.

## Final Formulation
- **Input:** Target $M$, Modulo $K$, List of intervals $(L, R)$.
- **Goal:** Minimal intervals to cover $[0, M]$.
- **Constraints:** $M \le 10^{18}$, $K \le 50$.
