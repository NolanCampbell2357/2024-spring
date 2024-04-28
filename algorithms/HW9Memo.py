def leastCoins(coins, change, memo):
    if change in memo:
        return memo[change]
    if(change == 0):
        return 0, []
    least = float('inf')
    leastCombo = []
    for coin in coins:
        if(coin <= change):
            count, combo = leastCoins(coins, change - coin, memo)
            if count + 1 < least:
              least = count + 1
              leastCombo = [coin] + combo
    memo[change] = (least, leastCombo)
    return least, leastCombo

print(leastCoins([1, 3, 4], 6, {}))