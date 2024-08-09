def find_knapsack_r(capacity, weights, values, n, t):
    # print(t, capacity, n)
    
    if n==0 or capacity ==0:
        return 0

    if t[capacity][n]!=-1:
        return t[capacity][n]
    
    if (weights[n-1] <= capacity):
        t[capacity][n] = max(values[n-1] + find_knapsack_r(capacity-weights[n-1], weights, values, n-1, t), 
        find_knapsack_r(capacity, weights, values, n-1, t)
        
        )
        return t[capacity][n]

    else:
        t[capacity][n] =  find_knapsack_r(capacity, weights, values, n-1, t)
        return t[capacity][n]

def find_knapsack(capacity, weights, values, n):
    t = [[-1 for i in range(n+1)] for j in range(capacity+1)]
    return find_knapsack_r(capacity, weights, values, n, t)



def knapsack(wt, profit, W):
    n = len(wt)
    # Create a 2D DP array of size (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the DP table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i-1] <= j:
                # Max of including the item or excluding it
                dp[i][j] = max(dp[i-1][j], profit[i-1] + dp[i-1][j - wt[i-1]])
            else:
                # If weight of the item is more than j, don't include it
                dp[i][j] = dp[i-1][j]
    
    # The maximum profit will be in dp[n][W]
    return dp[n][W]

# Example usage
wt = [1, 2, 3]        # Weights of the items
profit = [2, 3, 5]    # Profits of the items
W = 4                 # Maximum weight capacity of the knapsack

max_profit = knapsack(wt, profit, W)
print(f"Maximum profit: {max_profit}")
