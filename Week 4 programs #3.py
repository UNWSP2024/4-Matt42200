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