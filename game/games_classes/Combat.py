import random

class Combat:
    def __init__(self, attacker, defenser):
        self.pokemon1 = attacker
        self.pokemon2 = defenser

    def first_hit(self):
        if self.pokemon1.speed > self.pokemon2.speed:
            first_hit = self.pokemon1
        elif self.pokemon1.speed < self.pokemon2.speed:
            first_hit = self.pokemon2
        else:
            first_hit = random.choice([self.pokemon1, self.pokemon2])
        return first_hit


    def affinity(self, attacker, defender):
        affinity_values = type_pokemon.matrice()[index1][index2]
        return affinity_values
    
    def attack_chance(self):
        attack_chance = random.randint(0, 100)
        if attack_chance <= 15 :
            # attack missed
            attack_chance_ratio = 0 
        elif 16 <= attack_chance <= 90:
            # attack hit
            attack_chance_ratio = 1
        else:
            # attack critical hit
            attack_chance_ratio = 2
        return attack_chance_ratio
    
    def attack(self, attacker, defender):
        if button_attack.is_pressed:
            print("You choose attack")
            if self.attack_chance() == 0:
                print("Attack missed")
            elif self.attack_chance() == 1:
                print("Attack hit")
                defender.pv = self.pv_remaining(attacker, defender)
                print("Remaining PV : ", defender.pv)
            else:
                print("Critical hit")
                defender.pv = self.pv_remaining(attacker, defender)
                print("Remaining PV : ", defender.pv)

    
    def calculate_damage(self, pokemon1, pokemon2):
        damage = puissance_attack * affinity_values
        return damage
    
    def pv_remaining(self, pokemon1, pokemon2):
        pv_remaining = pokemon2.pv - self.calculate_damage(pokemon1, pokemon2)
        return pv_remaining