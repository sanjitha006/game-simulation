import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles =[1,1]
        self.results = [1,0]
        self.opp_play_styles = [1,1]
        self.points = 1


    def play_move(self):
        if(self.results[-1]==1):
            return 0
        elif(self.results[-1]==0):
            return 1
        else:
            return 0



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
        self.past_play_styles = [1,1]
        self.results = [0,1]
        self.opp_play_styles = [1,1]
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
    return(alice.points-1)


# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    total_points_in_all_iterations=0
    for i in range(100000):
        y=monte_carlo(num_rounds=3)
        total_points_in_all_iterations+=y

    expected_totalscore_in_3_matches_for_alice=total_points_in_all_iterations/100000
    #print(expected_totalscore_in_3_matches_for_alice)
