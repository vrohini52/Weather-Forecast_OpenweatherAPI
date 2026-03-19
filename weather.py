import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

api_key = "92bac66084657b12ee8a93b11129c2a5"

file_name = "history.csv"

# Weather function
def get_weather():
    
    city = input("Enter city: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    print(data)
    if data.get("cod") == 200:

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\nCity:", city)
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity)
        print("Weather:", weather)

        save_history(city,temp,humidity,weather)

    else:
        print("Error:", data.get("message"))


# Save history using pandas
def save_history(city,temp,humidity,weather):

    df  = pd.DataFrame([[city,temp,humidity,weather]],
                      columns=["City","Temperature","Humidity","Weather"])

    if os.path.exists(file_name):
        df.to_csv(file_name, mode="a",header=False,index=False)
    else:
        df.to_csv(file_name,index=False)


# View history
def view_history():

    if os.path.exists(file_name):

        df = pd.read_csv(file_name)
        print("\nSearch History\n")
        print(df)

    else:
        print("No history found.")


# Temperature graph
def show_graph():

    if os.path.exists(file_name):

        df = pd.read_csv(file_name)

        plt.figure()

        plt.bar(df["City"],df["Temperature"])

        plt.title("Temperature by City")

        plt.xlabel("City")

        plt.ylabel("Temperature °C")

        plt.show()

    else:
        print("No data available")


# Menu system
while True:

    print("\n====== Weather App ======")
    print("1. Search Weather")
    print("2. View History")
    print("3. Show Temperature Graph")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        get_weather()

    elif choice == "2":
        view_history()

    elif choice == "3":
        show_graph()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid choice")