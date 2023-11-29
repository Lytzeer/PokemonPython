from character import Character, Salameche, Arcanin, Carapuce, Tortank, Bulbizarre, Florizarre, Ponyta, Psykokwak, Paras
from affichage import Affichage
import random
import time

def create_pokemon() -> list:
    pokemon_list = []
    pokemon_list.append(Salameche("Salameche", 100, 5, "fire", {"Flamethrower": 10, "Fire Blast": 20}))
    pokemon_list.append(Arcanin("Arcanin", 100, 5, "fire", {"Flamethrower": 10, "Fire Blast": 20}))
    pokemon_list.append(Ponyta("Ponyta", 100, 5, "fire", {"Flamethrower": 10, "Fire Blast": 20}))
    pokemon_list.append(Carapuce("Carapuce", 100, 5, "water", {"Water Gun": 10, "Hydro Pump": 20}))
    pokemon_list.append(Tortank("Tortank", 100, 5, "water", {"Water Gun": 10, "Hydro Pump": 20}))
    pokemon_list.append(Psykokwak("Psykokwak", 100, 5, "water", {"Water Gun": 10, "Hydro Pump": 20}))
    pokemon_list.append(Bulbizarre("Bulbizarre", 100, 5, "grass", {"Vine Whip": 10, "Razor Leaf": 20}))
    pokemon_list.append(Florizarre("Florizarre", 100, 5, "grass", {"Vine Whip": 10, "Razor Leaf": 20}))
    pokemon_list.append(Paras("Paras", 100, 5, "grass", {"Vine Whip": 10, "Razor Leaf": 20}))
    return pokemon_list

def choose_pokemon(pokemon_list: list) -> list:
    chosen_pokemon = []
    affichage = Affichage()
    for i in range(2):
        affichage.display_character_list(pokemon_list)
        if i>0:
            chosen_pokemon.append(pokemon_list[int(input("Choose your second pokemon: "))-1])
        else:
            chosen_pokemon.append(pokemon_list[int(input("Choose your pokemon: "))-1])
        affichage.clear()
    return chosen_pokemon

def choose_attack(character: Character) -> str:
    affichage=Affichage()
    affichage.display_attack_list(character.get_attack_list())
    attack = input("Your choice: ")
    if attack in character.get_attack_list():
        return attack
    else:
        return choose_attack(character)
    
def choose_attack_bot(character: Character) -> str:
    randnb = random.randint(0, len(character.get_attack_list())-1)
    return character.get_attack_list()[randnb]
    
def choose_pokemon_bot(pokemon_list: list) -> list:
    chosen_pokemon = []
    randnb = random.randint(0, len(pokemon_list)-1)
    chosen_pokemon.append(pokemon_list[randnb])
    randnb2 = random.randint(0, len(pokemon_list)-1)
    while randnb2 == randnb:
        randnb2 = random.randint(0, len(pokemon_list)-1)
    chosen_pokemon.append(pokemon_list[randnb2])
    return chosen_pokemon

def choose_pokemon_to_fight(player_inventory: list) -> Character:
    affichage=Affichage()
    affichage.display_character_list(player_inventory)
    pokemon = int(input("Choose your pokemon for the fight: "))
    match(pokemon):
        case 1:
            return player_inventory[0]
        case 2:
            return player_inventory[1]
        case _:
            print("[red]Error : [/red][white]Choose a valid pokemon[/white]")
            return choose_pokemon_to_fight(player_inventory)
        
def choose_pokemon_to_fight_bot(bot_inventory: list) -> Character:
    randnb = random.randint(0, len(bot_inventory)-1)
    return bot_inventory[randnb]

def combat(player_pokemon: Character, bot_pokemon: Character)-> bool:
    affichage = Affichage()
    round = 1
    while player_pokemon.is_alive() and bot_pokemon.is_alive():
        affichage.clear()
        affichage.display_combat_hud(player_pokemon, bot_pokemon, round)
        attack = choose_attack(player_pokemon)
        bot_attack = choose_attack_bot(bot_pokemon)
        player_pokemon.attack(bot_pokemon, attack)
        bot_pokemon.attack(player_pokemon, bot_attack)
        affichage.display_combat_hud(player_pokemon, bot_pokemon, round)
        round += 1
    if player_pokemon.is_alive():
        affichage.display_player_winner(player_pokemon)
        input("Press Enter to continue...")
        time.sleep(3)
        return True
    else:
        affichage.display_bot_winner(bot_pokemon)
        input("Press Enter to continue...")
        time.sleep(3)
        return False
  
def main():
    affichage=Affichage()
    affichage.clear()
    pokemon_list = create_pokemon()
    player_inventory = choose_pokemon(pokemon_list)
    bot_inventory = choose_pokemon_bot(pokemon_list)
    while len(player_inventory) > 0 and len(bot_inventory) > 0:
        player_pokemon = choose_pokemon_to_fight(player_inventory)
        bot_pokemon = choose_pokemon_to_fight_bot(bot_inventory)
        if combat(player_pokemon, bot_pokemon):
            bot_inventory.remove(bot_pokemon)
        else:
            player_inventory.remove(player_pokemon)
    if len(player_inventory) > 0:
        affichage.display_game_winner(True)
    else:
        affichage.display_game_winner(False)


if __name__ == "__main__":
    main()