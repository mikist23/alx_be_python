import datetime

def display_current_datetime():
    current_date = datetime.datetime.today().replace(microsecond=0)
    print(f"Current date and time: {current_date}")
    return current_date


def calculate_future_date():
    day = int(input("Enter the number of days to add to the current date: "))
    today = display_current_datetime()
    future_date = datetime.timedelta(days = day)
    future_date = today.date() + future_date
    print(f"Future date: {future_date}")


display_current_datetime()
calculate_future_date()