import calendar

def display_months():
    months = list(calendar.month_name)  
    for month in months:
        if month: 
            print(month)

display_months()
