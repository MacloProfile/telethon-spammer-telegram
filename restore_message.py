import random


def restore_message(message):
    index = [random.randint(1, 100) for _ in range(10)]
    j = 0
    result = ""
    for i in message:
        if i in ['у', 'к', 'е', 'х', 'а', 'р', 'с', 'м']:
            # Replace with corresponding English characters
            result += {'у': 'y', 'к': 'k', 'е': 'e', 'х': 'x', 'а': 'a', 'р': 'p', 'с': 'c', 'м': 'm'}[i]
        elif i in ['y', 'k', 'e', 'x', 'a', 'p', 'c', 'm']:
            # Replace with corresponding Russian characters
            result += {'y': 'у', 'k': 'к', 'e': 'е', 'x': 'х', 'a': 'а', 'p': 'р', 'c': 'с', 'm': 'м'}[i]
        else:
            result += i
    return result