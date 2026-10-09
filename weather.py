def Fahrenheit(temp_celcius):
    # Convert the temperature from Celsius to Fahrenheit
    temperature_fahrenheit = (temp_celcius * 9 / 5) + 32
    return temperature_fahrenheit

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    # Calculate the wind chill using the provided formula
    wind_chill = temp_celcius - (luchtvochtigheid / 100 * windsnelheid)
    return wind_chill

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    # First, get the wind chill using the other function
    wind_chill = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    # Use the decision rules to determine the weather description
    if wind_chill < 0 and windsnelheid > 10:
        return "It is very cold and stormy! Turn the heating all the way up!"
    elif wind_chill < 0 and windsnelheid <= 10:
        return "It is quite cold! Turn on the heating on the ground floor!"
    elif wind_chill >= 0 and wind_chill < 10 and windsnelheid > 12:
        return "It is quite cold and windy; turn on the heating and close the vents!"
    elif wind_chill >= 0 and wind_chill < 10 and windsnelheid <= 12:
        return "It’s a bit cold, turn on the electric heater downstairs!"
    elif wind_chill >= 10 and wind_chill < 22:
        return "Lovely weather, not too cold or too warm."
    else:
        return "Hot! Turn on the air conditioning!"

def weerstation():
    total_temperature = 0
    days_entered = 0

    print("=== Welcome to the Weather Station ===")
    
    # Loop for a maximum of 7 days
    while days_entered < 7:
        print("--- Entering data for Day", days_entered + 1, "---")

        # Get temperature with error handling so the user can try again
        while True:
            temp_input = input("Temperature in degrees Celsius (press Enter to stop): ")
            if temp_input == "":
                print("Empty input received. Terminating weather station.")
                return 

            try:
                temp_celcius = float(temp_input)
                break 
            except ValueError:
                print("Invalid input. Please enter a valid number for the temperature.")

        # Get wind speed with error handling
        while True:
            wind_input = input("Wind speed in meters per second (press Enter to stop): ")
            if wind_input == "":
                print("Empty input received. Terminating weather station.")
                return 

            try:
                windsnelheid = float(wind_input)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the wind speed.")

        # Get humidity with error handling
        while True:
            humidity_input = input("Humidity as a whole percentage 0-100 (press Enter to stop): ")
            if humidity_input == "":
                print("Empty input received. Terminating weather station.")
                return 

            try:
                luchtvochtigheid = int(humidity_input)
                if luchtvochtigheid >= 0 and luchtvochtigheid <= 100:
                    break
                else:
                    print("The percentage must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a whole number for the humidity.")

        # Add to the running total and calculate the average
        total_temperature = total_temperature + temp_celcius
        days_entered = days_entered + 1
        average_temperature = total_temperature / days_entered

        # Get the Fahrenheit conversion and the weather report string
        temp_fahrenheit = Fahrenheit(temp_celcius)
        report = weerrapport(temp_celcius, windsnelheid, luchtvochtigheid)

        # Output the daily summary
        print("Temperature:", temp_celcius, "°C /", temp_fahrenheit, "°F")
        print("Weather description:", report)
        print("Average temperature so far:", average_temperature, "°C")
        print("--------------------------------------------------")

    print("Maximum of 7 days reached. Terminating weather station.")