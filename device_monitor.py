def get_initial_readings(readings):
    readings = [28, 31, 35, 37, 29]
    return readings


def classify_reading(reading):
    if reading < 30:
        return "NORMAL"
    elif reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def display_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print("Reading " + str(index + 1) + ": "
              + str(readings[index]) + " °C")


def add_reading(readings):
    new_reading = input("Enter temperature reading: ")

    if new_reading == "":
        print("Invalid input. The reading cannot be empty.")
    elif not new_reading.isdigit():
        print("Invalid input. Enter a whole number only.")
    else:
        temperature = int(new_reading)

        if temperature < 0 or temperature > 100:
            print("Invalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(temperature)
            print("Reading added successfully.")


def display_classifications(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        print(str(reading) + " °C -> " + classify_reading(reading))


def compute_total(readings):
    total = 0

    for reading in readings:
        total += reading

    return total


def compute_average(readings):
    if len(readings) == 0:
        return 0

    return compute_total(readings) / len(readings)


def find_minimum(readings):
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, category):
    count = 0

    for reading in readings:
        if classify_reading(reading) == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    print("\nMONITORING SUMMARY")
    print("------------------")

    if len(readings) == 0:
        print("No readings available.")
        return

    number = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, "NORMAL")
    warning_count = count_category(readings, "WARNING")
    critical_count = count_category(readings, "CRITICAL")

    print("Number of readings  :", number)
    print("Total of readings   :", total)
    print("Average temperature : {:.2f} °C".format(average))
    print("Minimum temperature :", minimum, "°C")
    print("Maximum temperature :", maximum, "°C")

    print()
    print("NORMAL   : {} ({:.2f}%)".format(
        normal_count, normal_count / number * 100))
    print("WARNING  : {} ({:.2f}%)".format(
        warning_count, warning_count / number * 100))
    print("CRITICAL : {} ({:.2f}%)".format(
        critical_count, critical_count / number * 100))

    status = determine_overall_status(warning_count, critical_count)
    print("\nOverall Status:", status)


def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    readings = []
    readings = get_initial_readings(readings)

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            display_classifications(readings)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()

    