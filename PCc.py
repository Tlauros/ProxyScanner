
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

import os
import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style

# Define the config file path and global config variable
FILE_PATH = "config.json"
CONFIG = None

class ProxyChecker:
    def __init__(self):
        """Initialize the ProxyChecker and load the config."""
        self.check_file_config()
        self.load_config()

    def check_file_config(self):
        """Check if the config file exists, create it if it doesn't."""
        if not os.path.exists(FILE_PATH):
            default_config = {
                "timeout": 10,
                "threads": 10,
                "max_ms": 4000,
                "import": ["proxies.txt"],
                "export": "working.txt",
                "url_check": "https://ipwho.is/",
                "host": "https://httpbin.org/get"
            }
            with open(FILE_PATH, 'w') as f:
                json.dump(default_config, f, indent=4)
            print(Fore.GREEN + f'File ({FILE_PATH}) created.' + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f'File ({FILE_PATH}) already exists.' + Style.RESET_ALL)

    def load_config(self):
        """Read the config file and set the global config variable."""
        global CONFIG
        with open(FILE_PATH) as f:
            CONFIG = json.load(f)
        print(Fore.CYAN + "Configuration loaded successfully." + Style.RESET_ALL)
        return CONFIG

    def open_config(self):
        """Return the global config or reload it if not available."""
        global CONFIG
        if CONFIG is None:
            self.load_config()
        return CONFIG

    def check_proxy_http(self, proxy):
        """Check a single HTTP proxy and return its status."""
        global CONFIG
        try:
            proxy_dict = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            response = requests.get(CONFIG['url_check'], proxies=proxy_dict, timeout=CONFIG['timeout'])

            if response.status_code == 200 and response.json().get('success', False):
                proxy_ip = proxy.split(':')[0]
                json_data = response.json()
                returned_ip = json_data['ip']
                if returned_ip == proxy_ip:
                    start_time = time.perf_counter()
                    response = requests.get(CONFIG['host'], proxies=proxy_dict, timeout=CONFIG['timeout'])
                    end_time = time.perf_counter()
                    elapsed_time_ms = round((end_time - start_time) * 1000)

                    if response.status_code == 200:
                        if elapsed_time_ms < CONFIG['max_ms']:
                            return (proxy, elapsed_time_ms, json_data['ip'], json_data['country'])
                        return (proxy, None, None, None)  # Too slow
                    return (proxy, None, None, None)  # Failed host check
                return (proxy, None, None, None)  # Invalid IP
            return (proxy, None, None, None)  # Bad response

        except requests.exceptions.RequestException:
            return (proxy, None, None, None)  # Proxy failed

    def check_proxy_https(self, proxy):
        """Check a single HTTPS proxy and return its status."""
        global CONFIG
        try:
            proxy_dict = {'https': f'https://{proxy}'}
            response = requests.get(CONFIG['url_check'], proxies=proxy_dict, timeout=CONFIG['timeout'])

            if response.status_code == 200 and response.json().get('success', False):
                proxy_ip = proxy.split(':')[0]
                json_data = response.json()
                returned_ip = json_data['ip']
                if returned_ip == proxy_ip:
                    start_time = time.perf_counter()
                    response = requests.get(CONFIG['host'], proxies=proxy_dict, timeout=CONFIG['timeout'])
                    end_time = time.perf_counter()
                    elapsed_time_ms = round((end_time - start_time) * 1000)

                    if response.status_code == 200:
                        if elapsed_time_ms < CONFIG['max_ms']:
                            return (proxy, elapsed_time_ms, json_data['ip'], json_data['country'])
                        return (proxy, None, None, None)  # Too slow
                    return (proxy, None, None, None)  # Failed host check
                return (proxy, None, None, None)  # Invalid IP
            return (proxy, None, None, None)  # Bad response

        except requests.exceptions.RequestException:
            return (proxy, None, None, None)  # Proxy failed

    def scan_http(self, proxy_list):
        """Scan a list of HTTP proxies and return working ones."""
        global CONFIG

        if not proxy_list:
            os.system('cls' if os.name == 'nt' else 'clear')
            return Fore.RED + 'Error: No proxies found.' + Style.RESET_ALL

        results = []
        export_file = CONFIG['export']
        print(Fore.CYAN + f'Checking {len(proxy_list)} HTTP proxies with {CONFIG["threads"]} threads...' + Style.RESET_ALL)

        with ThreadPoolExecutor(max_workers=CONFIG['threads']) as executor:
            future_to_proxy = {executor.submit(self.check_proxy_http, proxy): proxy for proxy in proxy_list}
            for future in as_completed(future_to_proxy):
                proxy, elapsed_time_ms, ip, country = future.result()
                if elapsed_time_ms is not None:
                    results.append((proxy, elapsed_time_ms))
                    print(Fore.GREEN + f'Proxy {proxy} (HTTP) is working. Ping: {elapsed_time_ms} ms' + Style.RESET_ALL)
                    with open(export_file, 'a') as f:
                        f.write(f"{proxy} | IP: {ip} | Country: {country} | Ping: {elapsed_time_ms} ms\n")
                elif ip is not None:
                    print(Fore.YELLOW + f'{proxy} | Too slow or failed host check' + Style.RESET_ALL)
                else:
                    print(Fore.RED + f'Proxy {proxy} failed' + Style.RESET_ALL)

        return results

    def scan_https(self, proxy_list):
        """Scan a list of HTTPS proxies and return working ones."""
        global CONFIG

        if not proxy_list:
            os.system('cls' if os.name == 'nt' else 'clear')
            return Fore.RED + 'Error: No proxies found.' + Style.RESET_ALL

        results = []
        export_file = CONFIG['export']
        print(Fore.CYAN + f'Checking {len(proxy_list)} HTTPS proxies with {CONFIG["threads"]} threads...' + Style.RESET_ALL)

        with ThreadPoolExecutor(max_workers=CONFIG['threads']) as executor:
            future_to_proxy = {executor.submit(self.check_proxy_https, proxy): proxy for proxy in proxy_list}
            for future in as_completed(future_to_proxy):
                proxy, elapsed_time_ms, ip, country = future.result()
                if elapsed_time_ms is not None:
                    results.append((proxy, elapsed_time_ms))
                    print(Fore.GREEN + f'Proxy {proxy} (HTTPS) is working. Ping: {elapsed_time_ms} ms' + Style.RESET_ALL)
                    with open(export_file, 'a') as f:
                        f.write(f"{proxy} | IP: {ip} | Country: {country} | Ping: {elapsed_time_ms} ms\n")
                elif ip is not None:
                    print(Fore.YELLOW + f'{proxy} | Too slow or failed host check' + Style.RESET_ALL)
                else:
                    print(Fore.RED + f'Proxy {proxy} failed' + Style.RESET_ALL)

        return results
