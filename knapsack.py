#knapsack algo
def Knapsack(W,wt,value,M):
    #for w = 0 to W M[0,w] <- 0
    mat = [[0 for x in range(W + 1)]for x in range (M + 1)]
    for i in range(M+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                mat[i][w] = 0
            elif wt[i-1] <= w:
                mat[i][w] = max(value[i-1] + mat[i-1][w-wt[i-1]], mat[i-1][w])
            else:
                mat[i][w] = mat[i-1][w]
    return mat[M][W]

if __name__ == '__main__':
    values = [1,6,18,22,28]
    weights = [1,2,5,6,7]
    weight_limit = 11
    M = len(values)
    print("Máxima ganancia: ",Knapsack(weight_limit,weights,values,M))