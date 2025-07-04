import random
import matplotlib.pyplot as plt


#First we need to create a player :
class Player:
    def __init__(self,ID,position):#we automatically want the player to be created and have an ID and a postion while their status is alive
        self.ID=ID
        self.position=position
        self.alive=True

#Now we need a play are , the bridge:
class Bridge:
    def __init__(self,length=18):#the length is given by the user
        self.panels=[random.choice( ['L','R'] ) for i in range(length)] #this chooses the panels from left or right in all of the rows
        self.length=length
    
    def is_safe(self,step,choice):
        return self.panels[step]==choice #if the choice for the given step matches the correct sequence the player can hop forward
    
#Now we create the game:
class Game:
    def __init__(self,user_position):
        self.bridge=Bridge() #the game creates a single bridge with only 1 correct sequence
        self.players=[Player(ID=i+1,position=i+1) for i in range(16)]
        self.user_postion=user_position
        self.known_panels=[None]*self.bridge.length#creating an array of 18 elemnts as None, for the first user
    
    def simulate_survival(self):
        for player in self.players: # iterating through all the players
            for step in range(self.bridge.length): #iterating through every 18 steps
                
                if not player.alive: #if player died then it will break out of the loop
                    break
                
                if self.known_panels[step]: #if the player knows the correct panel(from the known panels list) then it will make choice 
                    choice=self.known_panels[step]
                else:
                    choice=random.choice(['L','R'])#player makes a randome choice
                
                if self.bridge.is_safe(step,choice): #lets say the player chooses correctly and the panel is not already known
                    if not self.known_panels[step]:
                        self.known_panels[step] = choice
                else:
                    player.alive=False #player made the wrong choice and died
                    break
            
            if player.position==self.user_postion:#if the players pos matches the users pos returns the status of the user
                return player.alive


#now we need a simulation 
def run_simulations(num_simulations=100):
    positions=list(range(1,17)) #creates a list of all the postions
    survival_counts={pos:0 for pos in positions} #creates a dictionary for the survaival count of each postion

    for pos in positions:#checks for each position
        for i in range(num_simulations):
            game= Game(user_position=pos)
            survived=game.simulate_survival()
            if survived:
                survival_counts[pos]+=1
    
    return survival_counts



#now it is time to plot the data
def plot_survival(survival_counts,num_simulations):
    
    positions=list(survival_counts.keys()) #all the postions is the list of keys 
    rates=[(survival_counts[pos]/num_simulations)*100 for pos in positions]

    plt.figure(figsize=(10,6))
    plt.bar(positions,rates)
    plt.xlabel('Player Postion')
    plt.ylabel('Survival Rate (%)')
    plt.title(f'Survival Rate by Player Position ({num_simulations} simulations)')
    plt.xticks(positions)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    num_simulations=int(input("Enter the number of simulations: "))
    survival_counts=run_simulations(num_simulations)
    plot_survival(survival_counts,num_simulations)








