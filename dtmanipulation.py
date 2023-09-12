import datetime as dt

# Task 1 
current_date = "8/07/2021"
current_date_temp = dt.datetime.strptime(current_date, "%d/%m/%Y")
new_date = current_date_temp - dt.timedelta(days=15)

print(new_date.strftime("%Y-%m-%d"))


# Task 2  

current_date = "8/07/2021"
current_date_temp = dt.datetime.strptime(current_date, "%d/%m/%Y")
new_date = current_date_temp + dt.timedelta(days=7)

print(new_date.strftime("%Y-%m-%d"))

# Task 3

current_date = "1 January, 2020"
current_date_temp = dt.datetime.strptime(current_date, "%d %B, %Y")
new_date = current_date_temp + dt.timedelta(days=25)

print("Hello Friedrich, your rent of 300 euro is due on ",new_date.strftime("%d %B, %Y"))