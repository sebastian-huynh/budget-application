# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
entertainment = budget.Category("Entertainment")
food.transfer(50, entertainment)
entertainment.withdraw(25.55)
entertainment.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(entertainment)
print(auto)

print(create_spend_chart([food, entertainment, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)