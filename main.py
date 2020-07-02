from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 30},
         {"name": "Thunder", "cost": 10, "damage": 25},
         {"name": "Blizzard", "cost": 10, "damage": 20}]

player = Person(100, 50, 30, 25, magic)
enemy = Person(150, 60, 40, 35, magic)

running = True
iterator = 1

print(bcolors.FAIL + bcolors.BOLD + "UN ENEMIGO ESTÁ ATACANDO" + bcolors.ENDC)

while running:
    print("==================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print("El enemigo recibio", damage, "Y su vida es:", enemy.get_hp())

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("El enemigo infringió daño", enemy_damage, "Tu vida restante es:", player.get_hp())

