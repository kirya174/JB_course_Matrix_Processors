def print_output(income, percent):
    tax = income * percent/100
    print(f'The tax for {income} is {percent}%. That is {tax:.0f} dollars!')


income = int(input())
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
else:
    percent = 28

print_output(income, percent)