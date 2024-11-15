# 5. Реактивный агент, который играет ход, побеждающий предыдущий ход противника

import random

def reactionary_agent(observation, configuration):
    # Если это не первый ход, играем ход, побеждающий предыдущий ход противника
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % 3
    else:
        # Иначе выбираем случайный ход
        return random.randrange(0, configuration.signs)
