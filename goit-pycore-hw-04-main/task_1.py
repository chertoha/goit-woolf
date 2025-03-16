def total_salary(path):
   try:
    with open(path, "r", encoding="utf-8") as fh:
        salaries = [int(el.strip().split(",")[1]) for el in fh.readlines()]
    
    total = sum(salaries)
    return (total, int(total / len(salaries)))
    
   except FileNotFoundError:
    return "No file"
   except Exception as err: 
    return err
     




if __name__ == "__main__":
    total, average = total_salary("./data/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")