budget = float(input("Enter your budget for the month: $"))


total_expenses = 0.0


while True:
    try:
        expense = float(input("Enter an expense amount (or enter -1 to finish): "))
        if expense == -1:
            break
        if expense < 0:
            print("Please enter a valid positive expense amount.")
            continue
        total_expenses += expense
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


remaining_budget = budget - total_expenses


print("\nBudget Analysis:")
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining budget: ${remaining_budget:.2f}")


if remaining_budget > 0:
    print(f"You are under budget by ${remaining_budget:.2f}. Great job!")
elif remaining_budget < 0:
    print(f"You are over budget by ${abs(remaining_budget):.2f}. Consider reducing expenses.")
else:
    print("You have exactly met your budget.")