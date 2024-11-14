# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
for weeks in monthly_expenses:
    food += weeks[0]

transport = 0
for weeks in monthly_expenses:
    transport += weeks[1]
    
utilities = 0
for weeks in monthly_expenses:
    utilities += weeks[2]

week1 = 0 
for i in range(len(monthly_expenses[0])):
    week1 += monthly_expenses[0][i]

week2 = 0 
for i in range(len(monthly_expenses[1])):
    week2 += monthly_expenses[1][i]

week3 = 0 
for i in range(len(monthly_expenses[2])):
    week3 += monthly_expenses[2][i]

week4 = 0 
for i in range(len(monthly_expenses[3])):
    week4 += monthly_expenses[3][i]

total = 0
for i in range(len(monthly_expenses)):
    for j in range(len(monthly_expenses[i])):
        total += monthly_expenses[i][j]


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:',total)