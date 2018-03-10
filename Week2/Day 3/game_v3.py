# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Character(object):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.type = 'character'

    def attack(self, enemy):
        enemy.health -= self.power
        print "You do %d damage to the %s." % (self.power, enemy.type)
        if enemy.health <= 0:
            print "The %s has died." % (enemy.type)

    def alive(self):
        return self.health > 0

    def print_status(self):
        print "%s has %d health and %d power." % (
            self.type, self.health, self.power)


class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.type = 'Hero'


class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.type = 'Goblin'


def main():
    mainHero = Hero()
    mainGoblin = Goblin()

    while mainGoblin.alive() and mainHero.alive():
        mainHero.print_status()
        mainGoblin.print_status()

        print """
What do you want to do?"
1. fight goblin"
2. do nothing"
3. flee"
>
        """
        input = raw_input()
        if input == "1":
            # Hero attacks goblin
            mainHero.attack(mainGoblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if mainGoblin.alive():
            # Goblin attacks hero
            mainGoblin.attack(mainHero)


main()
