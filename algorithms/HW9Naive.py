def leastCoins(coins, change):
    if(change == 0):
        return 0, []
    least = float('inf')
    leastCombo = []
    for coin in coins:
        if(coin <= change):
            count, combo = leastCoins(coins, change - coin)
            if count + 1 < least:
              least = count + 1
              leastCombo = [coin] + combo
    return least, leastCombo

print(leastCoins([1, 3, 4], 6))