from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def helper(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = 0
        best_cut = []

        for i in range(1, n + 1):
            if i <= len(prices):
                profit, cuts = helper(n - i)
                profit += prices[i - 1]
                if profit > max_profit:
                    max_profit = profit
                    best_cut = [i] + cuts

        memo[n] = (max_profit, best_cut)
        return memo[n]

    max_profit, cuts = helper(length)
    return {"max_profit": max_profit, "cuts": cuts, "number_of_cuts": len(cuts) - 1}


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for n in range(1, length + 1):
        for i in range(1, n + 1):
            if i <= len(prices):
                if dp[n] < prices[i - 1] + dp[n - i]:
                    dp[n] = prices[i - 1] + dp[n - i]
                    cuts[n] = cuts[n - i] + [i]

    return {"max_profit": dp[length], "cuts": sorted(cuts[length], reverse=True), "number_of_cuts": len(cuts[length]) - 1}


def run_tests():
    test_cases = [
        {"length": 5, "prices": [2, 5, 7, 8, 10], "name": "Базовий випадок"},
        {"length": 3, "prices": [1, 3, 8], "name": "Оптимально не різати"},
        {"length": 4, "prices": [3, 5, 6, 7], "name": "Рівномірні розрізи"}
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()
