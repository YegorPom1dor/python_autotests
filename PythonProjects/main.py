import requests

# URL и хедеры для запросов
base_url = "https://api.pokemonbattle.ru/v2/"
headers = {
    "Content-Type": "application/json",
    "trainer_token": "token" #токен тренера
}

# 1. Создание покемона
create_pokemon_data = {
    "name": "Бульбазавр",
    "photo_id": 1
}

create_response = requests.post(f"{base_url}pokemons", headers=headers, json=create_pokemon_data)
print("Создание покемона:")
print(create_response.json())

# 2. Смена имени покемона
update_pokemon_data = {
    "pokemon_id": pokemon_id,  # Используем ID покемона
    "name": "Иви"
}

update_response = requests.put(f"{base_url}pokemons", headers=headers, json=update_pokemon_data)
print("\nСмена имени покемона:")
print(update_response.json())

# 3. Поймать покемона в покебол
catch_pokemon_data = {
    "pokemon_id": pokemon_id  # Используем тот же ID покемона
}

catch_response = requests.post(f"{base_url}trainers/add_pokeball", headers=headers, json=catch_pokemon_data)
print("\nПоймать покемона в покебол:")
print(catch_response.json())