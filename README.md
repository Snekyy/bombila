# Bombila - sms bomber for russian phones

## Installation:
```bash
git clone https://github.com/Snekyy/bombila.git
cd ./bombila
pip3 install -r requirements.txt
python3 bombila.py --help
```
## Usage:

usage: bombila [-h] [-p <phone>] [-t <seconds>] [--threads <int>]
               [-i <seconds>] [-T <seconds>] [--proxy] [-v]

optional arguments:</br>
  -h, --help                             show this help message and exit</br>
  -p <phone>, --phone <phone></br>       target's russian phone number, format no matters</br>
  -t <seconds>, --stop_time <seconds>    bombing time in seconds</br>
  --threads <int>                        threads count, more threads = more sms, (default: 50)</br>
  -i <seconds>, --interval <seconds>     intervals between requests in sec, (default: 0)</br>
  -T <seconds>, --timeout <seconds>      timeout for request in sec, (default: 3)</br>
  --proxy                                use proxy while bombing</br>
  -v, --version                          show program's version number and exit</br>


### Usage examples ###

* Running without args:
```bash
python3 bombila.py
```
* Running with a minimal amount of arguments:
```bash
python3 bombila.py -p 79877771122 -t 20
```
* Proxy (this will take proxies from config.py file):
```bash
python3 bombila.py -p 79877771122 -t 20 --proxy
```
* Use all possible arguments:
```bash
python3 bombila.py -p 79877771122 -t 20 --threads 100 -i 0.1 -T 3 --proxy
```
