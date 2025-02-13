2. 
total_tickets = 0


while True:
    movie_name = input("Enter the movie name (or type 'done' to finish): ")
    
    if movie_name.lower() == 'done':
        break
    
    try:
        tickets = int(input(f"How many tickets for '{movie_name}'? "))
        if tickets < 0:
            print("Please enter a positive number.")
            continue
        total_tickets += tickets
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue


print(f"\nTotal number of tickets desired: {total_tickets}")


3.
num_years = int(input("Enter the number of years: "))


total_rainfall = 0
total_months = num_years * 12  # Each year has 12 months


for year in range(1, num_years + 1):
    print(f"\nYear {year}:")
        for month in range(1, 13):
        while True:
            try:
                rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
                if rainfall < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_rainfall += rainfall
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")


average_rainfall = total_rainfall / total_months


print("\nRainfall Data Summary:")
print(f"Total months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")




4.
BEGIN
    DISPLAY "Enter your budget for the month:"
    INPUT budget


    SET total_expenses = 0


    REPEAT
        DISPLAY "Enter an expense amount (or enter -1 to finish):"
        INPUT expense


        IF expense != -1 THEN
            total_expenses = total_expenses + expense
        ENDIF
    UNTIL expense == -1


    SET remaining_budget = budget - total_expenses


    DISPLAY "Total expenses: ", total_expenses
    DISPLAY "Remaining budget: ", remaining_budget


    IF remaining_budget > 0 THEN
        DISPLAY "You are under budget by ", remaining_budget
    ELSEIF remaining_budget < 0 THEN
        DISPLAY "You are over budget by ", ABS(remaining_budget)
    ELSE
        DISPLAY "You have exactly met your budget."
    ENDIF
END


5.
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