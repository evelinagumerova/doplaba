import re
import random
from collections import UserDict

dict = UserDict()

filename = "D:\synonyms.txt"


def Save(key, value):
    with open(filename, 'a') as file:
        file.write("\n")
        file.write("{} - {}".format(key, value))


with open(filename, 'r') as file:
    lines = file.read().splitlines()
    for item in lines:

        key = item.split(" - ")[0].lower()

        values = item.split(" - ")[1:]

        if (len(values) > 0):
            values = values[0].strip()
            if (values.split(";") is None):
                value = values
            else:
                value = list(values.split(";"))

            value = [x.strip(' ') for x in value]

            if (dict.get(key) is None):
                dict[key] = value
            else:
                dict[key] += value

while True:
    s = input("Введите слово: ")
    if s:
        s = s.strip().lower()

        if (dict.get(s) is None):
            print('Нет синонимов для слова {} '.format(s))
        else:

            synonyms = dict[s]

            print('Синонимов: {}'.format(random.choice(synonyms)))

        res = input('Добавить новый синоним {} [Y] - да ? '.format(s)).strip()
        if res.lower() == 'y':
            newsyn = input('Введите синоним: ').strip().lower()
            if newsyn:
                if (dict.get(s) is None):
                    dict[s] = newsyn
                    Save(s, newsyn)
                else:
                    if (newsyn not in synonyms):
                        synonyms.append(newsyn)
                        dict[s] = list(set(synonyms))
                        Save(s, newsyn)