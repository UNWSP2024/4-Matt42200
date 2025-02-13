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