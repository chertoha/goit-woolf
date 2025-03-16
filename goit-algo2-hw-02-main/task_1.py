from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:

    jobs = [PrintJob(**job) for job in print_jobs]
    jobs.sort(key=lambda x: (x.priority, x.print_time))

    max_volume = constraints["max_volume"]
    max_items = constraints["max_items"]

    print_order = []
    total_time = 0

    while jobs:
        batch = []
        batch_volume = 0
        batch_time = 0

        for job in jobs[:]:
            if len(batch) < max_items and batch_volume + job.volume <= max_volume:
                batch.append(job)
                batch_volume += job.volume
                batch_time = max(batch_time, job.print_time)
                jobs.remove(job)
                print_order.append(job.id)

        total_time += batch_time

    return {
        "print_order": print_order,
        "total_time": total_time
    }


if __name__ == "__main__":
    constraints = {"max_volume": 300, "max_items": 2}

    test_cases = [
        {
            "name": "Тест 1 (однаковий пріоритет)",
            "jobs": [
                {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
            ]
        },
        {
            "name": "Тест 2 (різні пріоритети)",
            "jobs": [
                {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
            ]
        },
        {
            "name": "Тест 3 (перевищення обмежень)",
            "jobs": [
                {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
                {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
                {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
            ]
        }
    ]

    for test in test_cases:
        result = optimize_printing(test["jobs"], constraints)
        print(
            f"{test['name']}:\nПорядок друку: {result['print_order']}\nЗагальний час: {result['total_time']} хвилин\n")
