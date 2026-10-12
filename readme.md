# Breez 🌤️
**Smart weather. Smarter living.**

Breez is a Python-based platform designed for environmental data logging and automated smart home actuator control. This project was developed as a three-sprint computer science school assignment, demonstrating fundamental programming concepts such as control structures, file I/O operations, and REST API integration.

## 🚀 Features

### 1. Weather Station (Sprint 1)
A console-based data entry system that allows users to log daily weather conditions (up to 7 days). It calculates:
*   Temperature conversions (Celsius to Fahrenheit).
*   Wind chill factor.
*   Dynamic weather reports and heating recommendations based on decision rules.
*   Running average temperatures.

### 2. Smart App Controller (Sprint 2)
An automated system that reads environmental data from an input file and calculates optimal settings for smart home hardware:
*   **Boiler:** Adjusts capacity (0%, 50%, 100%) based on the difference between outside and target temperatures.
*   **Ventilation:** Adjusts fan speed based on the number of people in the house.
*   **Watering:** Activates garden sprinklers if rainfall is below a specific threshold.
*   **Manual Override:** Allows users to manually safely overwrite calculated actuator values for specific dates in the output file.

### 3. Live Platform Integration (Sprint 3)
A unified Command Line Interface (CLI) menu that ties all modules together. It also features a live connection to the **Open-Meteo API** to fetch and display the current real-time temperature in Utrecht.

---

## 📁 File Structure

*   `main.py`: The entry point of the application containing the main menu and the API connection.
*   `weather.py`: Contains the logic and data entry loops for the Weather Station.
*   `controller.py`: Contains the file reading, writing, and override logic for the Smart App Controller.
*   `input.txt`: The source data file read by the controller (space-separated values).
*   `output.txt`: The generated file containing actuator instructions (semicolon-separated values).

---

## 🛠️ Setup and Usage

1. **Prerequisites:** Make sure you have Python 3 installed on your computer.
2. **Install Dependencies:** The live weather feature requires the `requests` library. Install it via your terminal/command prompt:
   ```bash
   pip install requests
   ```
3. **Prepare Input Data:** Ensure you have an `input.txt` file in the same folder as your scripts. It should look like this:
   ```text
   date numPeople tempSetpoint tempOutside precip
   10-10-2026 3 21.0 10.5 0.0
   11-10-2026 2 20.0 2.0 4.5
   12-10-2026 5 22.0 15.0 1.0
   ```
4. **Run the App:** Execute the main script from your terminal:
   ```bash
   python main.py
   ```

---

## 🤝 Credits & Acknowledgements

*   **Daan van Oort** - For the great help, feedback, and support during development!
*   **Gemini** - For assistance with code structure, debugging, and polishing the Breez platform.