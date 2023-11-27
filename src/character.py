from rich import print
from healthbar import Healthbar

class Character:

    def __init__(self, name, maxhp, damage, defense, character_type):
        self._name = name
        self._hp = maxhp
        self._max_hp = maxhp
        self._damage = damage
        self._defense = defense
        self._type = character_type
        self._attack_list = {} # {attack_name: damage, ...}
        # Create healthbar
        self._healthbar = Healthbar(self._name, self._max_hp, self._hp)
        self._healthbar.create_healthbar()

    def get_name(self):
        return self._name
    
    def get_hp(self):
        return self._hp
    
    def get_attack_list(self):
        return self._attack_list
    
    def get_damage(self):
        return self._damage
    
    def get_type(self):
        return self._type
    
    def get_attack(self, attack_name):
        return self._attack_list[attack_name]
    
    def decrease_hp(self, damage):
        self._hp -= damage if damage <= self._hp else self._hp

    def is_alive(self):
        return self._hp > 0
    
    def attack(self, enemy, attack_name):
        enemy.decrease_hp(self._attack_list[attack_name])
    
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