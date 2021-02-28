# :bomb: Bombila - Ultimate sms bomber  :boom: 
![OS support](https://img.shields.io/static/v1?label=os&message=windows%2Flinux%2Fmac&color=red&style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Snekyy/bombila?color=orange&style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Snekyy/bombila?color=yellow&style=for-the-badge)
![GitHub](https://img.shields.io/github/license/Snekyy/bombila?color=green&style=for-the-badge)

## :scroll: Installation:

### :penguin: Linux / :apple: Mac:
```bash
git clone https://github.com/Snekyy/bombila.git
cd ./bombila
pip3 install -r requirements.txt
```

### :shit: Windows:
1. Download zip archive of repository - https://github.com/Snekyy/bombila/archive/master.zip
2. Unzip this archive
3. Open cmd and go to the directory of unziped archive
4. ```pip install -r requirements.txt```

## :crossed_swords: Usage:
bombila.py [-h/--help] [-c/--country <country-code>] [-p/--phone <phone-number>] [-t/--time <sec>] [--threads <num>] [-T/--timeout <sec>]

optional arguments:</br>
  -h, --help            show this help message and exit</br>
  -c, --country         country code without (+) sign</br>
  -p, --phone           target's phone number without country code</br>
  -t, --time            bombing time in seconds</br>
  --threads             bomber's threads count, (default: 50)</br>
  -T, --timeout         request's timeout, (default: 3)</br>

To skip -c, --country argv you can set default country code in config file - [./conf/config.py](./conf/config.py)</br>
Change value of "default_country_code" to your country code like that:
```python3
default_country_code = 7
```

### :fire: Usage Examples ###
* Running without args(you will get some questions later):
```bash
python3 bombila.py
```
* Running with minimal amount of args to run without questions:
```bash
python3 bombila.py -c 7 -p 9877771122 -t 20
```
* :drop_of_blood: Use all possible arguments:
```bash
python3 bombila.py -c 322 -p 9877771122 -t 228 --threads 1337 -T 2 
```
