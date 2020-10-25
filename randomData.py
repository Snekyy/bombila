import random
import json

def random_name():
    with open("random_data.json", "r") as file:
        names = json.load(file)["names"]
    return random.choice(names)

def random_email():
    with open("random_data.json", "r") as file:
        emails = json.load(file)["emails"]
    return random_name() + random_nums() + random.choice(emails)

def random_pass():
    return random_name() + random_nums()

def random_nums():
    ls = [str(random.randint(0, 10)) for i in range(5)]
    return "".join(ls)
