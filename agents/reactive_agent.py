# 12. Реактивный агент, который играет "ножницы", если противник сыграл "бумагу" на предыдущем ходу

import random

def reactive_agent(observation, configuration):
    # Если противник сыграл "бумагу" на предыдущем ходу, играем "ножницы"
    if observation.step > 0 and observation.lastOpponentAction == 1:
        return 2
    else:
        # Иначе играем "камень"
        return 0
