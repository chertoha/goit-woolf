from datetime import datetime

def get_days_from_today(date):
    try:
        reduced_date = datetime.strptime(date, "%Y-%m-%d") 
        current_datetime = datetime.today()
        return  (current_datetime - reduced_date).days
    except ValueError as err:
        return  f"Sorry, date format is wrong, should be 'YYYY-mm-dd', \n error:  {err.args[0]}"

print(get_days_from_today("2021-05-05"))

