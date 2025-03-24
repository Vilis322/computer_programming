import requests


def get_weather(city_name):
    url = f"https://wttr.in/{city_name}?format=%C+%t"

    response = requests.get(url)

    if response.status_code == 200:
        description, temperature = response.text.rsplit(" ", 1)
        print(f"Weather in {city_name}: {description}, {temperature}")
    else:
        print("Ошибка при получении данных")


get_weather(input("Enter the city: ").strip().capitalize())
