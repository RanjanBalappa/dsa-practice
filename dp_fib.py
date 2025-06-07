#Memorization
# def func(n, memo):
#     if n <= 1:
#         return n
        
#     if memo[n] != -1:
#         return memo[n]
    
#     memo[n]= func(n -1, memo) + func(n - 2, memo)
#     return memo[n]

# def main():
#     n = 10
#     memo = [-1] * (n+1)
#     print(func(n, memo))

# if __name__ == "__main__":
#     main()

#Tabulation
def func(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[n] = dp[n-1] + dp[n-2]

    return dp[n]

def main():
    n = 10
    print(func(n))

if __name__ == "__main__":
    main()