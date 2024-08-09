int knapsack(int wt[], int profit[], int W, int N):

{
    # base case: 
    if (N==0) or (W==0) : return 0

    # if we dont have to add: we will move our pointer by 1 to left. we are starting from end of array. 

    if(wt[N]> W): return knapsack(wt, profit, W, N-1)

    else:
        if_picked_ith_element = profit[N] + knapsack(wt, profit, W-wt[N], N-1)
        if_ignored = knapsack(wt, profit, W, N-1)

        return max(if_ignored, if_picked_ith_element)
}