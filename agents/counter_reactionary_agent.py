# 6. Контр-реактивный агент, который играет ход, проигрывающий предыдущему ходу противника

import random

def counter_reactionary_agent(observation, configuration):
    # Если это не первый ход, играем ход, проигрывающий предыдущему ходу противника
    if observation.step > 0:
        return (observation.lastOpponentAction + 2) % 3
    else:
        # Иначе выбираем случайный ход
        return random.randrange(0, configuration.signs)
