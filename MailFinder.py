import os, re, sys, time, json, requests, random
from requests.exceptions import Timeout

r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"

W = f"{w}\033[1;47m"
R = f"{w}\033[1;41m"
G = f"{w}\033[1;42m"
Y = f"{w}\033[1;43m"
B = f"{w}\033[1;44m"

version = "1.7"
space = "    "
des_space = "⁣  ⁣⁣  ⁣⁣ "
lines = space + "—"*85
validator_url = str(requests.get("https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/validator.txt").text)
validator_url = validator_url.replace("\n", "")
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}
h_apis = ["5d5015259730682de8b542355525b16ab7026c976a72993d", "83e338e3a43cdcc649a1ea49957d2c0223b601bb", "36a4ce62890b18e216951bb2cf4b9748129418f8"]

def cls():
    if sys.platform == 'win32':
          # clear in windows, java
          os.system('cls')
    else:
          # clear in linux, android, ubuntu
          os.system('clear')

def update():
    script_name = sys.argv[0]
    version_py = sys.version_info.major
    os.system("rm -rf "+script_name)
    os.system("wget https://github.com/mishakorzik/MailFinder/blob/main/MailFinder.py?raw=true")
    os.system("mv MailFinder.py?raw=true "+script_name)
    try:
        if version_py == "3":
            os.system("python3 "+script_name)
        elif version_py == "2":
            os.system("python "+script_name)
        elif version_py == "1":
            os.system("python "+script_name)
        else:
            os.system("python3 "+script_name)
    except:
        print(f"{space}{b}[{w}!{b}]{w} Error! Failed to start MailFinder check if python is installed correctly...")

def restart():
    print("{space}{b}[{w}01{b}]{w} Error! You forgot to write something...")
    time.sleep(2)
    cls()
    os.execl(sys.executable, sys.executable, *sys.argv)

def banner():
    print(f'''{b}
     __   __  _______  ___   ___      _______  ___   __    _  ______   _______  ______
    |  |_|  ||   _   ||   | |   |    |       ||   | |  |  | ||      | |       ||    _ |
    |       ||  |_|  ||   | |   |    |    ___||   | |   |_| ||  _    ||    ___||   | ||
    |       ||       ||   | |   |    |   |___ |   | |       || | |   ||   |___ |   |_||_
    |       ||       ||   | |   |___ |    ___||   | |  _    || |_|   ||    ___||    __  |
    | ||_|| ||   _   ||   | |       ||   |    |   | | | |   ||       ||   |___ |   |  | |
    |_|   |_||__| |__||___| |_______||___|    |___| |_|  |__||______| |_______||___|  |_|''')
    print(f'                  {w}.:.:;..{y} MailFinder v'+version+f' Developer: misha korzhik {w}..;:.:.')
    print(f'\n{des_space}{b}>> {w}To find the mail you need, write your last name and \n{des_space}{b}>> {w}first name in different ways. For example: vuiko, vuikoo, vu\n{des_space}{b}>> {w}It still takes a long time to find your e-mail.\n')

def selecttype():
    #print(f"{space}{b}[{w}1{b}]{w} Search e-mail from database")
    print(f"{space}{b}[{w}1{b}]{w} Check e-mail domain in blacklist")
    print(f"{space}{b}[{w}2{b}]{w} Check username on emails domains")
    print(f"{space} {w}|")
    print(f"{space}{b}[{w}3{b}]{w} Search e-mail information, hunter.io")
    print(f"{space}{b}[{w}4{b}]{w} Search e-mail via fullname")
    print(f"{space}{b}[{w}5{b}]{w} Update MailFinder\n")
    type = str(input(f"{space}{b}[{w}?{b}]{w} Select a number:{b} ").lower())
    if type == "1" or type == "01":
        checkdomain()
    elif type == "2" or type == "02":
        validator()
    elif type == "3" or type == "03":
        emailinfo()
    elif type == "4" or type == "04":
        mailfinder()
    elif type == "5" or type == "05":
        update()
    else:
        restart()

def auto():
    time.sleep(1)
    cls()
    banner()

def checkdomain():
    cls()
    banner()
    domain = str(input(f"{space}{b}[{w}?{b}]{w} While domain (ex. gmail.com):{b} ").lower())
    get = requests.get(validator_url+"domain/verify?"+str(domain)).text
    print(" ")
    if "ok::good domain" in get:
        print(f"{space}{b}[{w}+{b}]{w} Verified domain : Yes")
        print(f"{space}{b}[{w}+{b}]{w} Phishing domain : No")
        print(f"{space}{b}[{w}+{b}]{w} Fake domain     : No")
    else:
        print(f"{space}{b}[{w}+{b}]{w} Verified domain : No")
        print(f"{space}{b}[{w}+{b}]{w} Phishing domain : Unknown")
        print(f"{space}{b}[{w}+{b}]{w} Fake domain     : Unknown")
    time.sleep(1)

def emailinfo():
    h_api = random.choice(h_apis)
    auto()
    email = str(input(f"{space}{b}[{w}?{b}]{w} Write an email for information:{b} ").lower())
    auto()
    try:
        get = requests.get("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+h_api).json()
        data = get['data']
        one = str(data['status'])
        two = str(data['result'])
        three = str(data['regexp'])
        four = str(data['gibberish'])
        five = str(data['disposable'])
        six = str(data['mx_records'])
        seven = str(data['smtp_server'])
        eight = str(data['smtp_check'])
        nine = str(data['block'])
        print(f"{space}{b}[{w}+{b}]{w} Email       : "+email)
        print(f"{space}{b}[{w}+{b}]{w} Status      : "+one)
        print(f"{space}{b}[{w}+{b}]{w} Result      : "+two)
        print(f"{space}{b}[{w}+{b}]{w} Regexp      : "+three)
        print(f"{space}{b}[{w}+{b}]{w} gibberish   : "+four)
        print(f"{space}{b}[{w}+{b}]{w} disposable  : "+five)
        print(f"{space}{b}[{w}+{b}]{w} mx_records  : "+six)
        print(f"{space}{b}[{w}+{b}]{w} smtp_server : "+seven)
        print(f"{space}{b}[{w}+{b}]{w} smtp_check  : "+eight)
        print(f"{space}{b}[{w}+{b}]{w} Block       : "+nine)
    except:
        auto()
        print(f"{space}{b}[{w}!{b}]{w} Oh no, it looks like the free api keys have run out")
        print(f"{space}{b}[{w}!{b}]{w} Create your api key on the hunter.io website")
        h_api = str(input(f"{space}{b}[{w}?{b}]{w} Write you hunter.io api key:{b} ").lower())
        get = requests.get("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+h_api).json()
        data = get['data']
        one = str(data['status'])
        two = str(data['result'])
        three = str(data['regexp'])
        four = str(data['gibberish'])
        five = str(data['disposable'])
        six = str(data['mx_records'])
        seven = str(data['smtp_server'])
        eight = str(data['smtp_check'])
        nine = str(data['block'])
        print(f"{space}{b}[{w}+{b}]{w} Email       : "+email)
        print(f"{space}{b}[{w}+{b}]{w} Status      : "+one)
        print(f"{space}{b}[{w}+{b}]{w} Result      : "+two)
        print(f"{space}{b}[{w}+{b}]{w} Regexp      : "+three)
        print(f"{space}{b}[{w}+{b}]{w} gibberish   : "+four)
        print(f"{space}{b}[{w}+{b}]{w} disposable  : "+five)
        print(f"{space}{b}[{w}+{b}]{w} mx_records  : "+six)
        print(f"{space}{b}[{w}+{b}]{w} smtp_server : "+seven)
        print(f"{space}{b}[{w}+{b}]{w} smtp_check  : "+eight)
        print(f"{space}{b}[{w}+{b}]{w} Block       : "+nine)
    finally:
        get = requests.get("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+h_api).text

def validator():
    auto()
    user = str(input(f"{space}{b}[{w}?{b}]{w} While user name to validate email:{b} ").lower())
    auto()
    print(w+lines)
    data = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "live.com",
        "icloud.com",
        "email.com",
        "aol.com",
        "qq.com",
        "comcast.net",
        "proton.me",
        "protonmail.com",
        "inbox.com",
        "football.ua",
        "i.ua",
        "email.ua",
        "3g.ua",
        "meta.ua",
        "ua.fm",
        "yandex.com",
        "yandex.ru",
        "yandex.by",
        "yandex.kz",
        "ya.ru",
        "mail.ru",
        "inbox.ru",
        "list.ru",
        "bk.ru",
        "internet.ru",
        "myrambler.ru",
        "rambler.ru",
        "autorambler.ru",
        "lenta.ru",
        "rambler.ua",
        "ro.ru",
        "zoho.com",
        "mailbox.org",
        "firemail.eu",
        "firemail.de",
        "firemail.at",
        "123mail.org",
        "runbox.com",
        "runbox.me",
        "runbox.email",
        "mailhost.work",
        "mailhouse.biz",
        "softbank.jp",
        "startmail.com"
        "gazeta.pl",
        "int.pl",
        "o2.pl",
        "wp.pl",
        "me.com",
        "onmail.com",
        "mail.com",
        "europe.com",
        "usa.com",
        "iname.com",
        "writeme.com",
        "asia.com",
        "engineer.com",
        "post.com",
        "dr.com",
        "myself.com",
        "coolsite.net",
        "consultant.com",
        "cheerful.com",
        "accountant.com",
        "cash4u.com",
        "cyberservices.com",
        "worker.com",
        "workmail.com",
        "europemail.com",
        "germanymail.com",
        "moscowmail.com",
        "mexicomail.com",
        "italymail.com",
        "programmer.net",
        "null.net",
        ]
    try:
        for domain in data:
            email = user + "@" + domain
            try:
                response = requests.get(validator_url+"validate?"+email, timeout=15).text
                if "ok::1" in response:
                    print(f"{space}{B} DONE {w} Status: {g}valided{w} Email: {email}")
                else:
                    print(f"{space}{R} FAIL {w} Status: {g}invalid{w} Email: {email}")
            except Timeout:
                    print(f"{space}{Y} EXIT {w} Status: {g}timeout{w} Email: {email}")
    except KeyboardInterrupt:
        print("\r"),;sys.stdout.flush()
        pass

def mailfinder():
    time.sleep(1.5)
    cls()
    banner()
    name = str(input(f"{space}{b}[{w}?{b}]{w} While victim first name:{b} ").lower())
    surname = str(input(f"{space}{b}[{w}?{b}]{w} While victim last name:{b} ").lower())
    time.sleep(1.5)
    cls()
    banner()
    #print(f"{space}{b}[{w}1{b}]{w} Services: gmail.com, yahoo.com, outlook.com, hotmail.com, live.com")
    #print(f"{space}{b}[{w}2{b}]{w} Services: yandex.com, yandex.ru, mail.ru, inbox.ru, list.ru")
    #print(f"{space}{b}[{w}3{b}]{w} Services: myrambler.ru, rambler.ru, lenta.ru, autorambler.ru, ro.ru")
    #print(f"{space}{b}[{w}4{b}]{w} Services: i.ua, email.ua, 3g.ua, meta.ua, ua.fm")
    data = []
    print(f"""{space}{b}[{w}?{b}]{w} For automatic search, write 'auto'""")
    type = str(input(f"{space}{b}[{w}?{b}]{w} While domain (ex. gmail.com):{b} ").lower())
    if type == "auto":
        data = ["gmail.com", "yahoo.com", "outlook.com"]
    else:
        data.append(type)
    print('')
    if not data: restart()
    if not name: restart()
    if not surname: restart()
    fullname = name + surname
    a_name = name
    a_surname = surname
    b_surname = surname
    time.sleep(1.5)
    cls()
    banner()
    #names
    if 'iy' in name: a_name = name.replace('iy', 'ij')
    elif 'ch' in name: a_name = name.replace('ch', 'c')
    elif 'sha' in name: a_name = name.replace('sha', 'sa')
    elif 'viy' in name: a_name = name.replace('viy', 'vi')

    #surname 1
    if 'ch' in surname: a_surname = surname.replace('ch', 'c')
    elif 'sh' in surname: a_surname = surname.replace('sh', 'z')
    elif 'tvie' in surname: a_surname = surname.replace('vie', 'viy')
    elif 'ushun' in surname: a_surname = surname.replace('ushu', 'yshy')
    elif 'kov' in surname: a_surname = surname.replace('ov', 'iv')
    elif 'kov' in surname: a_surname = surname.replace('uv', 'yv')
    elif 'zhi' in surname: a_surname = surname.replace('zhi', 'zi')
    elif 'ahl' in surname: a_surname = surname.replace('ahl', 'akhl')

    #surname 2
    if 'zhy' in surname: b_surname = surname.replace('zhy', 'zi')
    elif 'shi' in surname: b_surname = surname.replace('shi', 'shu')
    elif 'kh' in surname: b_surname = surname.replace('kh', 'h')
    elif 'me' in surname: b_surname = surname.replace('me', 'mme')
    _a = "0"+surname+"."
    _b = name + 'ik'
    _c = name + 'marmelad'
    print(w+lines)
    listuser = [
        _a.replace(" ","")+a_name+"777",
        _a.replace(" ","")+a_name+"62",
        _a.replace(" ","")+a_name+"122",
        _a.replace(" ","")+a_name+"528",
        _a.replace(" ","")+a_name+"538",
        _a.replace(" ","")+a_name+"122000",
        _a.replace(" ","")+a_name+"160511",
        _a.replace(" ","")+a_name,
        "www."+surname.replace(" ","")+a_name,
        surname.replace(" ","")+a_name+"0000",
        surname.replace(" ","")+a_name+"00000",
        surname.replace(" ","")+a_name+"0001",
        surname.replace(" ","")+a_name+"00001",
        surname.replace(" ","")+a_name+"100000",
        surname.replace(" ","")+a_name+"150611",
        surname.replace(" ","")+a_name+"122000",
        surname.replace(" ","")+a_name+"323",
        surname.replace(" ","")+a_name+"151",
        surname.replace(" ","")+a_name+"528",
        surname.replace(" ","")+a_name+"538",
        surname.replace(" ","")+a_name+"666",
        surname.replace(" ","")+a_name+"707",
        surname.replace(" ","")+a_name+"701",
        surname.replace(" ","")+a_name+"344",
        surname.replace(" ","")+a_name+"811",
        surname.replace(" ","")+a_name+"400",
        surname.replace(" ","")+a_name+"218",
        surname.replace(" ","")+a_name+"100",
        surname.replace(" ","")+a_name+"666",
        surname.replace(" ","")+a_name+"945",
        surname.replace(" ","")+"."+name,
        surname.replace(" ","")+"."+a_name,
        a_surname.replace(" ","")+name,
        a_surname.replace(" ","")+a_name,
        a_surname.replace(" ","")+"."+name,
        a_surname.replace(" ","")+"."+a_name,
        b_surname.replace(" ","")+name,
        b_surname.replace(" ","")+a_name,
        b_surname.replace(" ","")+"."+name,
        b_surname.replace(" ","")+"."+a_name,
        surname.replace(" ","")+"."+name,
        name.replace(" ","")+a_surname,
        name.replace(" ","")+"."+surname,
        surname.replace(" ","")+"."+_b,
        surname.replace(" ","")+"."+_c,
        surname.replace(" ","")+"."+a_name,
        surname.replace(" ","")+"."+_c+"707",
        surname.replace(" ","")+"."+_c+"777",
        surname.replace(" ","")+"."+_c+"906",
        surname.replace(" ","")+"."+_c+"969",
        surname.replace(" ","")+"."+_c+"700",
        surname.replace(" ","")+"."+_c+"600",
        surname.replace(" ","")+"."+_c+"323",
        surname.replace(" ","")+"."+_c+"313",
        surname.replace(" ","")+"."+_c+"500",
        surname.replace(" ","")+"."+_c+"400",
        surname.replace(" ","")+"."+_c+"218",
        surname.replace(" ","")+"."+_c+"151",
        surname.replace(" ","")+"."+_c+"99",
        surname.replace(" ","")+"."+_c+"89",
        surname.replace(" ","")+"."+_c+"61",
        surname.replace(" ","")+"."+_c+"62",
        surname.replace(" ","")+"."+_c+"71",
        surname.replace(" ","")+"."+_c+"81",
        surname.replace(" ","")+"."+_c+"95",
        surname.replace(" ","")+"."+_c+"85",
        surname.replace(" ","")+"."+_c+"60",
        surname.replace(" ","")+"."+_c+"50",
        surname.replace(" ","")+"."+_c+"55",
        surname.replace(" ","")+"."+_c+"1",
        surname.replace(" ","")+"."+_c+"7",
        surname.replace(" ","")+"."+_c+"6",
        surname.replace(" ","")+"."+_c+"10",
        surname.replace(" ","")+"."+_c+"9",
        surname.replace(" ","")+"."+_c+"8",
        surname.replace(" ","")+"."+_c+"3",
        surname.replace(" ","")+"."+_c+"2",
        surname.replace(" ","")+"."+_c+"881",
        surname.replace(" ","")+"."+_c+"999",
        surname.replace(" ","")+"."+_c+"222",
        surname.replace(" ","")+"."+_c+"393",
        surname.replace(" ","")+"."+_c+"383",
        "www."+fullname.replace(" ",""),
        fullname.replace(" ","")+"150611",
        fullname.replace(" ","")+"2189",
        fullname.replace(" ","")+"e80",
        fullname.replace(" ","")+"717",
        fullname.replace(" ","")+"707",
        fullname.replace(" ","")+"760",
        fullname.replace(" ","")+"999",
        fullname.replace(" ","")+"666",
        fullname.replace(" ","")+"809",
        fullname.replace(" ","")+"807",
        fullname.replace(" ","")+"888",
        fullname.replace(" ","")+"848",
        fullname.replace(" ","")+"844",
        fullname.replace(" ","")+"909",
        fullname.replace(" ","")+"900",
        fullname.replace(" ","")+"950",
        fullname.replace(" ","")+"955",
        fullname.replace(" ","")+"960",
        fullname.replace(" ","")+"970",
        fullname.replace(" ","")+"670",
        fullname.replace(" ","")+"610",
        fullname.replace(" ","")+"606",
        fullname.replace(" ","")+"650",
        fullname.replace(" ","")+"681",
        fullname.replace(" ","")+"662",
        fullname.replace(" ","")+"555",
        fullname.replace(" ","")+"505",
        fullname.replace(" ","")+"550",
        fullname.replace(" ","")+"525",
        fullname.replace(" ","")+"537",
        fullname.replace(" ","")+"531",
        fullname.replace(" ","")+"411",
        fullname.replace(" ","")+"477",
        fullname.replace(" ","")+"444",
        fullname.replace(" ","")+"499",
        fullname.replace(" ","")+"323",
        fullname.replace(" ","")+"333",
        fullname.replace(" ","")+"321",
        fullname.replace(" ","")+"388",
        fullname.replace(" ","")+"370",
        fullname.replace(" ","")+"300",
        fullname.replace(" ","")+"299",
        fullname.replace(" ","")+"288",
        fullname.replace(" ","")+"270",
        fullname.replace(" ","")+"277",
        fullname.replace(" ","")+"266",
        fullname.replace(" ","")+"240",
        fullname.replace(" ","")+"244",
        fullname.replace(" ","")+"255",
        fullname.replace(" ","")+"232",
        fullname.replace(" ","")+"222",
        fullname.replace(" ","")+"218",
        fullname.replace(" ","")+"211",
        fullname.replace(" ","")+"200",
        fullname.replace(" ","")+"199",
        fullname.replace(" ","")+"189",
        fullname.replace(" ","")+"188",
        fullname.replace(" ","")+"166",
        fullname.replace(" ","")+"165",
        fullname.replace(" ","")+"169",
        fullname.replace(" ","")+"196",
        fullname.replace(" ","")+"151",
        fullname.replace(" ","")+"150",
        fullname.replace(" ","")+"142",
        fullname.replace(" ","")+"133",
        fullname.replace(" ","")+"120",
        fullname.replace(" ","")+"111",
        fullname.replace(" ","")+"100",
        fullname.replace(" ","")+"707",
        fullname.replace(" ","")+"000",
        fullname.replace(" ","")+"00",
        fullname.replace(" ","")+"62",
        fullname.replace(" ","")+"71",
        fullname.replace(" ","")+"54",
        fullname.replace(" ","")+"23",
        fullname.replace(" ","")+"22",
        fullname.replace(" ","")+"99",
        fullname.replace(" ","")+"89",
        fullname.replace(" ","")+"69",
        fullname.replace(" ","")+"96",
        fullname.replace(" ","")+"60",
        fullname.replace(" ","")+"59",
        fullname.replace(" ","")+"11",
        fullname.replace(" ","")+"10",
        fullname.replace(" ","")+"9",
        fullname.replace(" ","")+"7",
        fullname.replace(" ","")+"6",
        fullname.replace(" ","")+"4",
        fullname.replace(" ","")+"3",
        fullname.replace(" ","")+"2",
        fullname.replace(" ","")+"1",
        fullname.replace(" ","")+"0",
        fullname.replace(" ",""),
        "www."+surname.replace(" ","")+a_name,
        surname.replace(" ","")+a_name+"2189",
        surname.replace(" ","")+a_name+"380",
        surname.replace(" ","")+a_name+"323",
        surname.replace(" ","")+a_name+"528",
        surname.replace(" ","")+a_name+"538",
        surname.replace(" ","")+a_name+"666",
        surname.replace(" ","")+a_name+"707",
        surname.replace(" ","")+a_name+"701",
        surname.replace(" ","")+a_name+"344",
        surname.replace(" ","")+a_name+"811",
        surname.replace(" ","")+a_name+"400",
        surname.replace(" ","")+a_name+"100",
        surname.replace(" ","")+a_name+"666",
        surname.replace(" ","")+a_name+"945",
        surname.replace(" ","")+a_name+"888",
        surname.replace(" ","")+a_name+"111",
        surname.replace(" ","")+a_name+"222",
        surname.replace(" ","")+a_name+"333",
        surname.replace(" ","")+a_name+"444",
        surname.replace(" ","")+a_name+"555",
        surname.replace(" ","")+a_name+"888",
        surname.replace(" ","")+a_name+"777",
        surname.replace(" ","")+a_name+"999",
        surname.replace(" ","")+a_name+"000",
        surname.replace(" ","")+a_name+"001",
        surname.replace(" ","")+a_name+"002",
        surname.replace(" ","")+a_name+"003",
        surname.replace(" ","")+a_name+"877",
        surname.replace(" ","")+a_name+"312",
        surname.replace(" ","")+a_name+"841",
        surname.replace(" ","")+a_name+"808",
        surname.replace(" ","")+a_name+"607",
        surname.replace(" ","")+a_name+"151",
        surname.replace(" ","")+a_name+"150",
        surname.replace(" ","")+a_name+"61",
        surname.replace(" ","")+a_name+"81",
        surname.replace(" ","")+a_name+"79",
        surname.replace(" ","")+a_name+"41",
        surname.replace(" ","")+a_name+"42",
        surname.replace(" ","")+a_name+"44",
        surname.replace(" ","")+a_name+"56",
        surname.replace(" ","")+a_name+"55",
        surname.replace(" ","")+a_name+"57",
        surname.replace(" ","")+a_name+"69",
        surname.replace(" ","")+a_name+"12",
        surname.replace(" ","")+a_name+"11",
        surname.replace(" ","")+a_name+"10",
        surname.replace(" ","")+a_name+"32",
        surname.replace(" ","")+a_name+"36",
        surname.replace(" ","")+a_name+"76",
        surname.replace(" ","")+a_name+"40",
        surname.replace(" ","")+a_name+"9",
        surname.replace(" ","")+a_name+"8",
        surname.replace(" ","")+a_name+"7",
        surname.replace(" ","")+a_name+"6",
        surname.replace(" ","")+a_name+"5",
        surname.replace(" ","")+a_name+"4",
        surname.replace(" ","")+a_name+"3",
        surname.replace(" ","")+a_name+"2",
        surname.replace(" ","")+a_name+"1",
        surname.replace(" ","")+a_name+"0",
        name.replace(" ","")+a_surname,
        a_name.replace(" ","")+a_surname,
        #a_surname a_name
        a_surname.replace(" ","")+a_name+"0000",
        a_surname.replace(" ","")+a_name+"00000",
        a_surname.replace(" ","")+a_name+"0001",
        a_surname.replace(" ","")+a_name+"00001",
        a_surname.replace(" ","")+a_name+"100000",
        a_surname.replace(" ","")+a_name+"150611",
        a_surname.replace(" ","")+a_name+"122000",
        a_surname.replace(" ","")+a_name+"607",
        a_surname.replace(" ","")+a_name+"1010",
        a_surname.replace(" ","")+a_name+"1111",
        a_surname.replace(" ","")+a_name+"150611",
        a_surname.replace(" ","")+a_name+"263",
        a_surname.replace(" ","")+a_name+"1000",
        a_surname.replace(" ","")+a_name+"380",
        a_surname.replace(" ","")+a_name+"706",
        a_surname.replace(" ","")+a_name+"323",
        a_surname.replace(" ","")+a_name+"528",
        a_surname.replace(" ","")+a_name+"538",
        a_surname.replace(" ","")+a_name+"666",
        a_surname.replace(" ","")+a_name+"707",
        a_surname.replace(" ","")+a_name+"701",
        a_surname.replace(" ","")+a_name+"344",
        a_surname.replace(" ","")+a_name+"811",
        a_surname.replace(" ","")+a_name+"400",
        a_surname.replace(" ","")+a_name+"100",
        a_surname.replace(" ","")+a_name+"666",
        a_surname.replace(" ","")+a_name+"945",
        a_surname.replace(" ","")+a_name+"888",
        a_surname.replace(" ","")+a_name+"111",
        a_surname.replace(" ","")+a_name+"222",
        a_surname.replace(" ","")+a_name+"333",
        a_surname.replace(" ","")+a_name+"444",
        a_surname.replace(" ","")+a_name+"555",
        a_surname.replace(" ","")+a_name+"888",
        a_surname.replace(" ","")+a_name+"777",
        a_surname.replace(" ","")+a_name+"999",
        a_surname.replace(" ","")+a_name+"000",
        a_surname.replace(" ","")+a_name+"001",
        a_surname.replace(" ","")+a_name+"002",
        a_surname.replace(" ","")+a_name+"003",
        a_surname.replace(" ","")+a_name+"877",
        a_surname.replace(" ","")+a_name+"312",
        a_surname.replace(" ","")+a_name+"841",
        a_surname.replace(" ","")+a_name+"808",
        a_surname.replace(" ","")+a_name+"607",
        a_surname.replace(" ","")+a_name+"151",
        a_surname.replace(" ","")+a_name+"62",
        a_surname.replace(" ","")+a_name+"61",
        a_surname.replace(" ","")+a_name+"81",
        a_surname.replace(" ","")+a_name+"79",
        a_surname.replace(" ","")+a_name+"41",
        a_surname.replace(" ","")+a_name+"42",
        a_surname.replace(" ","")+a_name+"44",
        a_surname.replace(" ","")+a_name+"56",
        a_surname.replace(" ","")+a_name+"55",
        a_surname.replace(" ","")+a_name+"57",
        a_surname.replace(" ","")+a_name+"69",
        a_surname.replace(" ","")+a_name+"12",
        a_surname.replace(" ","")+a_name+"11",
        a_surname.replace(" ","")+a_name+"10",
        a_surname.replace(" ","")+a_name+"32",
        a_surname.replace(" ","")+a_name+"36",
        a_surname.replace(" ","")+a_name+"76",
        a_surname.replace(" ","")+a_name+"40",
        a_surname.replace(" ","")+a_name+"9",
        a_surname.replace(" ","")+a_name+"8",
        a_surname.replace(" ","")+a_name+"7",
        a_surname.replace(" ","")+a_name+"6",
        a_surname.replace(" ","")+a_name+"5",
        a_surname.replace(" ","")+a_name+"4",
        a_surname.replace(" ","")+a_name+"3",
        a_surname.replace(" ","")+a_name+"2",
        a_surname.replace(" ","")+a_name+"1",
        a_surname.replace(" ","")+a_name+"0",
        a_surname.replace(" ","")+a_name,
        #a_name a_surname
        a_surname.replace(" ","")+a_name+"989",
        a_surname.replace(" ","")+a_name+"150611",
        a_surname.replace(" ","")+a_name+"706",
        a_surname.replace(" ","")+a_name+"708",
        a_surname.replace(" ","")+a_name+"3331",
        a_name.replace(" ","")+a_surname+"0000",
        a_name.replace(" ","")+a_surname+"00000",
        a_name.replace(" ","")+a_surname+"0001",
        a_name.replace(" ","")+a_surname+"00001",
        a_name.replace(" ","")+a_surname+"100000",
        a_name.replace(" ","")+a_surname+"150611",
        a_name.replace(" ","")+a_surname+"122000",
        a_name.replace(" ","")+a_surname+"380",
        a_name.replace(" ","")+a_surname+"323",
        a_name.replace(" ","")+a_surname+"528",
        a_name.replace(" ","")+a_surname+"538",
        a_name.replace(" ","")+a_surname+"666",
        a_name.replace(" ","")+a_surname+"707",
        a_name.replace(" ","")+a_surname+"701",
        a_name.replace(" ","")+a_surname+"344",
        a_name.replace(" ","")+a_surname+"811",
        a_name.replace(" ","")+a_surname+"400",
        a_name.replace(" ","")+a_surname+"100",
        a_name.replace(" ","")+a_surname+"666",
        a_name.replace(" ","")+a_surname+"945",
        a_name.replace(" ","")+a_surname+"888",
        a_name.replace(" ","")+a_surname+"111",
        a_name.replace(" ","")+a_surname+"222",
        a_name.replace(" ","")+a_surname+"333",
        a_name.replace(" ","")+a_surname+"444",
        a_name.replace(" ","")+a_surname+"555",
        a_name.replace(" ","")+a_surname+"888",
        a_name.replace(" ","")+a_surname+"777",
        a_name.replace(" ","")+a_surname+"999",
        a_name.replace(" ","")+a_surname+"000",
        a_name.replace(" ","")+a_surname+"001",
        a_name.replace(" ","")+a_surname+"002",
        a_name.replace(" ","")+a_surname+"003",
        a_name.replace(" ","")+a_surname+"877",
        a_name.replace(" ","")+a_surname+"312",
        a_name.replace(" ","")+a_surname+"841",
        a_name.replace(" ","")+a_surname+"808",
        a_name.replace(" ","")+a_surname+"607",
        a_name.replace(" ","")+a_surname+"151",
        a_name.replace(" ","")+a_surname+"217",
        a_name.replace(" ","")+a_surname+"62",
        a_name.replace(" ","")+a_surname+"61",
        a_name.replace(" ","")+a_surname+"81",
        a_name.replace(" ","")+a_surname+"79",
        a_name.replace(" ","")+a_surname+"41",
        a_name.replace(" ","")+a_surname+"42",
        a_name.replace(" ","")+a_surname+"44",
        a_name.replace(" ","")+a_surname+"56",
        a_name.replace(" ","")+a_surname+"55",
        a_name.replace(" ","")+a_surname+"57",
        a_name.replace(" ","")+a_surname+"69",
        a_name.replace(" ","")+a_surname+"12",
        a_name.replace(" ","")+a_surname+"11",
        a_name.replace(" ","")+a_surname+"10",
        a_name.replace(" ","")+a_surname+"32",
        a_name.replace(" ","")+a_surname+"36",
        a_name.replace(" ","")+a_surname+"76",
        a_name.replace(" ","")+a_surname+"40",
        a_name.replace(" ","")+a_surname+"9",
        a_name.replace(" ","")+a_surname+"8",
        a_name.replace(" ","")+a_surname+"7",
        a_name.replace(" ","")+a_surname+"6",
        a_name.replace(" ","")+a_surname+"5",
        a_name.replace(" ","")+a_surname+"4",
        a_name.replace(" ","")+a_surname+"3",
        a_name.replace(" ","")+a_surname+"2",
        a_name.replace(" ","")+a_surname+"1",
        a_name.replace(" ","")+a_surname+"0",
        #name a_surname
        name.replace(" ","")+a_surname,
        name.replace(" ","")+a_surname+"380",
        name.replace(" ","")+a_surname+"323",
        name.replace(" ","")+a_surname+"528",
        name.replace(" ","")+a_surname+"538",
        name.replace(" ","")+a_surname+"666",
        name.replace(" ","")+a_surname+"707",
        name.replace(" ","")+a_surname+"701",
        name.replace(" ","")+a_surname+"344",
        name.replace(" ","")+a_surname+"811",
        name.replace(" ","")+a_surname+"400",
        name.replace(" ","")+a_surname+"100",
        name.replace(" ","")+a_surname+"666",
        name.replace(" ","")+a_surname+"945",
        name.replace(" ","")+a_surname+"888",
        name.replace(" ","")+a_surname+"111",
        name.replace(" ","")+a_surname+"222",
        name.replace(" ","")+a_surname+"333",
        name.replace(" ","")+a_surname+"444",
        name.replace(" ","")+a_surname+"555",
        name.replace(" ","")+a_surname+"888",
        name.replace(" ","")+a_surname+"777",
        name.replace(" ","")+a_surname+"999",
        name.replace(" ","")+a_surname+"000",
        name.replace(" ","")+a_surname+"001",
        name.replace(" ","")+a_surname+"002",
        name.replace(" ","")+a_surname+"003",
        name.replace(" ","")+a_surname+"877",
        name.replace(" ","")+a_surname+"312",
        name.replace(" ","")+a_surname+"841",
        name.replace(" ","")+a_surname+"808",
        name.replace(" ","")+a_surname+"607",
        name.replace(" ","")+a_surname+"62",
        name.replace(" ","")+a_surname+"61",
        name.replace(" ","")+a_surname+"81",
        name.replace(" ","")+a_surname+"79",
        name.replace(" ","")+a_surname+"41",
        name.replace(" ","")+a_surname+"42",
        name.replace(" ","")+a_surname+"44",
        name.replace(" ","")+a_surname+"56",
        name.replace(" ","")+a_surname+"55",
        name.replace(" ","")+a_surname+"57",
        name.replace(" ","")+a_surname+"69",
        name.replace(" ","")+a_surname+"12",
        name.replace(" ","")+a_surname+"11",
        name.replace(" ","")+a_surname+"10",
        name.replace(" ","")+a_surname+"32",
        name.replace(" ","")+a_surname+"36",
        name.replace(" ","")+a_surname+"76",
        name.replace(" ","")+a_surname+"40",
        name.replace(" ","")+a_surname+"9",
        name.replace(" ","")+a_surname+"8",
        name.replace(" ","")+a_surname+"7",
        name.replace(" ","")+a_surname+"6",
        name.replace(" ","")+a_surname+"5",
        name.replace(" ","")+a_surname+"4",
        name.replace(" ","")+a_surname+"3",
        name.replace(" ","")+a_surname+"2",
        name.replace(" ","")+a_surname+"1",
        _b.replace(" ","")+surname,
        _b.replace(" ","")+surname+"5",
        _b.replace(" ","")+surname+"6",
        _b.replace(" ","")+surname+"3021",
        _b.replace(" ","")+surname+"0000",
        _b.replace(" ","")+surname+"001",
        _b.replace(" ","")+surname+"top",
        _b.replace(" ","")+surname+"mini",
        _b.replace(" ","")+surname+"kik",
        _b.replace(" ","")+surname+"heh",
        _b.replace(" ","")+surname+"706",
        _b.replace(" ","")+surname+"380",
        _b.replace(" ","")+surname+"62",
        _b.replace(" ","")+surname+"707",
        _b.replace(" ","")+surname+"81",
        _b.replace(" ","")+surname+"312",
        _b.replace(" ","")+surname+"323",
        _b.replace(" ","")+surname+"150611",
        _b.replace(" ","")+surname+"001",
        _b.replace(" ","")+surname+"1",
        _b.replace(" ","")+surname+"2",
        _b.replace(" ","")+surname+"3",
        _b.replace(" ","")+surname+"4",
        _b.replace(" ","")+surname+"7",
        _b.replace(" ","")+surname+"54",
        _b.replace(" ","")+surname+"55",
        _b.replace(" ","")+surname+"528",
        _b.replace(" ","")+surname+"538",
        _b.replace(" ","")+surname+"81",
        _b.replace(" ","")+surname+"96",
        _b.replace(" ","")+surname+"000",
        _b.replace(" ","")+surname+"44",
        _b.replace(" ","")+surname+"43",
        _b.replace(" ","")+surname+"2000",
        _b.replace(" ","")+surname+"2001",
        _b.replace(" ","")+surname+"2002",
        _b.replace(" ","")+surname+"2003",
        _b.replace(" ","")+surname+"2004",
        _b.replace(" ","")+surname+"2005",
        _b.replace(" ","")+surname+"2006",
        _b.replace(" ","")+surname+"2007",
        _b.replace(" ","")+surname+"2008",
        _b.replace(" ","")+surname+"2009",
        _b.replace(" ","")+surname+"72",
        _b.replace(" ","")+surname+"82",
        _b.replace(" ","")+surname+"98",
        _b.replace(" ","")+surname+"97",
        _b.replace(" ","")+surname+"89",
        _b.replace(" ","")+surname+"61",
        _b.replace(" ","")+surname+"53",
        _b.replace(" ","")+surname+"52",
        _b.replace(" ","")+surname+"199",
        _b.replace(" ","")+surname+"198",
        ]
    file = open("result.txt","w")
    ok = []
    try:
        for user in listuser:
            for domain in data:
                email = user + "@" + domain
                response = requests.get(validator_url+"validate?"+email, timeout=15).text
                if "ok::1" in response:
                    file.write(email+"\n")
                    ok.append(email)
                    print(f"{space}{B} DONE {w} Status: {g}valid{w} Email: {email}")
                elif response == "3":
                    print(f"{space}{Y} EXIT {w} Status: {g}timeout{w} Email: {email}")
                else:
                    #print(f"{space}{R} FAIL {w} Status: {g}invalid{w} Email: {email}")
                    pass
    except requests.exceptions.ReadTimeout:
        pass
    except TimeoutError:
        pass
    except requests.exceptions.SSLError:
        pass
    except KeyboardInterrupt:
        print("\r"),;sys.stdout.flush()
        pass
    file.close()
    print(w+lines)
    print(f"{space}{b}>{w} {str(len(ok))} retrieved as: {y}result.txt{w}")

cls()
banner()
selecttype()
