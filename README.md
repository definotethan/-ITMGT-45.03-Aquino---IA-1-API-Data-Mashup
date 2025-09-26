# -ITMGT-45.03-Aquino-IA-1-API-Data-Mashup

# Pokémon API Project

This is a Python program that fetches data from two Pokémon APIs, combines it, and shows the data in a table in the terminal. It handles loading messages, errors, empty results, and lets you retry if something goes wrong.

This project was made with the use of Python and the requests library

## APIs Used

- List Pokémon: https://pokeapi.co/api/v2/pokemon?limit=10
- Pokémon Details: https://pokeapi.co/api/v2/pokemon/{name} (e.g., https://pokeapi.co/api/v2/pokemon/pikachu)
- Pokémon Species Details: https://pokeapi.co/api/v2/pokemon-species/{name} (e.g., https://pokeapi.co/api/v2/pokemon-species/pikachu)
- API documentation: https://pokeapi.co/docs/v2

## How to Setup

1. Clone the repo:
git clone <your-repo-url>
cd <your-folder>

2. Install dependencies:
pip install requests

3. Run the program:
python main.py

## How to Use

Run the program, then it will fetch and show the data. If there is a problem or no data, it will ask if you want to try again or exit through the erminal.

## How Data is Joined

For each Pokémon in the list, the program fetches details from two APIs using the Pokémon's name. It joins the data by matching the name, so all info shows together.

Example:
- For "pikachu", it fetches from /pokemon/pikachu and /pokemon-species/pikachu and combines the stats, type, color, legendary status, and computes HP-to-Weight ratio for the table.

## Limitations

- API rate limits might slow fetching if you request many Pokémon
- Only shows data in the terminal (no graphics)
- Does not support fetching beyond initial limit
- May miss some Pokémon data depending on the APIs

## AI Assistance

This project was developed with some assistance from AI, especially for debugging and cleaning messy code. A specific use case was that I used AI to give me methods that would allow me to test the different errors (API, Empty List and Network Errors). Code and logic were reviewed and adjusted manually.
