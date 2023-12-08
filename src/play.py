from character import Character, Salameche, Arcanin, Carapuce, Tortank, Bulbizarre, Florizarre, Ponyta, Psykokwak, Paras
from affichage import Affichage
from rich import print
import random
import os
import logging


def create_pokemon_list() -> list:
    pokemon_list = []
    pokemon_list.append("Salameche")
    pokemon_list.append("Arcanin")
    pokemon_list.append("Ponyta")
    pokemon_list.append("Carapuce")
    pokemon_list.append("Tortank")
    pokemon_list.append("Psykokwak")
    pokemon_list.append("Bulbizarre")
    pokemon_list.append("Florizarre")
    pokemon_list.append("Paras")
    logging.info("Pokemon list created")
    return pokemon_list

def create_all_pokemon_stats() -> dict:
    pokemon_stats = {}
    pokemon_stats["Salameche"] = {"HP": 285, "Type": "fire", "Attack List": {"Ember": [40, 100], "Fire Spin": [60, 80]}}
    pokemon_stats["Arcanin"] = {"HP": 380, "Type": "fire", "Attack List": {"Fire Fang": [45, 95], "Flare Blitz": [70, 85]}}
    pokemon_stats["Ponyta"] = {"HP": 330, "Type": "fire", "Attack List": {"Fire Spin": [35, 90], "Flame Charge": [50, 100]}}
    pokemon_stats["Carapuce"] = {"HP": 320, "Type": "water", "Attack List": {"Water Gun": [20, 100], "Hydro Pump": [70, 85]}}
    pokemon_stats["Tortank"] = {"HP": 530, "Type": "water", "Attack List": {"Aqua Tail": [30, 90], "Hydro Pump": [80, 85]}}
    pokemon_stats["Psykokwak"] = {"HP": 350, "Type": "water", "Attack List": {"Water Pulse": [27, 100], "Hydro Pump": [70, 85]}}
    pokemon_stats["Bulbizarre"] = {"HP": 328, "Type": "grass", "Attack List": {"Vine Whip": [25, 100], "Solar Beam": [30, 85]}}
    pokemon_stats["Florizarre"] = {"HP": 490, "Type": "grass", "Attack List": {"Razor Leaf": [35, 95], "Frenzy Plant": [40, 85]}}
    pokemon_stats["Paras"] = {"HP": 300, "Type": "grass", "Attack List": {"Seed Bomb": [30, 85], "X-Scissor": [35, 100]}}
    logging.info("Pokemon stats created")
    return pokemon_stats

def create_pokemon(pokemon_name: str, pokemon_stats) -> Character:
    match pokemon_name:
        case "Salameche":
            logging.info("Salameche created")
            return Salameche(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Arcanin":
            logging.info("Arcanin created")
            return Arcanin(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Ponyta":
            logging.info("Ponyta created")
            return Ponyta(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Carapuce":
            logging.info("Carapuce created")
            return Carapuce(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Tortank":
            logging.info("Tortank created")
            return Tortank(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Psykokwak":
            logging.info("Psykokwak created")
            return Psykokwak(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Bulbizarre":
            logging.info("Bulbizarre created")
            return Bulbizarre(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Florizarre":
            logging.info("Florizarre created")
            return Florizarre(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case "Paras":
            logging.info("Paras created")
            return Paras(pokemon_name, pokemon_stats["HP"], pokemon_stats["Type"], pokemon_stats["Attack List"])
        case _:
            print(f"[red]Error : [/red][white]Choose a valid pokemon[/white]")
            logging.error(f"Error : Choose a valid pokemon")
            exit(1)

def choose_pokemon(pokemon_list: list) -> list:
    chosen_pokemon = []
    pokemon_stats=create_all_pokemon_stats()
    affichage = Affichage()
    for i in range(2):
        affichage.display_character_list(pokemon_list,pokemon_stats)
        if i>0:
            choice=input("Choose your second pokemon: ")
            if choice =='':
                affichage.clear()
                logging.error(f"Error : Choose a valid pokemon")
                print(f"[red]Error : [/red][white]Choose a valid pokemon[/white]")
                exit(1)
            choice=int(choice)
            if choice == 0 or choice > len(pokemon_list):
                affichage.clear()
                logging.error(f"Error : Choose a valid pokemon")
                print(f"[red]Error : [/red][white]Choose a valid pokemon[/white]")
                exit(1)
            chosen_pokemon.append(create_pokemon(pokemon_list[choice-1],pokemon_stats[pokemon_list[choice-1]]))
        else:
            choice=input("Choose your pokemon: ")
            if choice =='':
                affichage.clear()
                logging.error(f"Error : Choose a valid pokemon")
                print(f"[red]Error : [/red][white]Choose a valid pokemon[/white]")
                exit(1)
            choice=int(choice)
            if choice == 0 or choice > len(pokemon_list):
                affichage.clear()
                logging.error(f"Error : Choose a valid pokemon")
                print(f"[red]Error : [/red][white]Choose a valid pokemon[/white]")
                exit(1)
            chosen_pokemon.append(create_pokemon(pokemon_list[choice-1],pokemon_stats[pokemon_list[choice-1]]))
        affichage.clear()
        logging.info(f"Pokemon {chosen_pokemon[i].get_name()} added to inventory")
    return chosen_pokemon

def choose_attack(character: Character,bot_pokemon: Character, round,error="") -> str:
    affichage=Affichage()
    if error != "":
        print(error)
    affichage.display_combat_hud(character, bot_pokemon, round)
    affichage.display_attack_list(character.get_attack_list())
    attack = input("Your choice: ")
    if attack in character.get_attack_list():
        logging.info(f"Attack {attack} chosen")
        return attack
    else:
        error = f"[red]Error : [/red][white]Choose a valid attack[/white]"
        logging.error(f"Error : Choose a valid attack")
        affichage.clear()
        return choose_attack(character,bot_pokemon,round,error)
    
def choose_attack_bot(character: Character) -> str:
    a_list = []
    for key in character.get_attack_list():
         a_list.append(key)
    randnb = random.randint(0, len(a_list)-1)
    logging.info(f"Attack {a_list[randnb]} chosen")
    return a_list[randnb]
    
    
def choose_pokemon_bot(pokemon_list: list) -> list:
    pokemon_stats= create_all_pokemon_stats()
    chosen_pokemon = []
    randnb = random.randint(0, len(pokemon_list)-1)
    chosen_pokemon.append(create_pokemon(pokemon_list[randnb],pokemon_stats[pokemon_list[randnb]]))
    randnb2 = random.randint(0, len(pokemon_list)-1)
    while randnb2 == randnb:
        randnb2 = random.randint(0, len(pokemon_list)-1)
        logging.info(f"Pokemon {pokemon_list[randnb2]} added to inventory")
    chosen_pokemon.append(create_pokemon(pokemon_list[randnb2],pokemon_stats[pokemon_list[randnb2]]))
    return chosen_pokemon

def choose_pokemon_to_fight(player_inventory: list, error="") -> Character:
    affichage=Affichage()
    create_all_pokemon_stats()
    affichage.display_characters_choose(player_inventory,error)
    pokemon =input("Choose your pokemon for the fight: ")
    match(pokemon):
        case "1":
            logging.info(f"Pokemon {player_inventory[0].get_name()} chosen for the fight")
            return player_inventory[0]
        case "2":
            logging.info(f"Pokemon {player_inventory[1].get_name()} chosen for the fight")
            return player_inventory[1]
        case _:
            affichage.clear()
            logging.error(f"Error : Choose a valid pokemon")
            error = f"[red]Error : [/red][white]Choose a valid pokemon[/white]"
            return choose_pokemon_to_fight(player_inventory,error)
        
def choose_pokemon_to_fight_bot(bot_inventory: list) -> Character:
    randnb = random.randint(0, len(bot_inventory)-1)
    logging.info(f"Pokemon {bot_inventory[randnb].get_name()} chosen for the fight")
    return bot_inventory[randnb]

def combat(player_pokemon: Character, bot_pokemon: Character)-> bool:
    affichage = Affichage()
    round = 1
    while player_pokemon.is_alive() and bot_pokemon.is_alive():
        affichage.clear()
        attack = choose_attack(player_pokemon,bot_pokemon,round)
        bot_attack = choose_attack_bot(bot_pokemon)
        player_pokemon.attack(bot_pokemon, attack)
        bot_pokemon.attack(player_pokemon, bot_attack)
        affichage.display_combat_hud(player_pokemon, bot_pokemon, round)
        round += 1
    if player_pokemon.is_alive():
        affichage.display_player_winner(player_pokemon)
        input("Press Enter to continue...")
        return True
    else:
        affichage.display_bot_winner(bot_pokemon)
        input("Press Enter to continue...")
        return False
    
def check_attack(attack: str, attack_list: list) -> bool:
    for a in attack_list:
        if a == attack:
            return True
    return False

def main_menu_choice():
    affichage=Affichage()
    affichage.main_menu()
    choice=int(input("Your choice: "))
    if choice != 1 and choice != 2 and 3:
        affichage.clear()
        print(f"[red]Error : [/red][white]Choose a valid option[/white]")
        exit(1)
    if choice == 1:
        affichage.clear()
        return
    if choice == 2:
        affichage.clear()
        affichage.display_info()
        input(f">>>")
        main_menu_choice()
        return
    if choice == 3:
        affichage.clear()
        exit(0)

def init_game():
    pokemon_list = create_pokemon_list()
    player_inventory = choose_pokemon(pokemon_list)
    bot_inventory = choose_pokemon_bot(pokemon_list)
    return player_inventory, bot_inventory

def init_pokemon(player_inventory: list, bot_inventory: list):
    player_pokemon = choose_pokemon_to_fight(player_inventory)
    bot_pokemon = choose_pokemon_to_fight_bot(bot_inventory)
    return player_pokemon, bot_pokemon

def init_combat(player_inventory: list, bot_inventory: list):
    while len(player_inventory) > 0 and len(bot_inventory) > 0:
        player_pokemon, bot_pokemon = init_pokemon(player_inventory, bot_inventory)
        if combat(player_pokemon, bot_pokemon):
            bot_inventory.remove(bot_pokemon)
            logging.info(f"Pokemon {bot_pokemon.get_name()} removed from bot inventory")
        else:
            player_inventory.remove(player_pokemon)
            logging.info(f"Pokemon {player_pokemon.get_name()} removed from player inventory")

def check_winner(player_inventory: list) -> bool:
    if len(player_inventory) > 0:
        return True
    else:
        return False


def main():
    affichage=Affichage()
    main_menu_choice()
    player_inventory, bot_inventory = init_game()
    init_combat(player_inventory, bot_inventory)
    affichage.display_game_winner(check_winner(player_inventory))


if __name__ == "__main__":
    if not os.path.exists('./log/pokemon_battle/'):
        os.makedirs('./log/pokemon_battle/')

    logging.basicConfig(filename='./log/pokemon_battle/battle.log', level=logging.DEBUG)
    main()