# Bombila - Ultimate sms bomber 

## Installation:
```bash
git clone https://github.com/Snekyy/bombila.git
cd ./bombila
pip3 install -r requirements.txt
python3 bombila.py --help
```
## Usage:

usage: bombila.py [-h] [-c <country-code>] [-p <phone-number>] [-t <seconds>] [--threads <num>] [-T <seconds>] [--proxy] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -c, --country         country code without (+) sign
  -p, --phone           target's phone number without country code
  -t, --time            bombing time in seconds
  --threads             bomber's threads count (default: 50)
  -T, --timeout         request's timeout, (default: 3)
  --proxy               use proxy from config.py file
  --version             show program's version number and exit

To skip -c, --country argv you can set default country code in config file - ./conf/config.py
Change value of "default_country_code" to your country code like that:
```python3
default_country_code = 7
```
### Usage Examples ###
* Running without args(you will get some questions later):
```bash
python3 bombila.py
```
* Running with minimal amount of args to run without questions:
```bash
python3 bombila.py -c 7 -p 9877771122 -t 20
```
* Use proxy while bombing:
```bash
python3 bombila.py -c 228 -p 9998887766 -t 20 --proxy
```
* Use all possible arguments:
```bash
python3 bombila.py -c 322 -p 9877771122 -t 228 --threads 1337 -T 2 --proxy
```

### Change log

#### 0.0.5
	1. Support of non-russian phone numbers
	2. New argument(-c, --country). Takes country code without "+" sign
	3. "Default country code" option in config file(./conf/config.py). If you will set some value to it you will can skip --country argument
	4. Code structure and documentation update

#### 0.0.4.1
	1. Fix shuffle of services(when they shuffle ones they changed for all threads)
	2. Control+C kills script faster now

#### 0.0.4
	1. PEP8 code style
	2. Proxy argument(--proxy). All requests will be send with proxy
	3. ASCII art)
	4. Project rename. "sms-bomber" --> "Bombila"

#### 0.0.3
	1. Multithreading. New script parameter: --threads(set bomber's threads count)
	2. Services list update
	3. Services shuffling for every thread of bomber

#### 0.0.2
	1. New arguments:
		* timeout for request (-T/--timeout)
		* time of bombing (-t/--stop-time
		* interval between requests (-i/--interval)
	
#### 0.0.1
	1. First commit
