import numpy as np

payoff_matrix = [
    [[0.5, 0, 0.5], [0.7, 0, 0.3], [5 / 11, 0, 6 / 11]],
    [[0.3, 0, 0.7], [1 / 3, 1 / 3, 1 / 3], [0.3, 0.5, 0.2]],
    [[6 / 11, 0, 5 / 11], [0.2, 0.5, 0.3], [0.1, 0.8, 0.1]]
]

def calc_expected_score(alice_move, alice_score, bob_score, remaining_rounds):
    """
    Calculates the expected score for a given Alice move.
    """
    expected_value = 0
    for bob_move in range(3):
        win_prob, draw_prob, lose_prob = payoff_matrix[alice_move][bob_move]
        
        if win_prob > 0:
            win_value = get_move_scores(alice_score + 1, bob_score, remaining_rounds - 1)
            expected_value += win_prob * (1 + sum(win_value)) / 3

        if draw_prob > 0:
            draw_value = get_move_scores(alice_score + 0.5, bob_score + 0.5, remaining_rounds - 1)
            expected_value += draw_prob * (0.5 + sum(draw_value)) / 3

        if lose_prob > 0:
            lose_value = get_move_scores(alice_score, bob_score + 1, remaining_rounds - 1)
            expected_value += lose_prob * sum(lose_value) / 3
    return expected_value

def get_move_scores(alice_score, bob_score, remaining_rounds):
    """
    Calculates scores for each possible move (attack, balanced, defence).
    """
    if remaining_rounds == 0:
        return [0, 0, 0]
    for i in range(3):
	l.append(calculate_expected_score(i, alice_score, bob_score, remaining_rounds))
    return(l) 
def optimal_strategy(alice_score, bob_score, rounds_left):
    move_scores = get_move_scores(alice_score, bob_score, rounds_left)
    best_move = np.argmax(move_scores) 
    return best_move


optimal_move = optimal_strategy(alice_score, bob_score, rounds_left)
