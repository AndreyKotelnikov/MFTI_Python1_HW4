# 4. Агент, который копирует ход противника

import random

def copy_opponent_agent(observation, configuration):
    # Если это не первый ход, копируем предыдущий ход противника
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        # Иначе выбираем случайный ход
        return random.randrange(0, configuration.signs)
