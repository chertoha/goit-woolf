import re


def parse_log_line(line: str) -> dict:
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)$"
    match = re.match(pattern, line)
    if match:
        date, level, text = match.groups()
    return {"date": date, "level": level, "text": text}


def load_logs(file_path: str) -> list:
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append(parse_log_line(line))
    return res


def filter_logs_by_level(logs: list, level: str) -> list:

    res = filter(lambda log: log['level'].lower() == level.lower(), logs)
    return list(res)


def count_logs_by_level(logs: list) -> dict:
    res = {}

    for log in logs:
        key = log["level"]
        if key in res:
            res[key] = res[key] + 1
        else:
            res[key] = 1

    return res
