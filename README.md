# -ITMGT-45.03-Aquino---IA-1-API-Data-Mashup

# Pokémon API Project

This is a Python program that fetches data from two Pokémon APIs, combines it, and shows the data in a table in the terminal. It handles loading messages, errors, empty results, and lets you retry if something goes wrong.

## About

The project fetches Pokémon details and Pokémon species info from two different APIs. It joins this data, calculates extra info like HP-to-Weight ratio, and shows it in the terminal.

It also deals with errors like no internet, empty results, or fetch failures by asking the user if they want to retry.

## Tech Used

- Python 3
- requests library

## Features

- Fetches a list of Pokémon (you choose how many)
- Fetches stats and species info separately and joins them
- Calculates an HP-to-Weight ratio
- Shows loading, error, and empty messages
- Lets user retry on errors or empty data
- Displays a formatted table in the terminal

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

The program fetches data from two APIs for each Pokémon name. It matches and joins the data by the Pokémon’s name so all info shows together.

## Limitations

- API rate limits might slow fetching if you request many Pokémon
- Only shows data in the terminal (no graphics)
- Does not support fetching beyond initial limit
- May miss some Pokémon data depending on the APIs
