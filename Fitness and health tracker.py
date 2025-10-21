import matplotlib.pyplot as plt

tracker_data = []
goals = {'Steps': 8000, 'Calories': 2000, 'Water': 2.0}  # default goals

def set_goals():
    print("\n--- Set Your Daily Fitness Goals ---")
    goals['Steps'] = int(input("Enter daily steps goal: "))
    goals['Calories'] = int(input("Enter daily calorie limit: "))
    goals['Water'] = float(input("Enter daily water intake goal (liters): "))
    print("Goals updated successfully.\n")

def input_data():
    date = input("Enter today's date (YYYY-MM-DD): ")
    steps = int(input("How many steps did you take today? "))
    calories = int(input("How many calories did you consume today? "))
    water = float(input("How many liters of water did you drink today? "))

    # Estimate calories burned based on steps
    calories_burned = round(steps * 0.04, 2)

    daily_data = {
        'Date': date,
        'Steps': steps,
        'Calories': calories,
        'Water': water,
        'Calories Burned': calories_burned
    }
    tracker_data.append(daily_data)
    print(f"\nData added for {date} successfully.\n")

def display_data():
    print("\nFitness and Health Tracker Summary:")
    if len(tracker_data) == 0:
        print("No data entered yet.")
        return

    for entry in tracker_data:
        print(f"\nDate: {entry['Date']}")
        print(f"Steps Taken: {entry['Steps']} steps (Goal: {goals['Steps']})")
        print(f"Calories Consumed: {entry['Calories']} kcal (Goal: {goals['Calories']})")
        print(f"Water Consumed: {entry['Water']} liters (Goal: {goals['Water']})")
        print(f"Calories Burned (approx): {entry['Calories Burned']} kcal")
        print("Goals Met:")
        print(f"   Steps: {'Yes' if entry['Steps'] >= goals['Steps'] else 'No'}")
        print(f"   Calories: {'Yes' if entry['Calories'] <= goals['Calories'] else 'No'}")
        print(f"   Water: {'Yes' if entry['Water'] >= goals['Water'] else 'No'}")
        print("-" * 40)

def show_statistics():
    if len(tracker_data) == 0:
        print("No data available for statistics.")
        return

    total_steps = sum(d['Steps'] for d in tracker_data)
    total_calories = sum(d['Calories'] for d in tracker_data)
    total_water = sum(d['Water'] for d in tracker_data)
    total_burned = sum(d['Calories Burned'] for d in tracker_data)
    n = len(tracker_data)

    avg_steps = total_steps / n
    avg_calories = total_calories / n
    avg_water = total_water / n

    best_day = max(tracker_data, key=lambda x: x['Steps'])
    lowest_cal_day = min(tracker_data, key=lambda x: x['Calories'])

    print("\nWeekly Progress Summary:")
    print(f"Total Days Tracked: {n}")
    print(f"Average Steps: {avg_steps:.0f}")
    print(f"Average Calories: {avg_calories:.0f}")
    print(f"Average Water Intake: {avg_water:.2f} L")
    print(f"Total Calories Burned: {total_burned:.0f} kcal")
    print(f"Best Day (Most Steps): {best_day['Date']} with {best_day['Steps']} steps")
    print(f"Lowest Calorie Day: {lowest_cal_day['Date']} with {lowest_cal_day['Calories']} kcal\n")

def plot_data():
    if len(tracker_data) == 0:
        print("No data to plot.")
        return
    
    dates = [entry['Date'] for entry in tracker_data]
    steps = [entry['Steps'] for entry in tracker_data]
    calories = [entry['Calories'] for entry in tracker_data]
    water = [entry['Water'] for entry in tracker_data]
    burned = [entry['Calories Burned'] for entry in tracker_data]

    # Steps
    plt.figure(figsize=(10, 6))
    plt.bar(dates, steps, color='blue')
    plt.axhline(goals['Steps'], color='gray', linestyle='--', label='Goal')
    plt.title('Steps Taken Each Day')
    plt.xlabel('Date')
    plt.ylabel('Steps')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Calories
    plt.figure(figsize=(10, 6))
    plt.bar(dates, calories, color='red')
    plt.axhline(goals['Calories'], color='gray', linestyle='--', label='Calorie Limit')
    plt.title('Calories Consumed Each Day')
    plt.xlabel('Date')
    plt.ylabel('Calories (kcal)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Water
    plt.figure(figsize=(10, 6))
    plt.bar(dates, water, color='green')
    plt.axhline(goals['Water'], color='gray', linestyle='--', label='Goal')
    plt.title('Water Intake Each Day')
    plt.xlabel('Date')
    plt.ylabel('Water (liters)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Calories Burned
    plt.figure(figsize=(10, 6))
    plt.plot(dates, burned, marker='o', color='purple')
    plt.title('Calories Burned from Steps')
    plt.xlabel('Date')
    plt.ylabel('Calories Burned (kcal)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\n=== Fitness and Health Tracker ===")
        print("1. Set daily goals")
        print("2. Enter today's data")
        print("3. View all data")
        print("4. View progress summary")
        print("5. View graphs")
        print("6. Exit")

        choice = input("Choose an option (1–6): ")

        if choice == '1':
            set_goals()
        elif choice == '2':
            input_data()
        elif choice == '3':
            display_data()
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            plot_data()
        elif choice == '6':
            print("Exiting the program. Stay healthy.")
            break
        else:
            print("Invalid choice. Try again.")

main()
