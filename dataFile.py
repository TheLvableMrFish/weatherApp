# Note: If you encounter an ImportError indicating that matplotlib is not installed,
# you can install it using pip. Run the following command in your terminal or command prompt:
# pip install matplotlib
import matplotlib.pyplot as plt

def plot_weather(dates, max_temps, min_temps):
    # dates = week_data['daily']['time']
    # max_temps = week_data['daily']['temperature_2m_max']
    # min_temps = week_data['daily']['temperature_2m_min']

    # Identify the highest and lowest temperatures over the 7-day forecast
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)

    highest_temp_date = dates[max_temps.index(highest_temp)]
    lowest_temp_date = dates[min_temps.index(lowest_temp)]

    plt.figure(figsize=(10, 5))

    # Plot the max and min temperatures
    plt.plot(dates, max_temps, label='Max Temperature (°F)', marker='o', color='red')
    plt.plot(dates, min_temps, label='Min Temperature (°F)', marker='o', color='blue')

    # Highlight the highest and lowest temperatures
    plt.scatter([highest_temp_date], [highest_temp], color='darkred', label=f'Highest Temp: {highest_temp}°F')
    plt.scatter([lowest_temp_date], [lowest_temp], color='darkblue', label=f'Lowest Temp: {lowest_temp}°F')

    # Chart details
    plt.xlabel('Date')
    plt.ylabel('Temperature (°F)')
    plt.title('7-Day Forecast: High and Low Temperatures')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()