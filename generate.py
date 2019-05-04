#!/usr/bin/python
# coding: utf-8

import random
'''
Generate randome name and familyName and city
'''


def get_name_female():
    with open("./data/name_f.txt") as f:
        return(random.choice(f.readlines()).strip())


def get_name_male():
    with open("./data/name_m.txt") as f:
        return(random.choice(f.readlines()).strip())


def get_city():
    with open("./data/city.txt") as f:
        return(random.choice(f.readlines()).strip())


def get_surname_male():
    with open("./data/surname.txt") as f:
        return(random.choice(f.readlines()).strip())


def get_surname_female():
    with open("./data/surname.txt") as f:
        return(random.choice(f.readlines()).strip() + 'а')


def get_age():
    return random.randint(18, 70)


def get_user_male(item):
    name = get_name_male()
    surname = get_surname_male()
    age = get_age()
    location = get_city()
    return(item, name, surname, age, 'M', location)


def get_user_female(item):
    name = get_name_female()
    surname = get_surname_female()
    age = get_age()
    location = get_city()
    return(item, name, surname, age, 'F', location)


def get_users(count):
    users = []
    for i in range(count):
        choose = random.randint(0, 1)
        if choose == 0:
            users.append(get_user_female(i))
        else:
            users.append(get_user_male(i))
    return users


print(get_users(2))
