import sys

# Set recursion depth just in case, though not used
sys.setrecursionlimit(2000)

def solve():
    # Read Input
    try:
        input = sys.stdin.read
        data = input().split()
    except Exception:
        return

    if not data:
        return

    iterator = iter(data)
    M = int(next(iterator))
    K = int(next(iterator))
    N = int(next(iterator))

    # Adjacency Matrix for 1 step
    # mat[u][v] = max length to go from rem u -> rem v
    # Initialize with -1 (representing -infinity)
    INF = -1
    adj = [[INF] * K for _ in range(K)]

    for _ in range(N):
        l_val = int(next(iterator))
        r_val = int(next(iterator))
        
        # Determine next remainder
        next_rem = (r_val + l_val) % K
        
        # We want to maximize length for a specific u->v transition
        if l_val > adj[r_val][next_rem]:
            adj[r_val][next_rem] = l_val

    # Function to multiply two KxK matrices in (max, +) semiring
    def mul_mat(A, B):
        C = [[INF] * K for _ in range(K)]
        for i in range(K):
            for k in range(K):
                if A[i][k] == INF: continue
                val_ik = A[i][k]
                row_b = B[k]
                for j in range(K):
                    if row_b[j] == INF: continue
                    curr = val_ik + row_b[j]
                    if curr > C[i][j]:
                        C[i][j] = curr
        return C

    # Precompute powers of the matrix: adj^(2^0), adj^(2^1), ...
    # Max M is 10^18, so 60 bits is enough (2^60 > 10^18)
    powers = []
    current_pow = adj
    
    # Check if 1 step is enough (edge case) or if 0 reachable
    # Actually, we run binary lifting. We need up to ~60 powers.
    # Note: If M is small, we still compute, overhead is small.
    
    for _ in range(62):
        powers.append(current_pow)
        current_pow = mul_mat(current_pow, current_pow)

    # Current state: dp[rem] = max_dist starting from 0 ending at rem
    # Initial: rem 0 has dist 0, others -INF
    current_dist = [-1] * K
    current_dist[0] = 0
    
    total_steps = 0
    
    # Try to jump by 2^i steps if it doesn't finish the job
    for i in range(61, -1, -1):
        # Multiply vector current_dist by powers[i]
        next_dist = [-1] * K
        mat = powers[i]
        
        possible_to_move = False
        max_reached = -1
        
        for u in range(K):
            if current_dist[u] == -1: continue
            row = mat[u]
            for v in range(K):
                if row[v] == -1: continue
                val = current_dist[u] + row[v]
                if val > next_dist[v]:
                    next_dist[v] = val
                if val > max_reached:
                    max_reached = val
        
        # Check condition: 
        # If max_reached < M, it means even after these 2^i steps,
        # we haven't reached the goal. So we MUST take these steps.
        # Note: If max_reached == -1, it means we hit a dead end in this path,
        # treating as < M.
        
        if max_reached < M:
            # Commit to these steps
            current_dist = next_dist
            total_steps += (1 << i)
    
    # After the loop, current_dist is the state after `total_steps`.
    # We haven't reached M yet. The answer should be total_steps + 1.
    # But we must verify if it's possible to move one more step.
    
    # Check if we can reach >= M in exactly one more step
    can_finish = False
    
    # One more matrix multiplication with powers[0] (1 step)
    final_check_max = -1
    for u in range(K):
        if current_dist[u] == -1: continue
        row = powers[0][u]
        for v in range(K):
            if row[v] != -1:
                val = current_dist[u] + row[v]
                if val >= M:
                    can_finish = True
                if val > final_check_max:
                    final_check_max = val

    if can_finish:
        print(total_steps + 1)
    else:
        # If we couldn't finish even with 1 more step, 
        # AND we couldn't take larger jumps, it implies we are stuck or M is unreachable.
        # But logically, if we processed bits correctly, total_steps is the max steps < M.
        # So total_steps + 1 should be >= M.
        # If final_check_max < M, then it's impossible.
        print("-1")

if __name__ == "__main__":
    solve()
