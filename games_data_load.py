import django
import os
import requests
import xml.etree.ElementTree as ET
from review_site.models import Game

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board_game_chronicle.settings')
django.setup()



def search_game(game_name):
    search_url = f"https://boardgamegeek.com/xmlapi/search?search={game_name}&exact=1"
    response = requests.get(search_url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to retrieve data from API")

def parse_search_response(xml_data):
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    games = []
    for game in root.findall('boardgame'):
        game_data = {
            'id': game.attrib['objectid'],
            'name': game.find('name').text
        }
        games.append(game_data)

    return games

def get_game_details(game_id):
    game_details_url = f"https://boardgamegeek.com/xmlapi/boardgame/{game_id}"
    response = requests.get(game_details_url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to retrieve data from API")

def parse_game_details(xml_data):
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    for game in root.findall('boardgame'):
        game_data = {
            'id': game.attrib['objectid'],
            'game_name': game.find('name').text,
            'description': game.find('description').text if game.find('description') is not None else None,
            'min_players': game.find('minplayers').text if game.find('minplayers') is not None else None,
            'max_players': game.find('maxplayers').text if game.find('maxplayers') is not None else None,
            'playing_time': game.find('maxplaytime').text if game.find('maxplaytime') is not None else None,
            'image': game.find('image').text if game.find('image') is not None else None
        }
        return game_data

def main():

    games = ["Shasn", "Gloomhaven", "King of Tokyo", "Kemet", "The Settlers of Catan", "Evolution: Climate", "Onitama", "Everdell", "Munchkin", "Dobble", "Trial by Trolley", "Hanabi", "Heat", "Scout", "Twilight Imperium: Fourth Edition", "Oath", "Wingspan", "Scythe", "Root", "Pandemic", "Azul", "Dominion", "Ticket to Ride", "Unmatched Game System", "Splendor", "Galaxy Trucker", "Cryptid", "Hive", "Dixit", "Love Letter"]
    data = []
    for game in games:
        search_response = search_game(game)

        
        games = parse_search_response(search_response)

        game_id = games[0]["id"]

         
        game_details_response = get_game_details(game_id)

       
        game_details = parse_game_details(game_details_response)
        
        
        Game.objects.update_or_create(
            id=game_details['id'],
            defaults={
                'game_name': games[0]['name'],
                'description': game_details['description'],
                'min_players': game_details['min_players'],
                'max_players': game_details['max_players'],
                'playing_time': game_details['playing_time'],
                'image': game_details['image']
            }
        )
        
if __name__=='__main__':
    main()

