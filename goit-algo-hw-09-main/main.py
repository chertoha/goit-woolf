COINS = [50, 25, 10, 5, 2, 1]


def find_coins_eager(amount):
    coins = list(sorted(COINS, reverse=True))
    result = {}

    for coin in coins:
        while amount >= coin:
            amount -= coin
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1

    return result


def find_min_coins(amount):
    coins = list(sorted(COINS, reverse=True))
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


if __name__ == "__main__":
    amount = 113
    print("Greedy Algorithm:")
    print(find_coins_eager(amount))

    print("Dynamic Programming:")
    print(find_min_coins(amount))

    import time

    large_amount = 100000

    start = time.time()
    find_coins_eager(large_amount)
    print(
        f"Greedy algorithm time for {large_amount}: {time.time() - start:.6f} seconds")

    start = time.time()
    find_min_coins(large_amount)
    print(
        f"Dynamic programming time for {large_amount}: {time.time() - start:.6f} seconds")
