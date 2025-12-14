import sys

# QWEN ATTEMPT 2: Try to find a cycle and skip
def solve():
    M, K, N = map(int, sys.stdin.readline().split())
    adj = []
    for _ in range(N):
        adj.append(list(map(int, sys.stdin.readline().split())))

    curr_rem = 0
    curr_dist = 0
    steps = 0
    history = {}

    while curr_dist < M:
        # Find best next interval (Greedy pick max length)
        best_l = -1
        for l, r in adj:
            if r == curr_rem:
                if l > best_l:
                    best_l = l
        
        if best_l == -1:
            print(-1)
            return

        curr_rem = (curr_rem + best_l) % K
        curr_dist += best_l
        steps += 1
        
        # Naive cycle detection
        if curr_rem in history:
            prev_dist, prev_steps = history[curr_rem]
            cycle_len = curr_dist - prev_dist
            cycle_steps = steps - prev_steps
            
            remaining = M - curr_dist
            if remaining > 0:
                num_cycles = remaining // cycle_len
                steps += num_cycles * cycle_steps
                curr_dist += num_cycles * cycle_len
            history = {} # Reset to avoid infinite loop logic errors
        else:
            history[curr_rem] = (curr_dist, steps)
            
    print(steps)
solve()
