limit = int(input("Limit:"))
base = 0
num = 1
num_total = 0
calculation = 'The consecutive sum: '
while base < limit:
    calculation += f"{num} + "
    base += num
    num += 1

print(f"{calculation[:-3]} = {base}")
