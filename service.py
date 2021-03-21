import json
import random
import string
import requests
import conf.config as cfg


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


class Service:
    def __init__(self, service, phone, timeout):
        self.service = service
        self.phone = phone
        self.timeout = timeout


    def __parse_data(self):
        if "data" in self.service:
            self.datatype = "data"
            self.payload = self.service["data"]
        elif "json" in self.service:
            self.datatype = "json"
            self.payload = self.service["json"]
        else:
            self.datatype = "url"
            self.payload = json.dumps({"url": self.service["url"]})


    def __replace_data(self):
        for old, new in {
            "'": '"',
            "%phone%": self.phone,
            "%name%": randomName(),
            "%email%": randomEmail(),
            "%password%": randomPass(),
            "%token%": randomToken()
        }.items():
            if old in self.payload:
                self.payload = self.payload.replace(old, new)


    def get_domain_name(self):
        """ Returns domain name of service. """
        return self.service["url"].split('/')[2]


    def send_request(self):
        """ Send sms request to the server of service. """
        self.__parse_data()
        self.__replace_data()
        session = requests.Session()
        request = requests.Request("POST", self.service["url"])
        self.payload = json.loads(self.payload)
        if self.datatype == "json":
            request.json = self.payload
        elif self.datatype == "data":
            request.data = self.payload
        else:
            request.url = self.payload["url"]
        request = request.prepare()
        session.send(request, timeout=self.timeout)
