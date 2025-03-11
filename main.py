"""
 ___________  ________    _______  ___      ___ 
("     _   ")|"      "\  /"     "||"  \    /"  |
 )__/  \\__/ (.  ___  :)(: ______) \   \  //  / 
    \\_ /    |: \   ) || \/    |    \\  \/. ./  
    |.  |    (| (___\ || // ___)_    \.    //   
    \:  |    |:       :)(:      "|    \\   /    
     \__|    (________/  \_______)     \__/     
                                                
     Github : https://github.com/Tlauros
     Discord : https://discord.gg/NCm8CmPE
     Version : 1.0.0
"""
import time
import os
import json
import random
from PCc import ProxyChecker
from colorama import Fore, Style, init
init()

os.system('cls' if os.name == 'nt' else 'clear')
PC = ProxyChecker()
config = PC.open_config()
checked = 0
proxy_http = []
proxy_https = []
file_path = config['import']

#######################################

print(Fore.GREEN + r"""
  _____                        _____
 |  __ \                      / ____|
 | |__) | __ _____  ___   _  | (___   ___ __ _ _ __  _ __   ___ _ __
 |  ___/ '__/ _ \ \/ / | | |  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |   | | | (_) >  <| |_| |  ____) | (_| (_| | | | | | | |  __/ |
 |_|   |_|  \___/_/\_\\__, | |_____/ \___\__,_|_| |_|_| |_|\___|_|
                       __/ |
                      |___/
    Developer : TDEV
    GITHUB : https://github.com/Tlauros
    DISCORD : https://discord.gg/NCm8CmPE
    Version : 1.0.0

""" + Style.RESET_ALL)

time.sleep(random.randint(1,4))

print(Fore.CYAN + f'''
Make sure you have a config.json file in the same directory as this script.
Check out the README.md for more information.

Using these settings from config.json:
    Threads: {config['threads']}
    Timeout: {config['timeout']}
    Max ms: {config['max_ms']}
    Import: {', '.join(config['import'])}
    Export: {config['export']}
    Url Test : {config['url_check']}
    Host: {config['host']}
''' + Style.RESET_ALL)
while True:
    print(Fore.YELLOW + r'''
    1 - SCAN HTTP PROXY
    2 - SCAN HTTPS PROXY
    0 - Exit
    ''' + Style.RESET_ALL)
    choice = input("\n  Enter your choice: ") 

    if choice == '1':
        for file_proxy_http in config['import']:
            try:
                with open(file_proxy_http) as f:
                    proxy_http.extend(f.readlines())
                    print(PC.scan_http(proxy_http))
            except FileNotFoundError:
                print(Fore.RED + f'Error: file "{file_path}" not found.' + Style.RESET_ALL)
            input("\n🔙 Press Enter to return to menu...")
    elif choice == '2':
        for file_proxy_https in config['import']:
            try:
                with open(file_proxy_https) as f:
                    proxy_https.extend(f.readlines())
                    print(PC.scan_https(proxy_https))
            except FileNotFoundError:
                print(Fore.RED + f'Error : file "{file_path}" not found.' + Style.REST_ALL)
        input("\n Press Enter to return to menu...")
    elif choice == '0':
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("exit...")
        break
