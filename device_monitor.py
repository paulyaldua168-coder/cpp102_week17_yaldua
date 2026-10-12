readings = [28, 31, 35, 37, 29]

def view_readings():
    """Display all stored temperature readings"""
    print("\n---Device Readings---")
    for reading in readings:
        print(f"{reading}°C")

def add_readings():
    """Ask the user for the reading and add it to the list"""
    
    reading = int(input("Enter temperature reading: "))
    readings.append(reading)
    print("Reading added successfully")

def main_menu():
    """Display the MAIN MENU and PROCESS under the user's choice"""
    choice=""

    while choice!="5":
        print("\n---SIMULATED DEVICE MONITORING SYSTEM---")
        print("-----------------------------------------")
        print("[1] View Readings")
        print("[2] Add Readings")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")

    choice = input("\nEnter choice: ")

    if choice=="1":
        view_readings()

    elif choice=="2":
        add_readings()

    elif choice=="2":
        u

    elif choice=="2":
        u

    elif choice=="2":
        u
     
    else:
        print("Invalid choice. Please select 1-5")
    
if name == "__main__":
    main()

    