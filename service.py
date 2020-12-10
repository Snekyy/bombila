import json
import requests
import data_generator 


class Service:

    def __init__(self, service, timeout, proxy):
        self.service = service
        self.timeout = timeout
        self.proxy = proxy

    def parse_data(self):
        """ Parse data from service. 
            Creates datatype, domain_name and payload vars
        """
        self.domain_name = self.service["url"].split('/')[2]
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
        """ Replace phone number and other random info
            in service template if needed
        """
        for old, new in {
            "'": '"',
            "%phone%": phone,
            "%phone9%": phone[1::],
            "%name%": data_generator.randomName(),
            "%email%": data_generator.randomEmail(),
            "%password%": data_generator.randomPass(),
            "%token%": data_generator.randomToken()
        }.items():
            if old in self.payload:
                self.payload = self.payload.replace(old, new)

    def send_request(self):
        """ Send request for sms to server """
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
        session.send(request, timeout=self.timeout, proxies=self.proxy)



