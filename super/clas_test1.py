class Creature(object):
    def __init__(self, level=1, weapon=None):
        self.level = level
        self.hp = 0
        self.mp = 0
        self.attack = 0
        self.defence = 0
        self.weapon = weapon
        self.job = 'neet'
        
    def status(self):
        return 'Job:{} | HP:{} | MP:{} | Atk:{} | Def:{} | Weapon:{}'.format \
                    (self.job, self.hp, self.mp, self.attack, self.defence, self.weapon)

    
class Warrior(Creature):
    def __init__(self, level):
        super().__init__(level)
        self.attack += 3 * level
        if self.weapon is None:
            self.weapon = 'sword'
        if self.job == 'neet':
            self.job = 'Warrior'
        else: self.job += 'Warrior'
            
            
class Magician(Creature):
    def __init__(self, level):
        super().__init__(level)
        self.mp += 4 *level
        if self.weapon is None:
            self.weapon = 'rod'
        if self.job == 'neet':
            self.job = 'Magic'
        else: self.job += 'Magic'
            
            
class MagicWarrior(Warrior, Magician):
    def __init__(self, level):
        super().__init__(level)
        
        
class WarriorMagic(Magician, Warrior):
    def __init__(self, level):
        super().__init__(level)