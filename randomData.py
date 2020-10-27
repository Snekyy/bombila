import random
import string
import conf.config as cfg

def shuffleServices(services):
    random.shuffle(services)

def randomName():
    names = cfg.names
    return random.choice(names)

def randomEmail():
    emails = cfg.emails
    return randomName() + randomNums() + random.choice(emails)

def randomPass():
    return randomName() + randomNums()

def randomNums():
    ls = [str(random.randint(10, 99)) for i in range(2)]
    return "".join(ls)

def randomToken():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(30))
