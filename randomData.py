import random
import json

def randomName():
    with open("names.json", "r") as file:
        name = random.choice(json.load(file)["names"])
    return name

def randomEmail():
    with open("emails.json", "r") as file:
        email = random.choice(json.load(file)["emails"])
    return randomName() + email

def randomPass():
    password = randomName() + "1337"
    return password
