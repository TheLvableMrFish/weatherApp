# Team Memebers:
# Anthony Tahan
# Cayla Holthaus
# Christian Pagano
# Todd Kemmerer
# Sheba Coble

# Note: If you encounter an ImportError indicating that matplotlib is not installed,
# you can install it using pip. Run the following command in your terminal or command prompt:
# pip install matplotlib

# tkinter is a gui library
import tkinter as tk

from api import get_coordinates, get_current_weather, get_weeks_weather, get_dates

from celciusToFahrenheit import Temperature_Converter

from date import convert_dates_to_weekdays

from dataFile import plot_weather

from excel import write_to_excel

def weather_gui():
    # Get our city name from GUI form
    city = entry.get()

    # Gets cords from api using function from api.py
    # this allows us to use the city name for the cords of a city
    # and use them to collect weather data from the api open-meteo
    city_cords = get_coordinates(city)

    # Calls for the data that we extract the high/low temps for the week
    city_week_data = get_weeks_weather(city_cords[0], city_cords[1])

    # Gets the current weather and converts it using the function from api and then the function from celciusToFahrenheit
    current_weather = Temperature_Converter(get_current_weather(city_cords[0], city_cords[1])['current_weather']['temperature'])

    # Sets the values for the temps from the data collected from the api
    city_high_temps = city_week_data['daily']['temperature_2m_max']
    city_low_temps = city_week_data['daily']['temperature_2m_min']

    # Creates empty placeholder lists for the temperatures
    city_high_temps_converted = []
    city_low_temps_converted = []

    # Uses for loops convert temps from C to F from function in celciusToFahrenheit.py 
    for temps in city_high_temps:
        city_high_temps_converted.append(Temperature_Converter(temps))

    for temps in city_low_temps:
        city_low_temps_converted.append(Temperature_Converter(temps))

    # Clean the GUI
    for widget in frame.winfo_children():
        widget.destroy()
    
    if start_btn.winfo_exists:
        start_btn.destroy()
    
    # Display city name
    city_label = tk.Label(frame, text=f"Weather in {city}", font=("Helvetica", 16))
    city_label.grid(row=0, columnspan=7, pady=(0, 10))

    # Creates empty placeholder lists for the days of the week
    days = []

    # Calls the api for the dates of the weather in "YYYY-MM-DD" format with function from api.py
    city_dates = get_dates(city_cords[0], city_cords[1])['daily']['time']

    # Ues date.py's function to convert the dates to corresponding weekdays
    # inside it uses [:3] to splice the first 3 letters from each weekday
    for day in city_dates:
        days.append(convert_dates_to_weekdays(day)[:3])

    # Loops through our list of days of the week and high/low temps for gui
    for i, day in enumerate(days):

        # Create a label for each temperature
        day_label = tk.Label(frame, text=day, borderwidth=2, relief="groove", width=10, height=2)
        # This creates the 2rd row for the temps and the column is created for day value
        day_label.grid(row=1, column=i, padx=5, pady=5)

        # Create a label for each temperature
        temp_label = tk.Label(frame, text=f"{city_high_temps_converted[i]:.1f}/{city_low_temps_converted[i]:.1f}F°", borderwidth=2, relief="groove", width=10, height=2)
        # This creates the 3rd row for the temps and the column is created for each temp high/low value
        temp_label.grid(row=2, column=i, padx=5, pady=5)
    
    download_btn = tk.Button(frame, text=f"Download", command=lambda: write_to_excel(city, current_weather, city_high_temps_converted, city_low_temps_converted))
    download_btn.grid(row=3, column=1, padx=5, pady=5)

    show_weather_btn = tk.Button(frame, text=f"Show Weather", command=weather_gui)
    show_weather_btn.grid(row=3, column=3, padx=5, pady=5)

    show_graph_btn = tk.Button(frame, text=f"Show Chart", command=lambda: plot_weather(days, city_high_temps_converted, city_low_temps_converted))
    show_graph_btn.grid(row=3, column=5, padx=5, pady=5)
    
# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create an Entry widget for city input
entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

# Create a Button widget to show weather
start_btn = tk.Button(root, text="Show Weather", command=weather_gui)
start_btn.pack(padx=10, pady=20)

# Create a frame to hold the weather data grid
frame = tk.Frame(root)
frame.pack(padx=40, pady=20)

# Start the Tkinter event loop
root.mainloop()