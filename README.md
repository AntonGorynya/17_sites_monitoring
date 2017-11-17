# Sites Monitoring Utility

This script monitor sites from fille.
Check correct responce from server and domain date expired

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart

You can download and run it directly through console

Example of script launch on Linux, Python 3.5:

```bash
check_sites_health.py urls.txt

https://www.ya.ru is OK
domain name https://www.ya.ru is paid

https://www.mail.ru is OK
domain name https://www.mail.ru is paid

https://www.vk.com is OK
domain name https://www.vk.com is paid
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
