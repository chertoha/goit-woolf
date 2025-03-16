from datetime import datetime, timedelta
from pprint import pprint


def get_upcoming_birthdays(users):
    
    current_date = datetime.today().date()
    # current_date = datetime.strptime("1985.12.28", "%Y.%m.%d").date()

    res = []

    for user in users:
        date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        comparing_year = current_date.year
        if(date.month, date.day) < (current_date.month, current_date.day):
            comparing_year += 1

        
        comparing_date = datetime(comparing_year, date.month, date.day).date()

        if comparing_date < current_date or comparing_date >=  current_date + timedelta(days=7):
            continue

        congrats_date = comparing_date;

        if comparing_date.weekday() == 5: 
            congrats_date = comparing_date + timedelta(days=2)
        elif comparing_date.weekday() == 6:
            congrats_date = comparing_date + timedelta(days=1)

        res.append({**user, 'congratulation_date': congrats_date.strftime("%Y.%m.%d")})    
    
    return sorted(res, key=lambda elem: elem["congratulation_date"])



users = [
    {
        "name": "John Doe", 
        "birthday": "1985.01.23"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.01.27"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.11.16"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.11.15"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.11.21"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.11.17"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.01.27"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.01.27"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.11.19"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.01.03"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.12.29"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.01.27"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.12.31"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.11.22"
    },
    
    {
        "name": "Jane Smith", 
        "birthday": "1990.01.27"
    }
]


pprint(get_upcoming_birthdays(users), indent=4)