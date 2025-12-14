import heapq
import sys

# QWEN ATTEMPT 1: Dijkstra aiming for max distance
# Fails because M is 10^18 (TLE) and logic is greedy on distance
def solve():
    M, K, N = map(int, sys.stdin.readline().split())
    intervals = []
    for _ in range(N):
        intervals.append(list(map(int, sys.stdin.readline().split())))

    # Priority Queue: (-distance, remainder, steps)
    pq = [(0, 0, 0)] 
    visited = set()

    while pq:
        dist, rem, steps = heapq.heappop(pq)
        dist = -dist
        
        if dist >= M:
            print(steps)
            return

        if steps > 200000: # Heuristic break
            break
            
        # This approach is pure simulation, will TLE immediately on M=10^18
        for l, r in intervals:
            if r == rem:
                heapq.heappush(pq, (-(dist + l), (dist + l) % K, steps + 1))
                
    print(-1)
solve()
