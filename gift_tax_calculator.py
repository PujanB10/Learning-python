value=int(input("Value of gift:"))
amount=0
if value<5000:
    amount=0
elif 5000<=value<=25000:
    amount=(100+(value-5000)*0.08)
elif 25000<=value<=55000:
    amount=(1700+(value-25000)*0.1)  
elif 55000<=value<=200000:
    amount=(4700+(value-55000)*0.12)
elif 200000<=value<=1000000:
    amount=(22100+(value-200000)*0.15)
elif value>1000000:
    amount=(142100+(value-1000000)*0.17)  
if amount!=0:
    print(f"Amount of tax: {amount} euros")
else:
    print("No tax!")
