class Character:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.max_health=health
        self.attack_power=attack_power

    def take_damage(self,amount):
        self.health-=amount
        if self.health<0:
            self.health=0
        print(f"{self.name} took {amount} damage ! health is now {self.health}")

    def is_alive(self):
        return self.health>0

    def attack(self,target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.take_damage(self.attack_power)


class Player(Character):
    def __init__(self,name,health,attack_power,potion):
        super().__init__(name,health,attack_power)
        self.potion=potion

    def heal(self):
        if self.potion>0:
            self.health+=20
            if self.health>self.max_health:
                self.health=self.max_health
            self.potion-=1
        else:
            print("Out of potion")

class Enemy(Character):
    def __init__(self,name,health,attack_power,xp_reward):
        super().__init__(name,health,attack_power)
        self.xp_reward=xp_reward


def battle(player,enemy):
    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if not enemy.is_alive():
            print("You Defeated The Enemy")
            break
        enemy.attack(player)
        if not player.is_alive():
            print("You were killed")
            break

hero = Player("Hero", 100, 25, 3)
goblin = Enemy("Goblin", 60, 10, 50)
battle(hero, goblin)