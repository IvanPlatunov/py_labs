import requests
import json
api_id = "a009ef8bc82c0313247855776c5a42429b5c1601a7db8d2db86770977b83f402"
cont = input('Введите код материка: \n AFR - Африка \n ANT - Антарктида \n ASIA - Азия \n AUS - Австралия \n EUR - Европа \n NAR - Северная Америка \n SAR - Южная америка \n')
lim = input('Сколько событий вы хотели бы посмотреть? ')
resp_disaster = requests.get(f"https://api.ambeedata.com/disasters/latest/by-continent?continent={cont}&page=1&limit={lim}&x-api-key={api_id}")
disaster_data = resp_disaster.json()
print(disaster_data)
for i in range(int(lim)):
    print("-"*50)
    print("Название события -", disaster_data["result"][i]["event_name"])
    print("Время события -", disaster_data["result"][i]["date"])
    print("Код страны -", disaster_data["result"][i]["country_code"])
    print("Широта -", disaster_data["result"][i]["lat"])
    print("Долгота -", disaster_data["result"][i]["lng"])