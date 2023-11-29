from panel import Panels
from rich import print
from rich.table import Table
from os import system

class Affichage:
    def __init__(self):
        self._panel = Panels("Welcome", "Welcome to Pokemon Battle!",(1,3))
        self._table = Table()

    def convert_is_alive(self, is_alive):
        if is_alive:
            return "✅"
        else:
            return "❌"
        
    def clear(self):
        system("cls")


    def display_character_list(self, character_list):
        self._table.title = f"[blue]Character List[/blue]"
        self._table.add_column(f"[magenta]ID[/magenta]")
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