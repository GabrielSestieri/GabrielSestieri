class Robot:
    def __init__(self):
        self.energy = 20
        self.compound = None
        
    def charge(self, recharge):
        if self.compound == None:
            self.energy += recharge
        else:
            raise RuntimeError
    
    def sustain_damage(self, damage):
        if self.compound is None:
            self.energy -= damage
        else:
          raise RuntimeError
        
    def inflict_damage(self, robot):
        if self.compound is None:
            damage = (self.energy)*0.2
            robot.sustain_damage(damage)
        else:
           raise RuntimeError
    
class CompoundRobot(Robot):
    def __init__(self, Robot1, Robot2):
        super().__init__()
        self.energy = 0
        self.components = []
        self.add_robot(Robot1)
        self.add_robot(Robot2)
        
    def add_robot(self, Robot_obj):
        self.energy += Robot_obj.energy
        self.components.append(Robot_obj)
        Robot_obj.energy = 0
        Robot_obj.compound = self
    
def main():
    sav = Robot()
    gab = Robot()
    
    vicki = Robot()
    fer = Robot()
    
    sav.inflict_damage(vicki)
    sav.inflict_damage(fer)
    gab.inflict_damage(vicki)
    gab.inflict_damage(fer)
    
    
    fer.inflict_damage(gab)
    fer.inflict_damage(sav)
    vicki.inflict_damage(gab)
    vicki.inflict_damage(fer)
    
    savgab = CompoundRobot(sav, gab)
    fervick = CompoundRobot(vicki, fer)
    
    savgab.inflict_damage(fervick)
    fervick.inflict_damage(savgab)

    
    if savgab.energy > fervick.energy:
        print("\Savgab the robot WON with %s points of energy left\n" % (savgab.energy))
        print("Fervick the compounded robot LOST with %s points of energy left\n" % (fervick.energy))
    else:
        print("\Fervick the compounded robot WON with %s points of energy left\n" % (fervick.energy))
        print("Savgab the robot LOST with %s points of energy left\n" % (savgab.energy))
    
    
if __name__ == '__main__':
    main()