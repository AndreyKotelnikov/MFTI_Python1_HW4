# 8. Случайный агент, который выбирает ход случайно

import random

def random_agent(observation, configuration):
    # Возвращаем случайный ход
    return random.randrange(0, configuration.signs)
