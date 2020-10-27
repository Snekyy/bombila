import json
import requests
# My modules
import randomData

class Service:

    def __init__(self, service, timeout, proxy):
        self.service = service
        self.timeout = timeout
        self.proxy = proxy

    def parse_data(self):
        """ Parse data from service, creates datatype domain_name and payload vars """
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
        """ Replace data in payload """
        for old, new in {
            "'": '"',
            "%phone%": phone,
            "%phone9%": phone[1::],
            "%name%": randomData.randomName(),
            "%email%": randomData.randomEmail(),
            "%password%": randomData.randomPass(),
            "%token%": randomData.randomToken()
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
            # Catching errors
            try:
                session.send(request, timeout=self.timeout, proxies=self.proxy)
                print('Success - ' + self.domain_name)
            except requests.exceptions.ReadTimeout:
                print("FAIL - " + self.domain_name + " - ReadTimeout")
            except requests.exceptions.ConnectTimeout:
                print('FAIL - ' + self.domain_name + " - ConnectTimeout")
            except requests.exceptions.ConnectionError:
                print('FAIL - ' + self.domain_name + " - ConnectionError")
            except Exception as err:
                print(err)
