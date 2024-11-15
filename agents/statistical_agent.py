# 7. Статистический агент, который анализирует частоту ходов противника

def statistical_agent(observation, configuration):
    import random
    from collections import Counter

    if observation.step == 0:
        statistical_agent.opponent_history = []
    else:
        statistical_agent.opponent_history.append(observation.lastOpponentAction)

    if observation.step > 0:
        # Находим наиболее часто встречающийся ход противника
        count = Counter(statistical_agent.opponent_history)
        most_common = count.most_common(1)[0][0]
        # Играем ход, побеждающий наиболее частый ход противника
        return (most_common + 1) % 3
    else:
        return random.randrange(0, configuration.signs)
