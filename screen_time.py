from datetime import datetime, timedelta

file=input("Filename: ")
starting_date=input("Starting date: ")
no_of_days=int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
starting_date=(datetime.strptime(starting_date, "%d.%m.%Y")).date()

text=""
total_minutes=0
for i in range(no_of_days):
    days=timedelta(days=i)
    req_date=datetime.strftime(starting_date+days,"%d.%m.%Y")
    minutes=input(f"{(starting_date+days)}: ")
    minutes=minutes.replace(" ","/")
    for elements in minutes.split("/"):
        total_minutes+=int(elements)
    text+=(f"{req_date}: {minutes} \n")

print(f"Data stored in file {file}")
starting_date=datetime.strftime(starting_date,"%d.%m.%Y")

with open(file,"w") as writing_file:
    writing_file.write(f"Time period: {starting_date}-{req_date} \n")
    writing_file.write(f"Total minutes: {total_minutes} \n")
    writing_file.write(f"Average minutes: {total_minutes/no_of_days}\n")
    writing_file.write(text)



