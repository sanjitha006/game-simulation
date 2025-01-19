import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles =[1,1]  
        self.results = [1,0]           
        self.opp_play_styles = [1,1]  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 0:
            return 1
        elif self.results[-1] == 0.5:
            return 0
        else:
            if(((len(self.results)-self.points)/len(self.results))>(6/11)):
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
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
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

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    alice = Alice()
    bob = Bob()
    payoff_matrix = [[[1/2, 0, 1/2],[7/10, 0, 3/10],[5/11, 0, 6/11]], 
                                    [[3/10, 0, 7/10],[1/3, 1/3, 1/3],[3/10, 1/2, 1/5]], 
                                    [[6/11, 0, 5/11],[1/5, 1/2, 3/10],[1/10, 4/5, 1/10]]]
    
    
    total_sum_of_number_of_rounds_to_win=0
    for i in range(10000):
        total_alice_wins=1
        while(total_alice_wins!=T):
            simulate_round(alice,bob,payoff_matrix)
            if(alice.results[-1]==1):
                total_alice_wins+=1
        total_sum_of_number_of_rounds_to_win+=len(alice.results)
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
    return(total_sum_of_number_of_rounds_to_win/10000)
#print(estimate_tau(34))
#around 69 to 70
    
        
        
    
