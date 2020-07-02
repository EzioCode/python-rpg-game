from classes.game import Person

magic = [{"name": "Fire", "cost": 10, "damage": 30},
         {"name": "Thunder", "cost": 10, "damage": 25},
         {"name": "Blizzard", "cost": 10, "damage": 20}]

player = Person(100, 50, 30, 25, magic)

print("El daño del hechizo fue:", player.generate_spell_damage(1))
print("Vida restante:", player.take_damage(10))