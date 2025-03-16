from colorama import Fore, Style


def display_log_counts(counts: dict, active_level: str):
    print("{:<17} | {:10}".format("Рівень логування", "Кількість"))
    print("{:<17} | {:10}".format("—————————————————", "———————————"))
    for key, value in counts.items():
        if active_level != None and key.lower() == active_level.lower():
            print("{:<26} | {:<10}".format(
                Fore.RED + key + Style.RESET_ALL, value))
        else:
            print("{:<17} | {:<10}".format(key, value))


def display_log_details(logs, active_level: str):
    if active_level != None:
        print(f"\nДеталі логів для рівня {active_level.upper()}:\n")
    else:
        print("\nДеталі всіх логів\n")

    for log in logs:
        print(f"{log["date"]} - {log["text"]}")
