import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        cost = cable1 + cable2
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


cables = [8, 4, 6, 12]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")
