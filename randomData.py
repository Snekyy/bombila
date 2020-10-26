import random
import string
import json

def shuffleServices(services):
    random.shuffle(services)

def random_name():
    with open("./random_data.json", "r") as file:
        names = json.load(file)["names"]
    return random.choice(names)

def random_email():
    with open("./random_data.json", "r") as file:
        emails = json.load(file)["emails"]
    return random_name() + random_nums() + random.choice(emails)

def random_pass():
    return random_name() + random_nums()

def random_nums():
    ls = [str(random.randint(10, 99)) for i in range(2)]
    return "".join(ls)

def random_token():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(random.randint(20, 50)))
