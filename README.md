# Bombila - Ultimate sms bomber 


## Installation:

```bash
git clone https://github.com/Snekyy/bombila.git
cd ./bombila
pip3 install -r requirements.txt
python3 bombila.py --help
```
## Usage:

usage: bombila.py [-h/--help] [-c/--country <country-code>] [-p/--phone <phone-number>] [-t/--time <sec>] [--threads <num>] [-T/--timeout <sec>]

optional arguments:
  -h, --help            show this help message and exit</br>
  -c, --country         country code without (+) sign</br>
  -p, --phone           target's phone number without country code</br>
  -t, --time            bombing time in seconds</br>
  --threads             bomber's threads count (default: 50)</br>
  -T, --timeout         request's timeout, (default: 3)</br>

To skip -c, --country argv you can set default country code in config file - ./conf/config.py</br>
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
* Use all possible arguments:
```bash
python3 bombila.py -c 322 -p 9877771122 -t 228 --threads 1337 -T 2 
```
