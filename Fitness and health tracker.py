import matplotlib.pyplot as plt

tracker_data = []
def input_data():
    date = input("Enter today's date (YYYY-MM-DD): ")
    steps = int(input("How many steps did you take today? "))
    calories = int(input("How many calories did you consume today? "))
    water = float(input("How many liters of water did you drink today? "))

    daily_data = {
        'Date': date,
        'Steps': steps,
        'Calories': calories,
        'Water': water
    }
    tracker_data.append(daily_data)

def display_data():
    print("\nFitness and Health Tracker Summary:")
    if len(tracker_data) == 0:
        print("No data entered yet!")
    else:
        for entry in tracker_data:
            print(f"Date: {entry['Date']}")
            print(f"Steps Taken: {entry['Steps']} steps")
            print(f"Calories Consumed: {entry['Calories']} kcal")
            print(f"Water Consumed: {entry['Water']} liters")
            print("-" * 30)

def plot_data():
    if len(tracker_data) == 0:
        print("No data to plot!")
        return
    
    dates = [entry['Date'] for entry in tracker_data]
    steps = [entry['Steps'] for entry in tracker_data]
    calories = [entry['Calories'] for entry in tracker_data]
    water = [entry['Water'] for entry in tracker_data]

    # 1.Plot Steps Data 
    plt.figure(figsize=(10, 6))
    plt.bar(dates, steps, color='blue')
    plt.title('Steps Taken Each Day')
    plt.xlabel('Date')
    plt.ylabel('Steps')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  

    # 2.Plot Calories Data
    plt.figure(figsize=(10, 6))
    plt.bar(dates, calories, color='red')
    plt.title('Calories Consumed Each Day')
    plt.xlabel('Date')
    plt.ylabel('Calories (kcal)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  

    # 3.Plot Water Intake Data 
    plt.figure(figsize=(10, 6))
    plt.bar(dates, water, color='green')
    plt.title('Water Intake Each Day')
    plt.xlabel('Date')
    plt.ylabel('Water (liters)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
def main():
    while True:
        print("\nFitness and Health Tracker")
        print("1. Enter today's data")
        print("2. View all data")
        print("3. View Graph")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            input_data()  
        elif choice == '2':
            display_data()  
        elif choice == '3':
            plot_data() 
        elif choice == '4':
            print("Exiting the program. Stay healthy!")
            break  
        else:
            print("Invalid choice! Please try again.")

main()
