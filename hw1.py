import calendar

def display_months():
    months = list(calendar.month_name)  # Get the month names
    for month in months:
        if month:  # Ignore empty strings (calendar.month_name[0] is an empty string)
            print(month)

display_months()
