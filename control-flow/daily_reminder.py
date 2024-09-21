task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound  = input("Is it time-bound? (yes/no): ").lower()

match time_bound:
    case 'yes':
        if priority == 'high':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif priority == 'medium':
             print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif priority == 'low':
             print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print("Invalid option!!! ")
    case 'no':
        if priority == 'high':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        elif priority == 'medium':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        elif priority == 'low':
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Invalid option!!! ")