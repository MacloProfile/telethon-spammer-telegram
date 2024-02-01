import random

import emoji


def restore_message(message):
    index = [random.randint(1, int(len(message) / 4)) for _ in range(15)]
    emoji_list = random_emoji()
    j = 0
    result = ""
    for i in message:
        flag = True
        if i in emoji_list:
            result += random.choice(emoji_list)
            flag = False
        elif i in ['у', 'к', 'е', 'х', 'а', 'р', 'с', 'м']:
            j += 1
            if j in index:
                result += {'у': 'y', 'к': 'k', 'е': 'e', 'х': 'x', 'а': 'a', 'р': 'p', 'с': 'c', 'м': 'm'}[i]
                flag = False
        elif i in ['y', 'k', 'e', 'x', 'a', 'p', 'c', 'm']:
            j += 1
            if j in index:
                result += {'y': 'у', 'k': 'к', 'e': 'е', 'x': 'х', 'a': 'а', 'p': 'р', 'c': 'с', 'm': 'м'}[i]
                flag = False
        if flag:
            result += i
    return result


def random_emoji():
    with open("emojy.txt", 'r', encoding='utf-8') as file:
        emoji_list = [char for char in file.read()]
    return emoji_list
