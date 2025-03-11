# Proxy Scanner v1.0.0 (Free Edition) 🚀 
### By TDEV
### Discord : https://discord.gg/NCm8CmPE
Welcome to **Proxy Scanner Free** – a lightweight, fast, and easy-to-use tool to test HTTP and HTTPS proxies! Whether you're a developer, a web scraper, or just curious about proxy performance, this tool has got you covered. It checks proxies in parallel with multi-threading for blazing speed! ⚡

## Features 🌟
- HTTP & HTTPS Support: Test both proxy types effortlessly.
- Multi-Threaded Scanning: Checks multiple proxies at once (default: 10 threads).
- Ping Measurement: See how fast each proxy responds.
- Simple Output: Working proxies are saved to `working.txt` with IP, country, and ping.
- Open Source: Free to use, modify, and share under the MIT License!

> Want more? Check out the **[Pro Edition](https://discord.gg/NCm8CmPE)** for SOCKS4/SOCKS5 support, GUI, and advanced features – only $10.99 (one-time payment)!

---

## Installation ⚙️
Get started in just a few steps:

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/ProxyScanner.git
   pip install -r requirements.txt
   cd ProxyScanner
   python3 main.py
## How It Works 🛠️
- The script reads proxies from `proxies.txt`.
- Tests them in parallel using multiple threads (configurable in `config.json`).
- Saves working proxies to `working.txt` with details like IP, country, and ping.
> For example :
```bash
    52.28.174.92:3128
      IP: 52.28.174.92 | Country: Germany | Ping: 150 ms
```
## Why Go Pro Version? 💎

The Free Edition is awesome, but the Pro Edition takes it to the next level:
  - SOCKS4 & SOCKS5 support
  - Graphical User Interface (GUI)
  - Advanced filtering (by country, speed, etc.)
  - One-time payment: $10.99
  - Have API optimise
  - Get it here: Link to Pro (coming soon!)


## Contributing 🤝
Found a bug? Want to add a feature? Feel free to:
  - Open an issue
  - Submit a pull request

## License 📜
This project is licensed under the MIT License – see LICENSE for details
