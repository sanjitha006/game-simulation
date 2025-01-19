import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles =[1,1]  
        self.results = [1,0]           
        self.opp_play_styles = [1,1]  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        
        attack_count = self.opp_play_styles.count(0)
        balanced_count = self.opp_play_styles.count(1)
        defense_count = self.opp_play_styles.count(2)
        
        if(((len(self.results)-self.points)/len(self.results))>(15/44)):
          return 0
        else:
          return 2
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles =[1,1] 
        self.results = [0,1]          
        self.opp_play_styles =[1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move=alice.play_move()
    bob_move=bob.play_move()
    result= np.random.choice([1, 0.5, 0], p=payoff_matrix[alice_move][bob_move])
    alice.observe_result(alice_move, bob_move, result)
    bob.observe_result(bob_move, alice_move, 1-result)
    payoff_matrix[0][0][0]=(bob.points/(alice.points+bob.points))
    payoff_matrix[0][0][2]=(alice.points/(alice.points+bob.points))
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    
    payoff_matrix = [[[1/2, 0, 1/2],[7/10, 0, 3/10],[5/11, 0, 6/11]], 
                                    [[3/10, 0, 7/10],[1/3, 1/3, 1/3],[3/10, 1/2, 1/5]], 
                                    [[6/11, 0, 5/11],[1/5, 1/2, 3/10],[1/10, 4/5, 1/10]]]
    alice.past_play_styles = [1,1]
    alice.results = [1,0]         
    alice.opp_play_styles =[1,1] 
    alice.points = 1
    bob.past_play_styles = [1,1]
    bob.results = [0,1]      
    bob.opp_play_styles = [1,1]  
    bob.points = 1
    for i in range(num_rounds):
        simulate_round(alice, bob, payoff_matrix)
    return(alice.results[-1])
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    #running 10000 iterations of  50 round each and looking at the 50th match's scores
    #observing expected score of Alice in 50th round
    number_of_win=0
    number_of_draw_=0
    number_of_loss=0
    for i in range(10000):
        y=monte_carlo(num_rounds=50)
        if y==1:
            number_of_win+=1
        elif y==0.5:
            number_of_draw_+=1
        else:
            number_of_loss+=1
    expected_score_in_50th_match_for_alice=(number_of_win+0.5*number_of_draw_)/10000
    print(expected_score_in_50th_match_for_alice)
    #the expected score is around 0.53
