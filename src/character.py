from __future__ import annotations
from rich import print
from healthbar import Healthbar
from affichage import Affichage
import random

class Character:

    def __init__(self, name, maxhp, character_type, attack_list):
        self._name = name
        self._hp = maxhp
        self._max_hp = maxhp
        self._type = character_type
        self._attack_list = attack_list # {attack_name: [damage, accuracy], ...}
        # Create healthbar
        self._healthbar = Healthbar(self._name, self._max_hp, self._hp)
        self._healthbar.create_healthbar()
        # Create affichage
        self._affichage = Affichage()

    def get_name(self):
        return self._name
    
    def get_hp(self):
        return self._hp
    
    def get_max_hp(self):
        return self._max_hp
    
    def get_attack_list(self):
        return self._attack_list
    
    def get_type(self):
        return self._type
    
    def get_attack(self, attack_name):
        return self._attack_list[attack_name]
    
    def get_damage(self, attack_name):
        return self._attack_list[attack_name][0]
    
    def get_accuracy(self, attack_name):
        return self._attack_list[attack_name][1]
    
    def decrease_hp(self, damage):
        self._hp -= damage if damage <= self._hp else self._hp

    def is_alive(self):
        return self._hp > 0
    
    def attack(self, enemy: Character, attack_name: str):
        random_number = random.randint(0, 100)
        if random_number > self.get_accuracy(attack_name):
            print(f"[red]{self.get_name()} missed his attack![/red]")
            return
        enemy.decrease_hp(self.get_damage(attack_name)*self.check_type(enemy))
    
    def check_type(self, enemy):
        if self._type == "fire":
            if enemy.get_type() == "grass":
                return 2
            elif enemy.get_type() == "water":
                return 0.5
            else:
                return 1
        elif self._type == "water":
            if enemy.get_type() == "fire":
                return 2
            elif enemy.get_type() == "grass":
                return 0.5
            else:
                return 1
        elif self._type == "grass":
            if enemy.get_type() == "water":
                return 2
            elif enemy.get_type() == "fire":
                return 0.5
            else:
                return 1
        else:
            return 1
        
    def choose_attack(self):
        print(f"Choose your attack:")
        self._affichage.display_attack_list(self._attack_list)
        attack = input("Your choice: ")
        if attack in self._attack_list:
            return attack
        else:
            return self.choose_attack()
        
# Pokemon

class Salameche(Character):
    pass

class Arcanin(Character):
    pass

class Ponyta(Character):
    pass

class Carapuce(Character):
    pass

class Tortank(Character):
    pass

class Psykokwak(Character):
    pass

class Bulbizarre(Character):
    pass

class Florizarre(Character):
    pass

class Paras(Character):
    pass