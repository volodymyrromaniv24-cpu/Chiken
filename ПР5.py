import requests


def get_country_info():
    print("=== Пошук інформації про країни ===")

    country = input("Введіть назву країни англійською (наприклад, Ukraine, Japan, Canada): ")


    url = f"https://restcountries.com/v3.1/name/{country}"

    print("Надсилаємо запит до сервера...\n")

    response = requests.get(url)


    if response.status_code == 200:

        data = response.json()[0]


        name = data.get('name', {}).get('official', 'Невідомо')
        capital = data.get('capital', ['Невідомо'])[0]
        population = data.get('population', 'Невідомо')
        region = data.get('region', 'Невідомо')


        print("--- Результат ---")
        print(f"Офіційна назва: {name}")
        print(f"Столиця: {capital}")
        print(f"Населення: {population} осіб")
        print(f"Регіон: {region}")
        print("-----------------")

    elif response.status_code == 404:

        print("[Помилка 404] Країну не знайдено. Перевірте правильність написання.")
    else:

        print(f"[Помилка] Запит не вдався. Статус-код: {response.status_code}")


if __name__ == "__main__":
    get_country_info()