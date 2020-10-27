# Bombila - sms bomber for russian phones

## Installation:


* git clone https://github.com/Snekyy/bombila.git
* cd ./sms_bomber
$ pip3 install -r requirements.txt
* python3 bomber.py --help

## Usage: 

usage: bombila [-h] [-p <phone>] [-t <seconds>] [--threads <int>]
               [-i <seconds>] [-T <seconds>] [--proxy] [-v]

Ultimate sms bomber - bombila. Russian numbers only

optional arguments:
  -h, --help            show this help message and exit
  -p <phone>, --phone <phone>
                        target's russian phone number, format no matters
  -t <seconds>, --stop_time <seconds>
                        bombing time in seconds
  --threads <int>       threads count, more threads = more sms, (default: 50)
  -i <seconds>, --interval <seconds>
                        intervals between requests in sec, (default: 0)
  -T <seconds>, --timeout <seconds>
                        timeout for request in sec, (default: 3)
  --proxy               use proxy while bombing
  -v, --version         show program's version number and exit

Usage example: ./bomber.py -p 79877771122 -t 20


