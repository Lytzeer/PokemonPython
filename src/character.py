from rich import print
from healthbar import Healthbar
from affichage import Affichage

class Character:

    def __init__(self, name, maxhp, damage, defense, character_type, attack_list):
        self._name = name
        self._hp = maxhp
        self._max_hp = maxhp
        self._damage = damage
        self._defense = defense
        self._type = character_type
        self._attack_list = attack_list # {attack_name: damage, ...}
        # Create healthbar
        self._healthbar = Healthbar(self._name, self._max_hp, self._hp)
        self._healthbar.create_healthbar()
        # Create affichage
        self._affichage = Affichage()

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
    
    def attack(self, enemy):
        attack_name = self.choose_attack()
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

if __name__ == "__main__":
    affichage = Affichage()
    salameche = Salameche("Salameche", 100, 10, 10, "fire", {"Flamethrower": 20, "Fireball": 10})
    arcanin = Arcanin("Arcanin", 200, 20, 20, "fire", {"Flamethrower": 20, "Fireball": 10})
    character_list = [salameche, arcanin]
    affichage.display_character_list(character_list)
    choose = input("Choose your character: ")
    match(choose):
        case "1":
            affichage.clear()
            index_character = 0
            print("You choose [red]Salameche[/red]!\nChoose an [red]attack[/red]:")
            affichage.display_attack_list(character_list[index_character].get_attack_list())
        case "2":
            affichage.clear()
            print(f"You choose [red]Arcanin[/red]!\nChoose an [red]attack[/red]:")
            index_character = 1
            affichage.display_attack_list(character_list[index_character].get_attack_list())
    
    attack = input("Your choice: ")
    affichage.clear()
    match(attack):
        case "1":
            attack = "Flamethrower"
        case "2":
            attack = "Fireball"
    affichage.display_attack_choose(attack)