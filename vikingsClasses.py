import random
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            return str(self.name) + ' has died in act of combat'
        else:
            return str(self.name) + ' has received ' + str(damage) + ' points of damage'

    def battleCry(self):
            return 'Odin Owns You All!'

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            return 'A Saxon has died in combat'
        else:
            return 'A Saxon has received ' + str(damage) + ' points of damage'

# War


class War:
        
        def __init__(self):
            self.vikingArmy = []
            self.saxonArmy = []
        
        def addViking(self, Viking):
            self.vikingArmy.append(Viking)
        
        def addSaxon(self, Saxon):
            self.saxonArmy.append(Saxon)
        
        def vikingAttack(self):
            self.viking = random.choice(self.vikingArmy)
            self.saxon = random.choice(self.saxonArmy)
            resis = self.saxon.receiveDamage(self.viking.strength)
            if self.saxon.health <= 0:
                self.saxonArmy.remove(self.saxon)
            return resis
        
        def saxonAttack(self):
            self.viking = random.choice(self.vikingArmy)
            self.saxon = random.choice(self.saxonArmy)
            resis = self.viking.receiveDamage(self.saxon.strength)
            if self.viking.health <= 0:
                self.vikingArmy.remove(self.viking)
            return resis
        
        def showStatus(self):
            if self.saxonArmy == []:
                return 'Vikings have won the war of the century!'
            elif self.vikingArmy == []:
                return 'Saxons have fought for their lives and survive another day...'
            else:
                return 'Vikings and Saxons are still in the thick of battle.'