from datetime import datetime

def convert_dates_to_weekdays(date):
    # Convert dates to days of the week
    day_of_week = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    return day_of_week