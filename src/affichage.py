from panel import Panels
from rich import print
from rich.table import Table
from os import system
from healthbar import Healthbar

class Affichage:
    def __init__(self):
        self._panel = Panels("Welcome", "Welcome to Pokemon Battle!",(1,3))
        self._table = Table()
        self._healthbar = Healthbar("Test", 100, 100)

    def convert_is_alive(self, is_alive):
        if is_alive:
            return "✅"
        else:
            return "❌"
        
    def clear(self):
        system("cls")


    def display_character_list(self, character_list, pokemon_stats):
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Character Choice[/blue]")
        self._panel.update_panel_text(f"[magenta]Choose your characters for the fight[/magenta]")
        self._panel.update_panel_color("red")
        self._panel.display_panel()
        print("\n")
        self._table.title = f"[blue]Character List[/blue]"
        self._table.add_column(f"[orange3]ID[/orange3]")
        self._table.add_column(f"[magenta]Name[/magenta]")
        self._table.add_column(f"[red]HP[/red]")
        self._table.add_column(f"[green]Type[/green]")
        i=1
        for character in character_list:
            self._table.add_row(str(i),character, str(pokemon_stats[character]["HP"]), pokemon_stats[character]["Type"])
            i+=1
        print(self._table)
        self._table = Table()

    def display_characters_choose(self, character_list,error = ""):
        self.clear()
        if error != "":
            print(error)
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Character Choice[/blue]")
        self._panel.update_panel_text(f"[magenta]Choose your characters for the fight[/magenta]")
        self._panel.update_panel_color("red")
        self._panel.display_panel()
        print("\n")
        self._table.title = f"[blue]Character List[/blue]"
        self._table.add_column(f"[orange3]ID[/orange3]")
        self._table.add_column(f"[magenta]Name[/magenta]")
        self._table.add_column(f"[red]HP[/red]")
        self._table.add_column(f"[green]Type[/green]")
        self._table.add_column(f"[cyan]Is Alive[/cyan]", justify="center")
        i=1
        for character in character_list:
            self._table.add_row(str(i),character.get_name(), str(character.get_hp()), character.get_type(), self.convert_is_alive(character.is_alive()))
            i+=1
        print(self._table)
        self._table = Table()
    
    def display_attack_list(self, attack_list):
        self._table.title = f"[blue]Attack List[/blue]"
        self._table.add_column("[magenta]Name[/magenta]")
        self._table.add_column("[red]Damage[/red]")
        for attack in attack_list:
            self._table.add_row(attack, str(attack_list[attack]))
        print(self._table)
        self._table = Table()

    def display_attack(self, attack_name, damage, enemy_name):
        print(f"{enemy_name} took {damage} damage from {attack_name} attack!")

    def display_character(self, character):
        print(f"{character.get_name()} has {character.get_hp()} HP left!")

    def display_attack_choose(self, attack):
        print(f"You choose [red]{attack}[/red] attack!")

    def display_combat_hud(self, player_pokemon, bot_pokemon, round):
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Pokemon Battle[/blue]")
        self._panel.update_panel_subtitle(f"[cyan]Round {round}[/cyan]")
        self._panel.update_panel_text(f"[green]{player_pokemon.get_name()}[/green] [magenta]VS[/magenta] [red]{bot_pokemon.get_name()}[/red]")
        self._panel.display_panel()
        self._healthbar.create_healthbar()
        self._healthbar.update_health(player_pokemon.get_hp())
        self._healthbar.update_maxHealth(player_pokemon.get_max_hp())
        self._healthbar.update_name(player_pokemon.get_name())
        self._healthbar.create_healthbar()
        self._healthbar.display_healthbar()
        print(f"\n[magenta]VS[/magenta]\n")
        self._healthbar.update_health(bot_pokemon.get_hp())
        self._healthbar.update_maxHealth(bot_pokemon.get_max_hp())
        self._healthbar.update_name(bot_pokemon.get_name())
        self._healthbar.create_healthbar()
        self._healthbar.display_healthbar()

    def display_player_winner(self, player_pokemon):
        self.clear()
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Pokemon Battle[/blue]")
        self._panel.update_panel_subtitle(f"[cyan]Winner[/cyan]")
        self._panel.update_panel_text(f"[green]{player_pokemon.get_name()}[/green] [magenta]WIN![/magenta]")
        self._panel.display_panel()
        self._healthbar.create_healthbar()
        self._healthbar.update_health(player_pokemon.get_hp())
        self._healthbar.update_maxHealth(player_pokemon.get_max_hp())
        self._healthbar.update_name(player_pokemon.get_name())
        self._healthbar.display_healthbar()

    def display_bot_winner(self, bot_pokemon):
        self.clear()
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Pokemon Battle[/blue]")
        self._panel.update_panel_subtitle(f"[cyan]Winner[/cyan]")
        self._panel.update_panel_text(f"[red]{bot_pokemon.get_name()}[/red] [magenta]WIN![/magenta]")
        self._panel.display_panel()
        self._healthbar.create_healthbar()
        self._healthbar.update_health(bot_pokemon.get_hp())
        self._healthbar.update_maxHealth(bot_pokemon.get_max_hp())
        self._healthbar.update_name(bot_pokemon.get_name())
        self._healthbar.display_healthbar()

    def display_game_winner(self, winner: bool):
        self.clear()
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Pokemon Battle[/blue]")
        self._panel.update_panel_subtitle(f"[cyan]Winner[/cyan]")
        if winner:
            self._panel.update_panel_text(f"[green]You[/green] [magenta]WIN![/magenta]")
        else:
            self._panel.update_panel_text(f"[red]Bot[/red] [magenta]WIN![/magenta]")
        self._panel.display_panel()

    def main_menu(self):
        self.clear()
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Pokemon Battle[/blue]")
        self._panel.update_panel_subtitle(f"[cyan]Main Menu[/cyan]")
        self._panel.update_panel_text(f"[green]1.[/green] Play\n[orange3]2.[/orange3] Info\n[magenta]3.[/magenta] Quit")
        self._panel.display_panel()

    def display_info(self):
        self.clear()
        self._panel.create_panel()
        self._panel.update_panel_title(f"[blue]Pokemon Battle[/blue]")
        self._panel.update_panel_subtitle(f"[cyan]Info[/cyan]")
        self._panel.update_panel_text(f"Hello, this is a Pokemon Battle game made by [green]Lytzeer[/green]\n\n[red]Github : [/red][white] https://github.com/Lytzeer[/white]\n[red]Discord : [/red][white] Lytzeer[/white]")
        self._panel.display_panel()
        print(f"Press [green]Enter[/green] to continue...")