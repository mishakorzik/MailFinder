import dns.resolver
import socket
import smtplib
import requests
import random
import string
import json
import socks

tor = "socks5://127.0.0.1:51567"
ua = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
]

proxies = {"http": tor, "https": tor}

_tor = tor.replace("socks5://", "")
ip, port = _tor.split(":")

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, int(port))
socks.wrapmodule(smtplib)

def validate(email):
    nickname, domain = email.split("@")
    if domain in ["gmail.com", "yahoo.com", "yandex.ru", "yandex.com", "yandex.by", "yandex.kz", "ya.ru"]:
        records = dns.resolver.resolve(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        host = socket.gethostname()
        server = smtplib.SMTP()
        #server.set_debuglevel(0)
        server.connect(mxRecord[:-1])
        server.helo(host)
        server.mail(email)
        code, message = server.rcpt(str(email))
        server.quit()
        if code == 250:
            return "1"
        else:
            return "0"
    elif domain in ["mail.ru", "bk.ru", "inbox.ru", "list.ru", "internet.ru"]:
        headers = {"User-Agent": random.choice(ua)}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.post("https://account.mail.ru/api/v1/user/exists?email="+str(email), headers=headers, timeout=7)
        if resp.status_code == 200:
            if exists := resp.json()['body']['exists']:
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["ukr.net"]:
        headers = {
            "User-Agent": random.choice(ua),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "DNT": "1",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.get("https://accounts.ukr.net:443/registration", headers=headers, timeout=7)
        if resp.status_code == 200:
            resp = s.post("https://accounts.ukr.net:443/api/v1/registration/reserve_login", json={"login": nickname}, headers=headers, timeout=7)
            if resp.status_code == 200:
                if not resp.json()['available']:
                    return "1"
                else:
                    return "0"
        else:
            return "3"
    elif domain in ["gazeta.pl"]:
        headers = {
            "User-Agent": random.choice(ua),
            "Referer": "https://konto.gazeta.pl/konto/rejestracja.do",
            "Accept": "*/*"
        }
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.get(f"https://konto.gazeta.pl/konto/checkLogin?login={nickname}&nosuggestions=true", headers=headers, timeout=7)
        if resp.status_code == 200:
            if resp.json()["available"] == "0":
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["onet.pl", "op.pl", "adres.pl", "vp.pl", "onet.eu", "cyberia.pl", "pseudonim.pl", "autograf.pl", "opoczta.pl", "spoko.pl", "amorki.pl", "buziaczek.pl", "poczta.onet.pl", "poczta.onet.eu", "onet.com.pl", "vip.onet.pl"]:
        headers = {
            "User-Agent": random.choice(ua),
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Referer": "https://konto.onet.pl/"}
        data = {
            "login": nickname,
            "captcha_response":"meow",
            "state":"https://poczta.onet.pl/"}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.post("https://konto.onet.pl/newapi/oauth/check-register-email-identity", headers=headers, data=json.dumps(data), timeout=7)
        if resp.status_code == 200:
            if not email in resp.json()["emails"]:
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["vivaldi.net"]:
        headers = {
            "User-Agent": random.choice(ua),
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://login.vivaldi.net",
            "Referer": "https://login.vivaldi.net/profile/id/signup"}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.post("https://login.vivaldi.net:443/profile/validateField", headers=headers, data={"field": "username", "value": nickname}, timeout=7)
        if resp.status_code == "200":
            if 'error' in resp.json() and resp.json()['error'] == "User exists [1007]":
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["mailbox.org"]:
        headers = {"User-Agent": random.choice(ua)}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.post("https://register.mailbox.org:443/ajax", headers=headers, json={"account_name": nickname, "action": "validateAccountName"}, timeout=7)
        if resp.status_code == 200:
            if resp.text == "Der Accountname existiert bereits.":
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["tutanota.com", "tutanota.de", "tutamail.com", "tuta.io", "keemail.me"]:
        headers = {"User-Agent": random.choice(ua)}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.get(f'https://mail.tutanota.com/rest/sys/mailaddressavailabilityservice?_body=%7B%22_format%22%3A%220%22%2C%22mailAddress%22%3A%22{nickname}%40{domain}%22%7D', headers=headers, timeout=7)
        if resp.status_code == 200:
            if resp.json()['available'] == "0":
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["firemail.at", "firemail.de", "firemail.eu"]:
        headers = {'User-Agent': random.choice(ua), 'Referer': 'https://firemail.de/E-Mail-Adresse-anmelden', 'X-Requested-With': 'XMLHttpRequest'}
        s = requests.Session()
        s.proxies.update(proxies)
        resp = s.get("https://firemail.de/index.php?action=checkAddressAvailability&address="+email, headers=headers, timeout=7)
        if resp.status_code == 200:
            if '>0<' in resp.text:
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["hotmail.com", "outlook.com", "live.com"]:
        apis = ["847edcb494d94b18bc6eed3046fa31b6", "05cc1ce01d0745799e137a986683e074", "d49ede9756994cf7bb381314761586aa", "4722441959ce4230a25f542305e148d6", "b633355a4c464dbb85ed927030f6166c"]
        api = random.choice(apis)
        resp = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key={api}&email={email}")
        if resp.status_code == 200:
            if resp.json()["deliverability"] == "DELIVERABLE":
                return "1"
            else:
                return "0"
        else:
            return "3"
    elif domain in ["rambler.ua", "rambler.ru", "myrambler.ru", "autorambler.ru", "ro.ru"]:
        #apis = ["", "", "", "", "", ""]
        #api = random.choice(apis)
        api = "b633355a4c464dbb85ed927030f6166c"
        resp = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key={api}&email={email}")
        if resp.status_code == 200:
            if resp.json()["deliverability"] == "DELIVERABLE":
                return "1"
            else:
                return "0"
        else:
            return "3"
