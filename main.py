import requests
import weather
import controller


def show_utrecht_temperature():
    # Set the Open-Meteo URL using Utrecht's latitude and longitude
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current_weather=true"

    try:
        print("Connecting to Open-Meteo API...")
        # Send a GET request to the API
        response = requests.get(api_url)

        # Convert the JSON response to a Python dictionary
        weather_data = response.json()

        # Extract the temperature from the dictionary
        current_temp = weather_data["current_weather"]["temperature"]
        print("The current temperature in Utrecht is:", current_temp, "°C")

    except:
        # A broad except block to catch network or dictionary errors
        print("An error occurred while fetching the weather data.")


def main():
    keep_running = True

    while keep_running == True:
        print("\n===== Main Application Platform =====")
        print("1) Run Weather Station")
        print("2) Run Smart App Controller")
        print("3) Show Current Temperature in Utrecht")
        print("4) Quit Platform")

        menu_choice = input("Select an option (1-4): ")

        if menu_choice == "1":
            weather.weerstation()
        elif menu_choice == "2":
            controller.smart_app_controller()
        elif menu_choice == "3":
            show_utrecht_temperature()
        elif menu_choice == "4":
            print("Goodbye!")
            keep_running = False
        else:
            print("Invalid input. Please enter a number from 1 to 4.")


# Simply call the main function to start the program
main()