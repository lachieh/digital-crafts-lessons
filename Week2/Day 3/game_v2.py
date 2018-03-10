# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Hero(object):
    def __init__(self):
        self.health = 10
        self.power = 5

    def attack(self, enemy):
        enemy.health -= self.power
            print "You do %d damage to the goblin." % self.power
            if enemy.health <= 0:
                print "The goblin is dead."

    def alive(self):
        return self.health > 0

    def print_status(self):
        print "You have %d health and %d power." % (
            self.health, self.power)


class Goblin(object):
    def __init__(self):
        self.health = 6
        self.power = 2

    def attack(self, enemy):
        enemy.health -= self.power
        print "The goblin does %d damage to you." % self.power
        if enemy.health <= 0:
            print "You are dead."

    def alive(self):
        return self.health > 0

    def print_status(self):
        print "You have %d health and %d power." % (
            self.health, self.power)


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
