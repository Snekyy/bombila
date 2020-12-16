# Bombila - sms bomber for russian phones

## Installation:
```bash
git clone https://github.com/Snekyy/bombila.git
cd ./bombila
pip3 install -r requirements.txt
python3 bombila.py --help
```
## Usage:

bombila.py [-h] [-p <phone-number>] [-t <seconds>] [--threads <num>] [-T <seconds>] [--proxy] [--version]</br>

optional arguments:</br>
  -h, --help            show this help message and exit</br>
  -p <phone-number>, --phone <phone-number>			target's phone number, format no matters</br>
  -t <seconds>, --time <seconds>		bombing time in seconds</br>
  --threads <num>       bomber's threads count (default: 50)</br>
  -T <seconds>, --timeout <seconds>      request's timeout, (default: 3)</br>
  --proxy               use proxy from config.py file</br>
  --version             show program's version number and exit

### Usage examples ###

* Running without args:
```bash
python3 bombila.py
```
* Running with minimal amount of args to run without questions:
```bash
python3 bombila.py -p 79877771122 -t 20
```
* Use proxy while bombing:
```bash
python3 bombila.py -p 79877771122 -t 20 --proxy
```
* Use all possible arguments:
```bash
python3 bombila.py -p 79877771122 -t 228 --threads 1337 -T 2 --proxy
```

### Change log

#### 0.0.4.1
	1. Fix shuffle of services(when they shuffle ones they changed for all threads)
	2. Control+C kills script faster now

#### 0.0.4
	1. PEP8 code style
	2. Proxy argument(--proxy). All requests will be send with proxy
	3. ASCII art)
	4. Project rename. "sms-bomber" --> "Bombila"

#### 0.0.3
	1. Multithreading. New script parametr - --threads(set bomber's threads count)
	2. Services list update
	3. Services shuffling for every thread of bomber

#### 0.0.2
	1. New arguments:
		* timeout for request (-T/--timeout)
		* time of bombing (-t/--stop-time
		* interval between requests (-i/--interval)
	
#### 0.0.1
	1. First commit
