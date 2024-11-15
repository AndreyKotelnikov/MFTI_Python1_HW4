# 14. Агент "Meta", который пытается предсказать следующий ход противника 
# на основе их предыдущего поведения и играет ход, побеждающий этот прогноз

def meta_agent(observation, configuration):
    import random

    if observation.step == 0:
        meta_agent.opponent_history = []
    else:
        meta_agent.opponent_history.append(observation.lastOpponentAction)

    if observation.step > 1:
        # Предполагаем, что противник будет реагировать на наш предыдущий ход
        predicted_opponent_move = (meta_agent.opponent_history[-1] + 1) % 3
        # Играем ход, побеждающий предположенный ход противника
        return (predicted_opponent_move + 1) % 3
    else:
        # Если недостаточно данных, выбираем случайный ход
        return random.randrange(0, configuration.signs)
