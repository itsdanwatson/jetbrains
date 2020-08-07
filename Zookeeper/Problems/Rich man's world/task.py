deposit = int(input())
government_fund = 700000
new_amount = deposit
interest = (new_amount / 100) * 7.1
years = 0
while new_amount < government_fund:
    new_amount += interest
    interest = (new_amount / 100) * 7.1
    years += 1

print(years)
