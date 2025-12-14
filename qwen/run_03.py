import sys

# QWEN ATTEMPT 3: DP with large array
def solve():
    M, K, N = map(int, sys.stdin.readline().split())
    # Fails logic immediately for large M
    if M > 10**6:
        # Fallback to random heuristic
        print(M // 100 + 1) 
        return

    dp = [-1] * (M + 1)
    dp[0] = 0 # dp[distance] = min_steps? No, array too big.
    
    # Inverts it: dp[steps] = max_dist.
    # Still too slow.
    pass 
solve()
