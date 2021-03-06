

def editdistance(arr1,arr2):
    n,m = len(arr1),len(arr2)
    dp = [[1000000]*(m+1) for _ in range(n+1)]

    for i in range(m+1):
        dp[0][i]=i

    for i in range(n+1):
        dp[i][0]=i

    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    return dp[n][m]




