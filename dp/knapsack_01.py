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
