import random

def generate_case(case_id):
    filename = f"test_cases/{case_id}.in"
    
    # Params
    if case_id == 1: # Small
        M = 20
        K = 5
        N = 3
    elif case_id == 2: # Impossible
        M = 100
        K = 10
        N = 2
    elif case_id == 3: # Large M, simple cycle
        M = 10**18
        K = 2
        N = 2
    elif case_id == 4: # Random Med
        M = random.randint(1000, 100000)
        K = 20
        N = 50
    else: # Max Constraints
        M = 10**18
        K = 50
        N = 100

    with open(filename, 'w') as f:
        f.write(f"{M} {K} {N}\n")
        
        for _ in range(N):
            if case_id == 3:
                # Force a 1-cycle
                L = 10**9 + 1
                R = 1 # Remainder will be (1 + 10^9 + 1)%2
                # Ensure connectivity
                if _ == 0: f.write(f"3 0\n") # 0 -> 1
                else: f.write(f"{L} 1\n") # 1 -> 1
            else:
                L = random.randint(1, 10**9 if case_id > 2 else 10)
                R = random.randint(0, K - 1)
                f.write(f"{L} {R}\n")

if __name__ == "__main__":
    import os
    if not os.path.exists("test_cases"):
        os.makedirs("test_cases")
    for i in range(1, 6):
        generate_case(i)
