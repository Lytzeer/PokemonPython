from healthbar import HealthBar
from panel import Panel
from character import Character, Salameche, Arcanin, Carapuce, Tortank, Bulbizarre, Florizarre, Ponyta, Psykokwak, Paras
from os import system
from affichage import Affichage
import random


def create_pokemon() -> list:
    pokemon_list = []
    pokemon_list.append(Salameche("Salameche", 100, "fire", {"Flamethrower": 10, "Fire Blast": 20}))
    pokemon_list.append(Arcanin("Arcanin", 100, "fire", {"Flamethrower": 10, "Fire Blast": 20}))
    pokemon_list.append(Ponyta("Ponyta", 100, "fire", {"Flamethrower": 10, "Fire Blast": 20}))
    pokemon_list.append(Carapuce("Carapuce", 100, "water", {"Water Gun": 10, "Hydro Pump": 20}))
    pokemon_list.append(Tortank("Tortank", 100, "water", {"Water Gun": 10, "Hydro Pump": 20}))
    pokemon_list.append(Psykokwak("Psykokwak", 100, "water", {"Water Gun": 10, "Hydro Pump": 20}))
    pokemon_list.append(Bulbizarre("Bulbizarre", 100, "grass", {"Vine Whip": 10, "Razor Leaf": 20}))
    pokemon_list.append(Florizarre("Florizarre", 100, "grass", {"Vine Whip": 10, "Razor Leaf": 20}))
    pokemon_list.append(Paras("Paras", 100, "grass", {"Vine Whip": 10, "Razor Leaf": 20}))
    return pokemon_list

def choose_pokemon(pokemon_list: list) -> list:
    chosen_pokemon = []
    affichage = Affichage()
    affichage.display_character_list(pokemon_list)
    for i in range(2):
        chosen_pokemon.append(pokemon_list[int(input("Choose your pokemon: "))-1])
    return chosen_pokemon

def choose_attack(character: Character) -> str:
    affichage=Affichage()
    affichage.display_attack_list(character.get_attack_list())
    attack = input("Your choice: ")
    if attack in character.get_attack_list():
        return attack
    else:
        return choose_attack(character)
    
def choose_pokemon_bot(pokemon_list: list) -> list:
    chosen_pokemon = []
    randnb = random.randint(0, len(pokemon_list)-1)
    chosen_pokemon.append(pokemon_list[randnb])
    randnb2 = random.randint(0, len(pokemon_list)-1)
    while randnb2 == randnb:
        randnb2 = random.randint(0, len(pokemon_list)-1)
    chosen_pokemon.append(pokemon_list[randnb2])
    return chosen_pokemon
    
def main():
    affichage=Affichage()
    pokemon_list = create_pokemon()
    player_inventory = choose_pokemon(pokemon_list)
    bot_inventory = choose_pokemon_bot(pokemon_list)
    
    