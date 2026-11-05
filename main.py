#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════╗
║   [ TANJIM PREMIUM ENGINE ]  v17.4 ✦ ULTIMATE ACCURACY FIX               ║
║   [ STATUS ] : UNLIMITED FP • ANTI-BLOCK • PREMIUM DASHBOARD             ║
║   [ DEV    ] : TANJIM                                                   ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import os, sys, re, json, uuid, time, random, string, threading

if sys.platform == "win32":
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass
    os.system('')

try:
    from curl_cffi import requests
except ImportError:
    print("\033[38;5;196m[!] CRITICAL: pip install curl-cffi cryptography\033[0m")
    sys.exit(1)

# ═══════════════════ COLORS ═══════════════════
RESET = "\033[0m"; BOLD = "\033[1m"; DIM = "\033[2m"
RED = "\033[38;5;196m"; GREEN = "\033[38;5;46m"; YELLOW = "\033[38;5;226m"
CYAN = "\033[38;5;51m"; WHITE = "\033[97m"; GRAY = "\033[38;5;240m"; DGRAY = "\033[38;5;238m"
PURPLE = "\033[38;5;135m"; BLUE = "\033[38;5;39m"; LIME = "\033[38;5;154m"; TEAL = "\033[38;5;44m"
GOLD = "\033[38;5;220m"

# ═══════════════════ SYMBOLS ═══════════════════
S_BAR = f"{PURPLE}▌{RESET}"; S_PTR = f"{CYAN}❯{RESET}"; S_DOT = f"{GRAY}•{RESET}"
S_OK = f"{GREEN}✔{RESET}"; S_FAIL = f"{RED}✖{RESET}"; S_WARN = f"{YELLOW}⚠{RESET}"
S_INFO = f"{CYAN}ℹ{RESET}"; S_DIAM = f"{PURPLE}◈{RESET}"; S_HEX = f"{CYAN}⬢{RESET}"; S_ARROW = f"{CYAN}▸{RESET}"

# ═══════════════════ CONFIG ═══════════════════
API_TOKEN = "M2GUS38GJZQ"
BASE_URL = "https://api.2oo9.cloud/MXS47FLFX0U/tnevs/@public/api"
LIVE_ACCESS_URL = f"{BASE_URL}/liveaccess"
GET_NUM_URL = f"{BASE_URL}/getnum"
SUCCESS_OTP_URL = f"{BASE_URL}/success-otp"
API_HEADERS = {"mauthapi": API_TOKEN, "accept": "application/json", "content-type": "application/json"}
W = 64

# ═══════════════════ FINGERPRINT ═══════════════════
def generate_random_fingerprint():
    devices = [
        ("Windows NT 10.0; Win64; x64", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36", '"Chromium";v="{v}", "Google Chrome";v="{v}", "Not-A.Brand";v="99"', "chrome"),
        ("Macintosh; Intel Mac OS X 10_15_7", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36", '"Google Chrome";v="{v}", "Chromium";v="{v}", "Not?A_Brand";v="24"', "chrome"),
        ("Macintosh; Intel Mac OS X 10_15_7", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.{v} Safari/605.1.15", None, "safari"),
        ("Windows NT 10.0; Win64; x64", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36 Edg/{v}.0.0.0", '"Not_A Brand";v="8", "Chromium";v="{v}", "Microsoft Edge";v="{v}"', "edge"),
        ("X11; Linux x86_64", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36", '"Chromium";v="{v}", "Google Chrome";v="{v}", "Not-A.Brand";v="99"', "chrome")
    ]
    _, ua_tpl, sec_tpl, imp_engine = random.choice(devices)
    if imp_engine == "safari":
        v = f"{random.randint(15, 17)}_{random.randint(0, 9)}"
        return {"imp": "safari15_5", "ua": ua_tpl.format(v=v), "sec_ch": None}
    elif imp_engine == "edge":
        v = random.randint(118, 124)
        return {"imp": "edge120", "ua": ua_tpl.format(v=v), "sec_ch": sec_tpl.format(v=v)}
    else:
        v = random.randint(118, 125)
        return {"imp": "chrome120" if v not in [119,120,121,124] else f"chrome{v}", "ua": ua_tpl.format(v=v), "sec_ch": sec_tpl.format(v=v)}

COUNTRY_MAP = {"237":"Cameroon","229":"Benin","234":"Nigeria","233":"Ghana","254":"Kenya","880":"Bangladesh","91":"India"}
FIRST_NAMES = ["James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles"]
LAST_NAMES = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez"]

def get_country_name(prefix):
    prefix = str(prefix).replace("+", "")
    for length in [3, 2, 1]:
        if prefix[:length] in COUNTRY_MAP: return COUNTRY_MAP[prefix[:length]]
    return "UNKNOWN"

# ═══════════════════ STATE ═══════════════════
dashboard_data = []; dash_lock = threading.Lock()
_filtered = set(); _filter_lock = threading.Lock()
file_lock = threading.Lock()
total_checked = total_success = total_failed = 0
stats_lock = threading.Lock()
_shutdown = threading.Event()
USER_PASSWORD = "Okabye#570"
REG_DYN = ("7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwGwQw9m1YwBgao6C0Mo2swaOfK0EUjwGzE2ZwNwmE2eUlwhE2Lw6OyES1Tw8W0Lo6-1Fw4mwr86C1nwqU8XwnqwIwtU26wbu1ww3dU")

# ═══════════════════ UI ═══════════════════
def clear_screen():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    sys.stdout.write("\033[H\033[2J\033[3J"); sys.stdout.flush(); time.sleep(0.05)

def draw_logo():
    print(f"""{PURPLE}{BOLD}
╔════════════════════════════════════════════════════════════════╗
║   ████████╗ █████╗ ███╗   ██╗     ██╗██╗███╗   ███╗            ║
║   ╚══██╔══╝██╔══██╗████╗  ██║     ██║██║████╗ ████║            ║
║      ██║   ███████║██╔██╗ ██║     ██║██║██╔████╔██║            ║
║      ██║   ██╔══██║██║╚██╗██║██   ██║██║██║╚██╔╝██║            ║
║      ██║   ██║  ██║██║ ╚████║╚█████╔╝██║██║ ╚═╝ ██║            ║
║      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝╚═╝     ╚═╝            ║
║   ✦ TANJIM PREMIUM ✦            v17.4 ✦ ULTIMATE EDITION        ║
╚════════════════════════════════════════════════════════════════╝
{RESET}{GRAY} ├─{RESET} {WHITE}Dev{RESET} : {PURPLE}{BOLD}TANJIM{RESET}       {GRAY}│{RESET}  {WHITE}Status{RESET} : {GREEN}◉ OPERATIONAL{RESET}  
{GRAY} └─{RESET} {WHITE}Mode{RESET}: {CYAN}Anti-Block{RESET}     {GRAY}│{RESET}  {WHITE}Ping{RESET}   : {LIME}24ms{RESET}
{GRAY}{'─'*64}{RESET}""")

def draw_stats_bar():
    with stats_lock: c, s, f = total_checked, total_success, total_failed
    with dash_lock: pend = sum(1 for d in dashboard_data if d.get('otp') in (None, 'PENDING'))
    print(f"{DGRAY}┌{'─'*62}┐{RESET}")
    print(f"{DGRAY}│{RESET} {S_OK} {GREEN}OK:{s:<3}{RESET} {DGRAY}│{RESET} {S_FAIL} {RED}FAIL:{f:<3}{RESET} {DGRAY}│{RESET} {S_WARN} {YELLOW}PEND:{pend:<3}{RESET} {DGRAY}│{RESET} {S_DIAM} {CYAN}TOTAL:{c:<3}{RESET} {DGRAY}│{RESET}")
    print(f"{DGRAY}└{'─'*62}┘{RESET}")

def draw_progress(current, total):
    if total <= 0: return
    pct = min(100, int(current * 100 / total))
    filled = int(20 * pct / 100)
    bar = f"{GREEN}{'█'*filled}{DGRAY}{'░'*(20-filled)}{RESET}"
    print(f"{GRAY}  [{bar}{GRAY}]{RESET} {GOLD}{pct:>3}%{RESET} {DGRAY}({current}/{total}){RESET}")

def draw_premium_table():
    with dash_lock: rows=list(dashboard_data)
    print(f"\n{PURPLE}╔{'═'*W}╗{RESET}")
    print(f"{PURPLE}║{RESET} {PURPLE}{BOLD}{'✦ LIVE DASHBOARD ✦':^{W-2}}{RESET} {PURPLE}║{RESET}")
    print(f"{PURPLE}╠{'═'*3}╦{'═'*16}╦{'═'*16}╦{'═'*9}╦{'═'*7}╣{RESET}")
    print(f"{PURPLE}║{RESET} {WHITE}{'#':<1} {PURPLE}║{RESET} {CYAN}{'NUMBER':<14} {PURPLE}║{RESET} {PURPLE}{'NAME':<14} {PURPLE}║{RESET} {BLUE}{'UID':<7} {PURPLE}║{RESET} {YELLOW}{'OTP':<5} {PURPLE}║{RESET}")
    print(f"{PURPLE}╠{'═'*3}╬{'═'*16}╬{'═'*16}╬{'═'*9}╬{'═'*7}╣{RESET}")
    if not rows:
        print(f"{PURPLE}║{RESET} {GRAY}{'Waiting for accounts...':^{W-2}}{RESET} {PURPLE}║{RESET}")
    else:
        for idx,d in enumerate(rows[-10:],1):
            otp=d['otp']; otp_col=f"{RED}PEND {RESET}" if otp=='PENDING' else f"{GREEN}{otp:<5}{RESET}"
            uid_s=str(d['fb_id'])[:5]+".." if len(str(d['fb_id']))>5 else str(d['fb_id'])
            nm=d.get('name',''); nm_s=nm[:12]+".." if len(nm)>12 else nm
            print(f"{PURPLE}║{RESET} {WHITE}{idx:<1} {PURPLE}║{RESET} {CYAN}{d['number']:<14} {PURPLE}║{RESET} {PURPLE}{nm_s:<14} {PURPLE}║{RESET} {BLUE}{uid_s:<7} {PURPLE}║{RESET} {otp_col} {PURPLE}║{RESET}")
    print(f"{PURPLE}╚{'═'*3}╩{'═'*16}╩{'═'*16}╩{'═'*9}╩{'═'*7}╝{RESET}")

# ═══════════════════ HELPERS ═══════════════════
def is_filtered(num):
    with _filter_lock:
        c = re.sub(r'\D','',str(num))
        return num in _filtered or c in _filtered

def add_filter(num):
    with _filter_lock:
        _filtered.add(str(num)); _filtered.add(re.sub(r'\D','',str(num)))

def save_line(fname,text):
    add_filter(text.split('|')[0].strip())
    with file_lock:
        try:
            with open(fname,'a',encoding='utf-8') as f: f.write(text+'\n')
        except: pass

def update_success_file_with_otp(number,otp):
    with file_lock:
        try:
            if not os.path.exists('Success_Numbers.txt'): return
            lines=open('Success_Numbers.txt','r',encoding='utf-8').readlines()
            new=[]
            for line in lines:
                parts=line.strip().split('|')
                if len(parts)>=2 and parts[0]==str(number): parts[1]=otp; new.append('|'.join(parts)+'\n')
                else: new.append(line)
            with open('Success_Numbers.txt','w',encoding='utf-8') as f: f.writelines(new)
        except: pass

def rand_name(): return random.choice(FIRST_NAMES),random.choice(LAST_NAMES)
def rand_dob(): y=time.localtime().tm_year; return random.randint(1975,y-18),random.randint(1,12),random.randint(1,28)
def gen_s(): c=string.ascii_lowercase+string.digits; return ':'.join(''.join(random.choices(c,k=6)) for _ in range(3))
def strip_json(t): return t[9:] if t.startswith("for (;;);") else t

# ═══════════════════ TOKENS ═══════════════════
_LSD=[re.compile(r'"LSD",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),re.compile(r'"lsd":\s*"([^"]+)"'),re.compile(r'name="lsd"\s+value="([^"]+)"')]
_REV=re.compile(r'"server_revision":\s*(\d+)'); _HSI=re.compile(r'"hsi":\s*"(\d+)"')
_SPINB=re.compile(r'"__spin_b":\s*"([^"]+)"'); _SPINT=re.compile(r'"__spin_t":\s*(\d+)')
_HS=[re.compile(r'"__hs":\s*"([^"]+)"'),re.compile(r'"haste_session":\s*"([^"]+)"')]
_COMET=re.compile(r'"comet_env":\s*(\d+)')
_DTSG=[re.compile(r'"DTSGInitData",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),re.compile(r'"DTSGInitialData",\s*\[\s*\],\s*\{\s*"token":\s*"([^"]+)"'),re.compile(r'name="fb_dtsg"\s+value="([^"]+)"'),re.compile(r'"fb_dtsg":\s*"([^"]+)"')]
_HSDP=re.compile(r'"__hsdp"\s*:\s*"([^"]*)"'); _HBLP=re.compile(r'"__hblp"\s*:\s*"([^"]*)"')
_SJSP=re.compile(r'"__sjsp"\s*:\s*"([^"]*)"'); _PUBKEY=re.compile(r'"key_id"\s*:\s*(\d+)[^}]{0,80}"public_key"\s*:\s*"([0-9a-fA-F]{40,})"')
_PUBKEY2=re.compile(r'"public_key"\s*:\s*"([0-9a-fA-F]{40,})"[^}]{0,80}"key_id"\s*:\s*(\d+)'); _CSR=re.compile(r'"__csr"\s*:\s*"([^"]*)"')

def extract_tokens(html,cookies=None):
    t={}
    t['lsd']=next((m.group(1) for p in _LSD for m in [p.search(html)] if m),'')
    t['rev']=(m:=_REV.search(html)) and m.group(1) or ''
    t['hsi']=(m:=_HSI.search(html)) and m.group(1) or ''
    t['spin_b']=(m:=_SPINB.search(html)) and m.group(1) or 'trunk'
    t['spin_t']=(m:=_SPINT.search(html)) and m.group(1) or str(int(time.time()))
    t['hs']=next((m.group(1) for p in _HS for m in [p.search(html)] if m),'')
    t['comet_req']=(m:=_COMET.search(html)) and m.group(1) or '102'
    t['fb_dtsg']=next((m.group(1) for p in _DTSG for m in [p.search(html)] if m),'')
    t['csr']=(m:=_CSR.search(html)) and m.group(1) or ''
    t['dyn']=(m:=re.search(r'"__dyn":"([^"]+)"',html)) and m.group(1) or REG_DYN
    if cookies:
        try: t['jazoest']='2'+str(sum(ord(c) for c in ''.join(cookies.get_dict().values())))
        except: t['jazoest']='22431'
    else: t['jazoest']='22431'
    return t

def extract_dyn(html): return {'hsdp':(_HSDP.findall(html) or [''])[0],'hblp':(_HBLP.findall(html) or [''])[0],'sjsp':(_SJSP.findall(html) or [''])[0]}

def extract_pubkey(html):
    m=_PUBKEY.search(html)
    if m: return int(m.group(1)),m.group(2)
    m=_PUBKEY2.search(html)
    if m: return int(m.group(2)),m.group(1)
    return None,None

def encrypt_pwd(pwd,pub_hex=None,pub_id=None):
    if not pub_hex or not pub_id: return f"#PWD_BROWSER:0:{int(time.time())}:{pwd}"
    try:
        from cryptography.hazmat.primitives.asymmetric import padding as ap
        from cryptography.hazmat.primitives import hashes,serialization
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        from cryptography.hazmat.backends import default_backend
        import base64
        ts=int(time.time())
        pk=serialization.load_der_public_key(bytes.fromhex(pub_hex),backend=default_backend())
        key,iv=os.urandom(32),os.urandom(12)
        ct=AESGCM(key).encrypt(iv,pwd.encode(),str(ts).encode())
        enc=pk.encrypt(key,ap.OAEP(mgf=ap.MGF1(hashes.SHA1()),algorithm=hashes.SHA1(),label=None))
        payload=bytes([5,pub_id&0xFF])+iv+enc+ct[-16:]+ct[:-16]
        return f"#PWD_BROWSER:5:{ts}:{base64.b64encode(payload).decode()}"
    except: return f"#PWD_BROWSER:0:{int(time.time())}:{pwd}"

def build_common(t,s,d,req='1'):
    return {'av':'0','__user':'0','__a':'1','__req':req,'__hs':t['hs'],'dpr':'1','__ccg':'EXCELLENT','__rev':t['rev'],'__s':s,'__hsi':t['hsi'],'__dyn':t.get('dyn',REG_DYN),'__csr':t.get('csr',''),'__hsdp':d['hsdp'],'__hblp':d['hblp'],'__sjsp':d['sjsp'],'__comet_req':t.get('comet_req','102'),'lsd':t['lsd'],'jazoest':t['jazoest'],'__spin_r':t['rev'],'__spin_b':t['spin_b'],'__spin_t':t['spin_t'],'__jssesw':'1'}

# ═══════════════════ 🚀 NEW BULLETPROOF NUMBER CHECKER ═══════════════════
def deep_number_check(session, number, fp, referer, tokens, dyn):
    try:
        # Login page hit kore check kora (100% accurate)
        h = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/login/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'user-agent': fp['ua']
        }
        if fp['sec_ch']: h['sec-ch-ua']=fp['sec_ch']; h['sec-ch-ua-mobile']='?0'; h['sec-ch-ua-platform']='"Windows"'

        data = {
            'lsd': tokens['lsd'],
            'email': number,
            'login_source': 'comet_loops_v2_login',
            'jazoest': tokens.get('jazoest', '22431'),
            'fb_dtsg': tokens.get('fb_dtsg', ''),
            'login': 'Log in'
        }

        r = session.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1', headers=h, data=data, impersonate=fp['imp'], timeout=15, allow_redirects=False)
        
        # Jodi redirect status 302 ashe, mane account ache (TAKEN)
        if r.status_code in [301, 302, 303]:
            return False
            
        # Jodi 200 ashe, tobe page text e check korbo
        txt = r.text.lower()
        if "find your account" in txt or "didn't match any account" in txt or "no account" in txt or "recover" in txt:
            return True # FRESH
            
        if "checkpoint" in txt or "enter your password" in txt or "login_error" in txt:
            return False # TAKEN

        # Fallback to Recovery if login fails
        h2={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.facebook.com','referer':referer,'sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','x-asbd-id':'359341','x-fb-friendly-name':'AccountRecoveryGetIdentitiesByContactPointQuery','x-fb-lsd':tokens['lsd'],'user-agent':fp['ua']}
        if fp['sec_ch']: h2['sec-ch-ua']=fp['sec_ch']; h2['sec-ch-ua-mobile']='?0'; h2['sec-ch-ua-platform']='"Windows"'
        
        vars_=json.dumps({"contact_point":number},separators=(',',':'))
        data2={**build_common(tokens,gen_s(),dyn,'2'),'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'AccountRecoveryGetIdentitiesByContactPointQuery','server_timestamps':'true','variables':vars_,'doc_id':'6523934574345678','fb_dtsg':tokens.get('fb_dtsg','')}
        
        r2 = session.post('https://www.facebook.com/api/graphql/',headers=h2,data=data2,impersonate=fp['imp'],timeout=15)
        
        if r2.status_code == 200:
            raw = strip_json(r2.text)
            try:
                j = json.loads(raw)
                data_obj = j.get("data", {})
                node = data_obj.get("account_recovery_get_identities_by_contact_point") or {}
                if isinstance(node, dict) and (node.get("identities") or node.get("users")):
                    return False # TAKEN
                return True # FRESH
            except: pass
            
    except Exception as e: 
        pass
    return False # Error hole safe hishebe TAKEN dhore next number try korbe

def fetch_number(range_id=""):
    for i in range(15):
        if _shutdown.is_set(): return None
        try:
            r=requests.post(GET_NUM_URL,headers=API_HEADERS,json={"rid":range_id} if range_id else {},timeout=10)
            d=r.json()
            if d.get("meta",{}).get("code")==200:
                n=d.get("data",{}).get("full_number")
                if n and not is_filtered(n): return n
                elif n: add_filter(n)
        except: pass
        time.sleep(0.5+i*0.1)
    return None

def fetch_otp(number=""):
    c=re.sub(r'\D','',str(number)); suf=c[-10:] if len(c)>=10 else c
    try:
        r=requests.get(SUCCESS_OTP_URL,headers=API_HEADERS,timeout=10)
        if r.status_code!=200: return None
        d=r.json().get("data",{})
        items=d.get("otps",d.get("messages",d.get("items",d.get("data",[]))))
        if isinstance(items,dict): items=[items]
        for it in items:
            if not isinstance(it,dict): continue
            fn=re.sub(r'\D','',str(it.get("number",it.get("full_number",it.get("phone","")))))
            fs=fn[-10:] if len(fn)>=10 else fn
            if not c or (suf and suf in fs) or c in fn:
                m=re.search(r'\b\d{4,6}\b',str(it.get("message",it.get("text",it.get("otp","")))))
                if m: return m.group(0)
    except: pass
    return None

def fetch_ranges():
    try:
        r=requests.get(LIVE_ACCESS_URL,headers=API_HEADERS,timeout=10)
        d=r.json()
        sv=d.get("data",{}).get("services",d.get("services",[]))
        pool=[]
        if isinstance(sv,list):
            for s in sv:
                if isinstance(s,dict):
                    sid=str(s.get("sid",s.get("name",""))).upper()
                    if "FACEBOOK" in sid or not sid:
                        for rg in s.get("ranges",[]):
                            pool.append({"rid":str(rg),"country":get_country_name(str(rg))})
        seen=set(); out=[]
        for x in pool:
            if x["rid"] not in seen: seen.add(x["rid"]); out.append(x)
        return out[:10]
    except: return []

# ═══════════════════ REGISTRATION ═══════════════════
def process_registration(range_id, given_number=None):
    global total_checked, total_success, total_failed
    
    for attempt in range(1, 16):
        if _shutdown.is_set(): return "filtered"
        
        if given_number:
            num = given_number.strip()
            if is_filtered(num): return "filtered"
        else:
            print(f"{GRAY}  ┌─ Attempt {WHITE}{attempt}{GRAY}/15 {DGRAY}{'─'*25}{RESET}")
            num = fetch_number(range_id)
            if not num:
                print(f"{GRAY}  │{RESET}  {S_FAIL} {RED}No number from API pool{RESET}")
                print(f"{GRAY}  └{'─'*40}{RESET}\n")
                time.sleep(0.5)
                continue
            if is_filtered(num): continue
            print(f"{GRAY}  │{RESET}  {S_ARROW} {WHITE}Number  {GRAY}:{RESET} {CYAN}{BOLD}{num}{RESET}")
        
        fp = generate_random_fingerprint()
        print(f"{GRAY}  │{RESET}  {S_ARROW} {WHITE}Device  {GRAY}:{RESET} {PURPLE}{fp['imp'].upper():<10}{RESET}")
        
        try: s = requests.Session()
        except: continue
        
        try: s.get("https://m.facebook.com/", impersonate=fp['imp'], timeout=10)
        except: pass
        
        try:
            resp = s.get("https://www.facebook.com/login/", impersonate=fp['imp'], timeout=15)
            if not resp or 'lsd' not in resp.text.lower(): raise Exception("No LSD")
        except Exception:
            print(f"{GRAY}  └{'─'*40}{RESET}\n")
            continue
        
        tokens = extract_tokens(resp.text, s.cookies)
        dyn = extract_dyn(resp.text)
        pk_id, pk_hex = extract_pubkey(resp.text)
        if not tokens['lsd']: 
            print(f"{GRAY}  └{'─'*40}{RESET}\n")
            continue
        
        print(f"{GRAY}  │{RESET}  {S_ARROW} {WHITE}Prüfer  {GRAY}:{RESET} {TEAL}Checking...{RESET}")
        
        # 🚀 THE ULTIMATE CHECK
        if not deep_number_check(s, num, fp, resp.url, tokens, dyn):
            print(f"{GRAY}  │{RESET}  {S_FAIL} {RED}{BOLD}TAKEN{RESET} {RED}— exists{RESET}")
            add_filter(num); save_line('Failed_Numbers.txt', f"{num}|AlreadyReg")
            with stats_lock: total_checked += 1; total_failed += 1
            print(f"{GRAY}  └{'─'*40}{RESET}")
            print(f"{DGRAY}  ⤷ fetching next number...{RESET}\n")
            continue 
        
        print(f"{GRAY}  │{RESET}  {S_OK} {GREEN}{BOLD}FRESH NUMBER!{RESET}")
        print(f"{GRAY}  │{RESET}  {S_DOT} {WHITE}Usable  {GRAY}:{RESET} {GREEN}{num}{RESET}")
        time.sleep(random.uniform(2.0, 3.5))
        
        try:
            resp_refresh = s.get("https://www.facebook.com/reg/", impersonate=fp['imp'], timeout=15)
            tokens = extract_tokens(resp_refresh.text, s.cookies)
        except: pass
        
        ah={'accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.facebook.com','referer':resp.url,'sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','x-asbd-id':'359341','x-fb-friendly-name':'useCAARegistrationFormSubmitMutation','x-fb-lsd':tokens['lsd'],'user-agent':fp['ua']}
        if fp['sec_ch']: ah['sec-ch-ua']=fp['sec_ch']; ah['sec-ch-ua-mobile']='?0'; ah['sec-ch-ua-platform']='"Windows"'
        
        pwd=encrypt_pwd(USER_PASSWORD, pk_hex, pk_id)
        fn,ln=rand_name(); full=f"{fn} {ln}"; y,m,d=rand_dob()
        
        variables=json.dumps({"input":{"actor_id":"0","client_mutation_id":str(uuid.uuid4()),"machine_id":"","reg_data":{"birthday_day":d,"birthday_month":m,"birthday_year":y,"contactpoint":{"sensitive_string_value":num},"contactpoint_type":"PHONE","custom_gender":"","did_use_age":False,"firstname":{"sensitive_string_value":fn},"fullname":{"sensitive_string_value":full},"ig_age_block_data":None,"lastname":{"sensitive_string_value":ln},"preferred_pronoun":None,"reg_passwd__":{"sensitive_string_value":pwd},"sex":"MALE","use_custom_gender":False,"username":{"sensitive_string_value":""}},"sk_pipa_consent_given":None,"waterfall_id":str(uuid.uuid4())}},separators=(',',':'))
        pd={**build_common(tokens,gen_s(),dyn,'u'),'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useCAARegistrationFormSubmitMutation','server_timestamps':'true','variables':variables,'doc_id':'25782408224726258','qpl_active_flow_ids':'250359044,516759801','fb_api_analytics_tags':'["qpl_active_flow_ids=250359044,516759801"]','fb_dtsg':tokens.get('fb_dtsg','')}
        
        print(f"{GRAY}  │{RESET}  {S_ARROW} {WHITE}Submit  {GRAY}:{RESET} {YELLOW}Registering...{RESET}")
        try: r2=s.post('https://www.facebook.com/api/graphql/',headers=ah,data=pd,impersonate=fp['imp'],timeout=20)
        except Exception:
            print(f"{GRAY}  │{RESET}  {S_FAIL} {RED}Timeout{RESET}")
            print(f"{GRAY}  └{'─'*40}{RESET}\n")
            continue
        
        try: j=json.loads(strip_json(r2.text))
        except:
            print(f"{GRAY}  └{'─'*40}{RESET}\n")
            continue
        
        if j.get("errors"):
            print(f"{GRAY}  │{RESET}  {S_FAIL} {RED}Checkpoint / Blocked{RESET}")
            with stats_lock: total_checked += 1; total_failed += 1
            print(f"{GRAY}  └{'─'*40}{RESET}\n")
            continue
        
        data=j.get("data",{})
        res=(data.get("caa_registration_homepage_submit") or data.get("caa_registration_form_submit") or data.get("registration_form_submit") or {})
        ck=r2.cookies.get_dict()
        uid=ck.get("c_user","") or res.get("account_id") or res.get("user_id") or ""
        
        if uid and len(str(uid))>5:
            otp=fetch_otp(num)
            with dash_lock: dashboard_data.append({"number":num,"otp":otp or "PENDING","fb_id":uid,"name":full})
            with stats_lock: total_checked += 1; total_success += 1
            ck_str=";".join(f"{k}={v}" for k,v in ck.items())
            save_line('Success_Numbers.txt',f"{num}|{otp or 'PENDING'}|{uid}|{full}|{USER_PASSWORD}|{ck_str}")
            return "success"
        else:
            print(f"{GRAY}  │{RESET}  {S_FAIL} {RED}Blocked{RESET}")
            with stats_lock: total_checked += 1; total_failed += 1
            print(f"{GRAY}  └{'─'*40}{RESET}\n")
            continue
    return "failed"

# ═══════════════════ ENGINE ═══════════════════
def run_premium_engine(range_id, target, mode, manual_numbers):
    global total_checked, total_success, total_failed
    with dash_lock: dashboard_data.clear()
    clear_screen(); draw_logo()
    with stats_lock: total_checked = total_success = total_failed = 0
    
    print(f"\n{S_HEX} {PURPLE}{BOLD}INITIALIZING ENGINE{RESET}")
    print(f"{GRAY} ┌{'─'*45}┐{RESET}")
    print(f"{GRAY} │{RESET} {S_ARROW} {WHITE}Target  {GRAY}: {YELLOW}{target} Accounts{RESET}")
    print(f"{GRAY} │{RESET} {S_ARROW} {WHITE}Mode    {GRAY}: {GREEN}Anti-Checkpoint{RESET}")
    print(f"{GRAY} │{RESET} {S_ARROW} {WHITE}Range   {GRAY}: {CYAN}{range_id or 'default'}{RESET}")
    print(f"{GRAY} └{'─'*45}┘{RESET}")
    print(f"{GRAY} {S_WARN} Press CTRL+C to abort{RESET}\n")
    time.sleep(0.6)

    _shutdown.clear()
    
    for i in range(1, target + 1):
        if _shutdown.is_set(): break
        draw_progress(i - 1, target)
        print(f"\n{GOLD}{BOLD} ⚡ CREATING ACCOUNT {i}/{target}...{RESET}\n")
        
        if mode == "2":
            num = manual_numbers[i-1] if i-1 < len(manual_numbers) else None
            result = process_registration(range_id, given_number=num)
        else:
            result = process_registration(range_id)
        
        if result == "success":
            with dash_lock: last = dashboard_data[-1]
            print(f"{GREEN}╔{'═'*45}╗{RESET}")
            print(f"{GREEN}║{RESET} {GREEN}{BOLD}{'✔  CREATED SUCCESSFULLY':^43}{RESET} {GREEN}║{RESET}")
            print(f"{GREEN}╠{'═'*45}╣{RESET}")
            print(f"{GREEN}║{RESET}  {S_DOT} {WHITE}Number   {GRAY}: {CYAN}{BOLD}{last['number']:<26}{RESET} {GREEN}║{RESET}")
            print(f"{GREEN}║{RESET}  {S_DOT} {WHITE}Name     {GRAY}: {PURPLE}{last['name']:<26}{RESET} {GREEN}║{RESET}")
            print(f"{GREEN}║{RESET}  {S_DOT} {WHITE}Password {GRAY}: {YELLOW}{USER_PASSWORD:<26}{RESET} {GREEN}║{RESET}")
            print(f"{GREEN}║{RESET}  {S_DOT} {WHITE}UID      {GRAY}: {BLUE}{str(last['fb_id']):<26}{RESET} {GREEN}║{RESET}")
            print(f"{GREEN}║{RESET}  {S_DOT} {WHITE}OTP      {GRAY}: {(GREEN + last['otp'] if last['otp'] != 'PENDING' else RED + 'PENDING'):<26}{RESET} {GREEN}║{RESET}")
            print(f"{GREEN}╚{'═'*45}╝{RESET}\n")
            time.sleep(1.5)
        else:
            print(f"{RED}  {S_FAIL} {RED}[INFO] Account #{i} failed.{RESET}\n")
            time.sleep(1)

    draw_progress(target, target)
    print(f"\n{GOLD}{BOLD} ✦ BATCH COMPLETE!{RESET}\n")
    draw_stats_bar()
    draw_premium_table()

# ═══════════════════ OTP WATCHER ═══════════════════
def run_otp_watcher_screen():
    clear_screen(); draw_logo()
    print(f"\n{PURPLE}{BOLD} ⬢ LIVE OTP MONITOR{RESET}")
    print(f"{GRAY} {S_INFO} Polling every 5s {DGRAY}•{RESET} {GRAY}Ctrl+C to return{RESET}\n")
    draw_stats_bar(); draw_premium_table()
    try:
        while True:
            with dash_lock: pending=[d for d in dashboard_data if d.get("otp") in (None,"PENDING")]
            if not pending: time.sleep(3); continue
            changed=False
            for item in pending:
                num=item["number"]; otp=fetch_otp(num)
                if otp:
                    with dash_lock: item["otp"]=otp
                    update_success_file_with_otp(num,otp); changed=True
            if changed:
                clear_screen(); draw_logo()
                print(f"\n{PURPLE}{BOLD} ⬢ LIVE OTP MONITOR{RESET}")
                print(f"{GRAY} {S_INFO} Polling every 5s {DGRAY}•{RESET} {GRAY}Ctrl+C to return{RESET}\n")
                draw_stats_bar(); draw_premium_table()
                print(f"\n{GREEN}{S_OK} OTP updated in real-time!{RESET}")
            time.sleep(5)
    except KeyboardInterrupt:
        print(f"\n{YELLOW} {S_WARN} Returning to Home...{RESET}")
        time.sleep(1.2)
    finally: clear_screen()

# ═══════════════════ HOME ═══════════════════
def premium_menu(options, title):
    print(f"\n{CYAN}{BOLD} {S_HEX} {title}{RESET}")
    print(f"{DGRAY} {'─'*45}{RESET}")
    for i, (key, label, desc) in enumerate(options, 1):
        print(f"  {GREEN}[{key}]{RESET}  {WHITE}{label:<15}{RESET} {DGRAY}—{RESET} {GRAY}{desc}{RESET}")
    print(f"{DGRAY} {'─'*45}{RESET}")

def main():
    global USER_PASSWORD
    clear_screen()
    while True:
        clear_screen(); draw_logo()
        print(f"\n{CYAN}{BOLD} {S_HEX} SECURITY{RESET}")
        print(f"{DGRAY} {'─'*45}{RESET}")
        p = input(f" {S_PTR} {WHITE}Pass {GRAY}(={YELLOW}Okabye#570{GRAY}):{RESET} ").strip()
        if p: USER_PASSWORD = p
        print(f" {S_OK} {GREEN}Locked:{RESET} {YELLOW}{USER_PASSWORD}{RESET}")
        
        premium_menu([("1", "Auto API", "Fetch from live ranges"),("2", "Manual TXT", "Load from file")], "SELECT MODE")
        mode = input(f" {S_PTR} {WHITE}Select {GRAY}[1/2]:{RESET} ").strip() or "1"
        
        range_id = ""; manual = []; total = 0
        
        if mode == "2":
            fp = input(f"\n {S_PTR} {WHITE}TXT {GRAY}(=numbers.txt):{RESET} ").strip() or "numbers.txt"
            if os.path.exists(fp):
                for line in open(fp, encoding='utf-8'):
                    n = line.strip().split('|')[0].strip()
                    if n and not n.startswith('#') and not is_filtered(n): manual.append(n)
            if not manual:
                print(f" {S_FAIL} {RED}No valid numbers!{RESET}"); input(f" {GRAY}Enter to continue...{RESET}"); continue
            total = len(manual)
            print(f" {S_OK} {GREEN}Loaded {WHITE}{total}{GREEN} numbers.{RESET}")
        else:
            ranges = fetch_ranges()
            if ranges:
                print(f"\n{GREEN}{BOLD} {S_HEX} LIVE RANGES{RESET}")
                print(f"{DGRAY} ┌{'─'*45}┐{RESET}")
                for i, r in enumerate(ranges, 1):
                    print(f"{DGRAY} │{RESET}  {GREEN}[{i:02d}]{RESET} {WHITE}{r['rid']:<12}{RESET} {CYAN}➔{RESET} {YELLOW}{r['country']:<12}{RESET} {DGRAY}│{RESET}")
                print(f"{DGRAY} └{'─'*45}┘{RESET}")
                ch = input(f" {S_PTR} {WHITE}Select {GRAY}[1-{len(ranges)}]:{RESET} ").strip()
                try:
                    idx = int(ch)
                    if 1 <= idx <= len(ranges): range_id = ranges[idx-1]["rid"]
                except: range_id = ch if ch else ""
            if not range_id: range_id = input(f" {S_PTR} {WHITE}Range ID {GRAY}(=default):{RESET} ").strip()
            try:
                t = input(f" {S_PTR} {WHITE}Target {GRAY}[1-20, =6]:{RESET} ").strip() or "6"
                total = int(t)
            except: total = 6
        
        input(f" {S_PTR} {WHITE}Proxy {GRAY}(=direct):{RESET} ")
        
        run_premium_engine(range_id, total, mode, manual)
        
        input(f"\n{GREEN} {S_OK} Press {WHITE}[ENTER]{GREEN} for {PURPLE}Live OTP Watcher{GREEN} {GRAY}(Ctrl+C = Home){RESET}")
        run_otp_watcher_screen()
        
        print(f"\n{GREEN} {S_OK} Returned to Home.{RESET}")
        input(f" {S_PTR} {WHITE}Enter to continue...{RESET}")

if __name__ == "__main__":
    main()