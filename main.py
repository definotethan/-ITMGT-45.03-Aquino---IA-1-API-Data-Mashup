import requests
import time

def fetch_pokemon_list(limit=10):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}')
        if response.status_code != 200:
            print("Error fetching Pokémon list.")
            return None
        pokemon_list = response.json()['results']
        return pokemon_list if pokemon_list else []
    except Exception as e:
        print(f"Network error: {e}")
        return None

def fetch_pokemon_data(name):
    try:
        poke_resp = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        species_resp = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{name}')
        if poke_resp.status_code != 200 or species_resp.status_code != 200:
            return None, None
        return poke_resp.json(), species_resp.json()
    except Exception as e:
        print(f"Error fetching data for {name}: {e}")
        return None, None

def display_table(pokemons):
    print(f"{'Name':<12} {'Type':<10} {'Weight':<8} {'Color':<10} {'Legendary':<10} {'HP/Weight':<10}")
    print('-' * 60)
    for p in pokemons:
        name = p['name']
        poke_data, species_data = fetch_pokemon_data(name)
        if not poke_data or not species_data:
            print(f"Skipped {name} due to fetch error.")
            continue
        poke_type = poke_data['types'][0]['type']['name']
        weight = poke_data['weight']
        hp = next(stat['base_stat'] for stat in poke_data['stats'] if stat['stat']['name'] == 'hp')
        color = species_data['color']['name']
        is_legendary = 'Yes' if species_data['is_legendary'] else 'No'
        hp_weight_ratio = round(hp / weight, 2) if weight else 'N/A'
        print(f"{name.capitalize():<12} {poke_type:<10} {weight:<8} {color:<10} {is_legendary:<10} {hp_weight_ratio:<10}")
        time.sleep(0.5)

while True:
    print("Loading Pokémon list...")
    pokemons = fetch_pokemon_list(limit=10)
    if pokemons is None:
        retry = input("Failed to load Pokémon list. Retry? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting program.")
            break
        continue
    if not pokemons:
        retry = input("No Pokémon found. Retry? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting program.")
            break
        continue
    print("Pokémon loaded successfully!")
    display_table(pokemons)
    break

