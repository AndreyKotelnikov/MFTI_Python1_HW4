# 10. Агент, который повторяет ход противника двух ходов назад

import random

def mirror_opponent_agent(observation, configuration):
    if observation.step == 0:
        mirror_opponent_agent.opponent_history = []
    else:
        mirror_opponent_agent.opponent_history.append(observation.lastOpponentAction)

    if observation.step >= 2:
        # Повторяем ход противника двух ходов назад
        return mirror_opponent_agent.opponent_history[-2]
    else:
        # Иначе выбираем случайный ход
        return random.randrange(0, configuration.signs)
