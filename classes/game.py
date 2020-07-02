import random


class Person:
    def __init__(self, hp, mp, attack, defense, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defense = defense
        self.magic = magic

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def generate_spell_damage(self, iterator):
        spell_low = self.magic[iterator]["damage"] - 5
        spell_high = self.magic[iterator]["damage"] + 5
        return random.randrange(spell_low, spell_high)

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def reduce_mp(self, cost):
        self.mp = self.mp - cost

    def get_spell_name(self, iterator):
        return self.magic[iterator]["name"]

    def get_spell_cost(self, iterator):
        return self.magic[iterator]["cost"]

    def choose_action(self):
        iterator = 1
        for item in self.actions
            print(str(iterator) + ":", item)
            iterator += 1

    def choose_spell(self):
        iterator = 1
        for spell in self.magic:
            print(str(iterator) + ":", spell["name"], "(cost:", spell["cost"] + ")")
            iterator += 1