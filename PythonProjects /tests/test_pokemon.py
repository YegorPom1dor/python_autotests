import requests

# Базовый URL и хедеры для запросов
base_url = "https://api.pokemonbattle.ru"
headers = {
    "Content-Type": "application/json",
    "trainer_token": "token"
}

def test_get_pokemons_status_code():
    # Запрос GET /v2/pokemons с параметром trainer_id
    trainer_id = 4631
    response = requests.get(f"{base_url}/v2/pokemons", headers=headers, params={"trainer_id": trainer_id})
    
    # Проверка, что статус-код ответа 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

#Проверь, что в ответе приходит строчка с именем твоего тренера
def test_trainer_name_in_pokemons_response():
    response_get: requests.get(base_url = f'{base_url}/v2/trainers', params = {'trainer_id' : trainer_id})