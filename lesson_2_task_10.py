def bank(initial_deposit, years):
    total_amount = initial_deposit
    interest_rate = 0.10
    for _ in range(years):
        interest = total_amount * interest_rate
        total_amount += interest
        total_amount *= 1.10
    return total_amount

initial_deposit = 100000
years = 5
final_amount = bank(initial_deposit, years)
print(f"Сумма на счете через {years} лет составит {final_amount:.2f} рублей.")