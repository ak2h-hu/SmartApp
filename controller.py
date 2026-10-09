def number_of_days(inputFile):
    # Try to open and read the file safely
    try:
        infile = open(inputFile, 'r')
        lines = infile.readlines()
        infile.close()

        # Count the lines to find the total days
        count = 0
        for line in lines:
            count = count + 1

        # Return count minus 1 because the first line is the header
        if count > 0:
            return count - 1
        else:
            return 0
            
    except FileNotFoundError:
        print("Error: The input file was not found.")
        return 0

def auto_calculate(inputFile, outputFile):
    # Try to read the input data safely
    try:
        infile = open(inputFile, 'r')
        lines = infile.readlines()
        infile.close()
    except FileNotFoundError:
        print("Error: The input file was not found. Cannot calculate.")
        return

    # Try to process and write the output data
    try:
        outfile = open(outputFile, 'w')
        is_first_line = True

        for line in lines:
            # Skip the header line
            if is_first_line == True:
                is_first_line = False
                continue

            # Split the string by spaces to get individual values
            parts = line.strip().split(" ")
            
            # Make sure the line has all 5 columns before processing
            if len(parts) >= 5:
                date = parts[0]
                
                try:
                    num_people = int(parts[1])
                    temp_setpoint = float(parts[2])
                    temp_outside = float(parts[3])
                    precip = float(parts[4])
                except ValueError:
                    print("Skipping line due to invalid data format.")
                    continue

                # Rule 1: Boiler Calculation
                temp_difference = temp_setpoint - temp_outside
                if temp_difference >= 20:
                    boiler_value = 100
                elif temp_difference >= 10 and temp_difference < 20:
                    boiler_value = 50
                else:
                    boiler_value = 0

                # Rule 2: Ventilation Calculation
                ventilation_value = num_people + 1
                if ventilation_value > 4:
                    ventilation_value = 4

                # Rule 3: Watering Calculation
                if precip < 3:
                    watering_value = True
                else:
                    watering_value = False

                # Build the output string separated by semicolons
                output_line = date + ";" + str(boiler_value) + ";" + str(ventilation_value) + ";" + str(watering_value) + "\n"
                outfile.write(output_line)

        outfile.close()
        print("Actuators successfully calculated and written to output file.")
        
    except:
        print("An error occurred while creating the output file.")

def overwrite_settings(outputFile):
    try:
        # Ask the user for the overwrite details
        date_to_find = input("Enter the date to overwrite (e.g., 10-10-2026): ")
        system_to_change = input("Enter system to overwrite (Boiler, Ventilation, Watering): ")
        new_value_string = input("Enter the new valid value: ")

        # Make sure the new value is an integer
        try:
            new_value = int(new_value_string)
        except ValueError:
            return -3

        # Check if the new value is allowed for the chosen system
        is_valid_value = False
        if system_to_change == "Boiler":
            if new_value >= 0 and new_value <= 100:
                is_valid_value = True
        elif system_to_change == "Ventilation":
            if new_value >= 0 and new_value <= 4:
                is_valid_value = True
        elif system_to_change == "Watering":
            if new_value == 0 or new_value == 1:
                is_valid_value = True

        # If it violates the boundary rules, return -3 immediately
        if is_valid_value == False:
            return -3

        # Open and read the current output file
        try:
            infile = open(outputFile, 'r')
            lines = infile.readlines()
            infile.close()
        except FileNotFoundError:
            print("Output file not found. Run 'Auto calculate' first.")
            return -1

        date_found = False
        updated_lines = []

        # Iterate through the file to find the specific date
        for line in lines:
            parts = line.strip().split(";")
            
            if len(parts) == 4:
                current_date = parts[0]
                boiler = parts[1]
                vent = parts[2]
                water = parts[3]

                # If the date matches, apply the overwrite logic
                if current_date == date_to_find:
                    date_found = True
                    if system_to_change == "Boiler":
                        boiler = str(new_value)
                    elif system_to_change == "Ventilation":
                        vent = str(new_value)
                    elif system_to_change == "Watering":
                        # Translate the 0 or 1 into False or True for the output
                        if new_value == 1:
                            water = "True"
                        else:
                            water = "False"

                # Reconstruct the line and save it to the updated list
                new_line = current_date + ";" + boiler + ";" + vent + ";" + water + "\n"
                updated_lines.append(new_line)
            else:
                updated_lines.append(line)

        # Write the completely updated list back into the file
        outfile = open(outputFile, 'w')
        for updated_line in updated_lines:
            outfile.write(updated_line)
        outfile.close()

        # Return success or date not found
        if date_found == True:
            return 0
        else:
            return -1

    except:
        return -3

def smart_app_controller():
    # File names used by the controller
    input_file = "input.txt"
    output_file = "output.txt"
    
    keep_running = True
    
    # Run the menu loop
    while keep_running == True:
        print("\n=== Smart App Controller Menu ===")
        print("1) How many days?")
        print("2) Auto calculate all actuators")
        print("3) Overwrite a value")
        print("4) Quit")

        menu_choice = input("Enter your choice (1-4): ")

        if menu_choice == "1":
            days = number_of_days(input_file)
            print("There are", days, "days of data in", input_file)
            
        elif menu_choice == "2":
            auto_calculate(input_file, output_file)
            
        elif menu_choice == "3":
            result = overwrite_settings(output_file)
            if result == 0:
                print("Success: Value overwritten correctly.")
            elif result == -1:
                print("Error (-1): The date was not found in the output file.")
            elif result == -3:
                print("Error (-3): Invalid system chosen or value out of bounds.")
                
        elif menu_choice == "4":
            print("Exiting the Smart App Controller.")
            keep_running = False
            
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")