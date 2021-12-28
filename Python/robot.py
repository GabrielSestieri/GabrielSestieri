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
    Tom = Robot()
    John = Robot()
    
    Victoria = Robot()
    Mandy = Robot()
    
    John.inflict_damage(Victoria)
    John.inflict_damage(Mandy)
    Tom.inflict_damage(Victoria)
    Tom.inflict_damage(Mandy)
     
    Mandy.inflict_damage(Tom)
    Mandy.inflict_damage(John)
    Victoria.inflict_damage(Tom)
    Victoria.inflict_damage(Mandy)
    
    TomJohn = CompoundRobot(John, Tom)
    VicMandy = CompoundRobot(Victoria, Mandy)
    
    TomJohn.inflict_damage(VicMandy)
    VicMandy.inflict_damage(TomJohn)

    
    if TomJohn.energy > VicMandy.energy:
        print("TomJohn the compunded robot WON with %s points of energy left\n" % round(TomJohn.energy,2))
        print("VicMandy the compounded robot LOST with %s points of energy left\n" % round(VicMandy.energy,2))
    else:
        print("VicMandy the compounded robot WON with %s points of energy left\n" % round(VicMandy.energy,2))
        print("TomJohn the compounded robot LOST with %s points of energy left\n" % round(TomJohn.energy,2))
    
    
if __name__ == '__main__':
    main()