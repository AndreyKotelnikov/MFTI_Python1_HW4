# 13. Агент "Beat Frequent", который анализирует последние N ходов противника, 
# определяет наиболее часто встречающийся ход и играет ход, побеждающий его

def beat_frequent_agent(observation, configuration):
    import random
    from collections import Counter

    N = 5  # Количество последних ходов для анализа

    if observation.step == 0:
        beat_frequent_agent.opponent_history = []
    else:
        beat_frequent_agent.opponent_history.append(observation.lastOpponentAction)

    if observation.step >= N:
        # Анализируем последние N ходов противника
        recent_actions = beat_frequent_agent.opponent_history[-N:]
        count = Counter(recent_actions)
        most_common = count.most_common(1)[0][0]
        # Играем ход, побеждающий наиболее частый ход
        return (most_common + 1) % 3
    else:
        # Если недостаточно данных, выбираем случайный ход
        return random.randrange(0, configuration.signs)
