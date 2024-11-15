# 11. Агент, который выбирает "камень" с вероятностью 40%, а "бумагу" и "ножницы" с вероятностью 30%

import random

def weighted_random_agent(observation, configuration):
    # Используем взвешенный выбор
    return random.choices([0, 1, 2], weights=[0.4, 0.3, 0.3])[0]
