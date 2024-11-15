# 9. Агент, который циклически перебирает ходы "камень", "бумага", "ножницы"

def pattern_agent(observation, configuration):
    if observation.step == 0:
        pattern_agent.next_move = 0
    move = pattern_agent.next_move
    pattern_agent.next_move = (pattern_agent.next_move + 1) % 3
    return move
