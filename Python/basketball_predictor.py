import random
import sys
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
class Teams:
    """ Predict who would win the basketball game
        Attributes: 
            team1(str): user input game match up
            team2(str): user input game match up
    """
    def __init__(self, team1, team2):
        """Read the nba csv file and access the stats for the specific team 
        attribute 
        Args:
            team1(str): user input game match up
        """   
        with open("nba_teams.csv", "r", encoding = "utf-8") as f:
            for team in f:
                new_team = team.strip("\n").split(",")
                if team1 == new_team[0]:
                    self.record = new_team[1]
                    self.home = new_team[2]
                    self.oe = float(new_team[3])
                    self.de = float(new_team[4])
                    self.turn_over = float(new_team[5])
                    self.points = 0  
                
                if team2 == new_team[0]:
                    self.record2 = new_team[1]
                    self.home2 = new_team[2]
                    self.oe2 = float(new_team[3])
                    self.de2 = float(new_team[4])
                    self.turn_over2 = float(new_team[5])
                    self.points2 = 0   
                
    def find_record(self):
        """ Use splicing to get the wins and losses from each team. 
        Depending on the teams record in comparison to the other team, 
        add a certain amount of points to the teams score 
        """ 
        wins = int(self.record[0:2])
        losses = int(self.record[3:5])
        wins2 = int(self.record2[0:2])
        losses2 = int(self.record2[3:5])
        points = (wins - losses)
        points2 = (wins2 - losses2)
        receive = round((abs(points + points)),2)
    
        if points > points2:
            self.points += receive
        else:
            self.points2 += receive
        return self.points, self.points2
        
    def home_court(self):
        """ Randomly choose a game location. If both teams are 'home' then no 
        one gets points but if one is considered home, then add points to their
        score
        """
        coordinate = ['e','w']
        home1 = True
        home2 = True
        game_location = random.choice(coordinate)
        
        if game_location != self.home.lower():
            home1 = False 
        if game_location != self.home2.lower():
            home2= False
        
        if home1 == False and home2 == False:
            self.points += 0 
            self.points2 += 0
        elif home1 == False and home2== True:
            self.points2 += 20
        elif home2 == False and home1== True:
            self.points += 20
        return self.points, self.points2
                       
    def offensive_efficiency(self):
        """  Subtracts the teams offensive officiency and if the team has a 
        greater offensive efficiency then they get the points added to their 
        score """
        sub = round((self.oe - self.oe2),2)
        sub1 = round((self.oe2 - self.oe),2)
        
        if sub > 0:
            val = round(((self.oe - self.turn_over)*(abs(sub)/10)),2)
            self.points += val
            self.points2 += sub
             
        else:
            val1 = round(((self.oe2 - self.turn_over2)*(abs(sub)/10)),2)
            self.points2 += val1
            self.points += sub1
        return self.points, self.points2
       
    def defense_efficiency(self):
        """ Takes the teams DE and compares it to the average, gives out or
         takes points accordingly."""
        sub = round((self.de - self.de2),2)
        sub1 = round((self.de2 - self.de),2)
        if sub > 0:
            val = round(((self.de - self.turn_over)*(abs(sub)/10)),2)
            self.points += val
            self.points2 += sub
            
        else:
            val1 = round(((self.de2 - self.turn_over2)*(abs(sub)/10)),2)
            self.points2 += val1
            self.points += sub1
        return self.points, self.points2
    
    def turn_overs(self):
        """ if the team has a lot of turn overs then subract from their
        probability of winning"""
        float(round((int(self.points)),2) - self.turn_over)
        float(round((int(self.points2)),2) - self.turn_over2)
        return self.points, self.points2
    
    def print_graphic(self):
        n_groups = 3
        data_team1 = (float(self.oe), float(self.de), float(self.turn_over))
        data_team2 = (float(self.oe2), float(self.de2), float(self.turn_over2))
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8
        bars = ax.bar(index, data_team1, bar_width, alpha=opacity, color='#4682B4', edgecolor='black', label=sys.argv[1].capitalize())
        bars2 = ax.bar(index + bar_width, data_team2, bar_width, alpha=opacity, color='#FFA450', edgecolor='black', label=sys.argv[2].capitalize())
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x(),  (yval+0.5), yval)   
        for bar in bars2:
            yval = bar.get_height()
            plt.text(bar.get_x(), yval+0.5, yval)   
        plt.xlabel('Stats')
        plt.ylabel('Score')
        plt.title('Teams Data Comparison')
        plt.xticks(index + 0.175, ('Offensive Efficiency', 'Defensive Efficiency', 'Turn Overs'))
        plt.legend()
        
        points_labels = [(f"{sys.argv[1].capitalize()}\n{self.points} Total Points"), (f"{sys.argv[2].capitalize()}\n{self.points2} Total Pts")]
        points = [self.points, self.points2]
        
        ax1 = fig.add_axes([.6, .3, .45, .5])
        ax1.pie(points, labels=points_labels, radius= 0.5, autopct="%1.1f%%")
    
        plt.tight_layout()
        plt.show()
        
    def total(self): 
        """ Call each method and return a total of points"""
        self.find_record()
        self.home_court()
        self.offensive_efficiency()
        self.defense_efficiency()
        self.turn_overs()
        self.print_graphic()
        return self.points, self.points2
         
def main():
    """ Take the teams from the command line and change them into first
    letter capitalized. Then extract the tuple and reveal each team's
    score
    """
    t= Teams(sys.argv[1].capitalize(), sys.argv[2].capitalize())
    scores = t.total()
    (team1_score, team2_score) = scores
    print(team1_score)
    print(team2_score)     
main()