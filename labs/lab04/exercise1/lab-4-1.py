kwh = int(input())
if kwh > 100:
    if kwh <= 200:
        charge = kwh * 0.5
    else:
        if kwh > 200:
            charge = kwh * 0.75
else:
    charge = kwh * 0.3
totalBill = kwh + charge
print(totalBill)
