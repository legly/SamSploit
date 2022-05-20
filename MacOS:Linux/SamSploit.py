# Copyright by Samraj
# Created by Samraj
# Github: https://www.github.com/SamOBoy97
# Website 1: Learn coding for free here http://samfw.visuinvoice.com
# Website 2: Free security apps like VIRUS SCANNER, VPN etc     https://cyberfreeworld.w3spaces.com
# Website 3: In this website i offer free Ethical hacking and penetration testing tools etc. https://samsploit.w3spaces.com
# Youtube: https://www.youtube.com/channel/UCS3BS8kYX_Ueg4qudMqmz-g


# PAKAGES
from tkinter import *
from tkmacosx import Button
import turtle
import subprocess
import requests
import hashlib
import socket
import time
import os
from rich.console import Console
console = Console()

# This will exit the applicaiton
def Exit():
	exit()

# Nmap port scanner
def NmapScanner():
	wn = turtle.getscreen()
	turtle.title("NMAP PORT SCANNER")
	turtle.write("NMAP PORT SCANNER",font=('arial',50,'bold'),align='center')
	ip = turtle.textinput("NMAP SCANNER","ENTER VICTIMS IP")
	turtle.clear()
	ssh = socket.socket()
	ftp = socket.socket()
	telnet = socket.socket()
	http = socket.socket()
	https = socket.socket()
	port24 = socket.socket()
	port25 = socket.socket()
	os.system("say Please Wait this might take a while")
	try:
		ssh.connect((ip,22))
		turtle.write("PORT 22 IS OPEN")
	except:
		pass

	try:
		ftp.connect((ip,21))
		turtle.write("PORT 21 IS OPEN")
	except:
		pass

	try:
		telnet.connect((ip,23))
		turtle.write("PORT 23 IS OPEN")
	except:
		pass

	try:
		http.connect((ip,80))
		turtle.write("PORT 80 IS OPEN")
	except:
		pass

	try:
		https.connect((ip,443))
		turtle.write("PORT 443 IS OPEN")
	except:
		pass

	try:
		port24.connect((ip,24))
		turtle.write("PORT NUMBER 24 IS OPEN")
	except:
		pass

	try:
		port25.connect((ip,25))
		turtle.write("PORT NUMBER 25 IS OPEN")
	except:
		pass

	turtle.clear()
	turtle.done()

# Gets the HTML code of any website
def WebScraper():
	while True:
		wn = turtle.getscreen()
		turtle.title("WEB SCRAPER")
		turtle.write("WEB SCRAPER",font=('arial',50,'bold'),align='center')
		URL_HOST = turtle.textinput("URL","ENTER URL OF THE WEBSITE")
		DIRECTORY = turtle.textinput("DIRECTORY","Enter the directory where you want to save the file")
		turtle.clear()
		try:
			os.chdir(DIRECTORY)
		except:
			continue
		try:
			HTML = requests.get(URL_HOST)
			html_file = open('index.html','w')
			html_file.write(HTML.text)
			turtle.write("FILE SAVED AT " + DIRECTORY,align='center',font=('arial',20,'bold italic'))
			break
		except:
			turtle.write("AN ERROR OCCOURED WHILE FETCHING THE CODE",font=('normal',40,'bold'))
			continue 
			turtle.done()

# Scans for vulnerability on Computers no matter what OS
def PcScanner():
	while True:
		wn = turtle.getscreen()
		turtle.title("System VULNEARABILITY Scanner")
		turtle.write("System VULNEARABILITY Scanner",font=('arial',30,'bold italic'),align='center')
		HOST = turtle.textinput("HOST","ENTER THE IP OF THE HOST")
		turtle.clear()
		ftp = socket.socket()
		ssh = socket.socket()
		telnet = socket.socket()
		try:
			ftp.connect((HOST,21))
			turtle.write("PORT NUMBER 21 IS OPEN",font=('arial',30,'bold'),align='center')
		except:
			pass

		try:
			ssh.connect((HOST,22))
			turtle.write("PORT NUMBER 22 IS OPEN",font=('arial',30,'bold'),align='center')
		except:
			pass
		try:
			telnet.connect((HOST,23))
			turtle.write("PORT NUMBER 23 IS OPEN",font=('arial',30,'bold'),align='center')
		except:
			pass
		subprocess.run("traceroute " + HOST + " >> traceroute_results",shell=True)
		traceroute_results = open('traceroute_results','r')
		output = traceroute_results.read()
		turtle.write(output,font=('arial',20,'bold'),align='center')
		traceroute_results.close()
		turtle.done()

# Website Vulnerality Scanner
def WebVulnerabilityScanner():
	window = turtle.getscreen()
	turtle.title("WEBSITE VULNEARABILITY SCANNER")
	turtle.write("WEBSITE VULNEARABILITY SCANNER",font=('arial',30,'bold italic'),align='center')
	HOST = turtle.textinput("URL",'ENTER WEBSITE URL for ex www.google.com')
	ip = turtle.textinput("IP",'ENTER WEBSITE IP ADDRESS')
	turtle.clear()
	subprocess.run('nslookup ' + HOST + " >> output",shell=True)
	subprocess.run("nmap -O " + ip + " >> nmap_results",shell=True)
	wn = Tk()
	scan_results = open('output','r')
	wn.title("SCAN OUTPUT")
	wn.geometry("1000x700")
	results=scan_results.read()
	Label(wn, text=results).pack()
	http = socket.socket()
	https = socket.socket()
	ftp = socket.socket()
	Label(wn, text="VULNEARABILITY SCAN STARTED PLEASE WAIT THIS MIGHT TAKE A WHILE").pack()
	try:
		http.connect((ip,80))
		Label(wn,text="PORT NUMBER 80 IS OPEN").pack()
	except:
		pass

	try:
		https.connect((ip,443))
		Label(wn, text="PORT NUMBER 443 IS OPEN").pack()
	except:
		pass

	try:
		ftp.connect((ip,21))
		Label(wn, text="PORT NUMBER 21 IS OPEN").pack()
	except:
		pass

	Label(wn,text="STARTING NMAP SCAN").pack()
	nmap_results = open('nmap_results','r')
	nmap_scan_result = nmap_results.read()
	Label(wn, text=nmap_scan_result).pack()
	wn.mainloop()
	turtle.done()

# This page is for the custom wordlist users

def custom_md5():
	window = turtle.getscreen()
	turtle.title("MD5 CUSTOM WORDLIST")
	turtle.write("ENTER THE PATH OF THE LOCATION OF THE FILE")
	wordlist_directory = turtle.textinput("LOCATION",'ENTER THE LOCATION OF THE WORDLIST')
	try:
		os.chdir(wordlist_directory)
	except:
		turtle.clear()
		turtle.write("ERROR OCCOURED",font=('arial',30,'bold'))
	wordlistname = turtle.textinput("WORDLIST","Enter worldlist name")
	md5_hash = turtle.textinput("MD5",'ENTER MD5 HASH')
	try:
		pass_lst = open(wordlistname,'r')
	except:
		turtle.clear()
		turtle.write("FILE NOT EXISTED!",font=('arial',30,'bold'))
	
	for password in pass_lst:
		encrypt = password.encode('utf-8')
		output = hashlib.md5(encrypt.strip()).hexdigest()
		if md5_hash == output:
			turtle.clear()
			turtle.write("PASSWORD IS: " + password,font=('normal',30,'bold'),align='center')
			break
		else:
			pass 


# Password Cracker MAIN page
def Password_Cracker():
	window = Tk()
	window.title("PASSWORD CRACKER")
	window.configure(background='black')
	window.geometry("800x800")
	Label(window, text="SELECT HASH TYPE", font=('normal',60,'bold italic'),bg='black',pady=40).pack(anchor='n')
	Button(window, text="MD5",padx=30,pady=20,bg='green',fg='white',command=custom_md5).pack(anchor='w')
	window.mainloop()


# Application Home page
window = Tk()
window.title("HACKING APP")
window.geometry("1000x700")
window.configure(background="black")
Label(window, text="HACKING APP",fg='green',bg='black',font=('arial',60,'bold italic'),pady=50).pack()
Button(window, text="NMAP SCAN",fg="white",bg="green",activebackground="red",padx=70,pady=20,command=NmapScanner).pack(anchor="center")
Button(window, text="PC VULNEARABILITY SCANNER",fg="white",bg="green",activebackground="red",padx=30,pady=20, command=PcScanner, cursor='arrow').pack(anchor="center")
Button(window, text="WEB VULNEARABILITY SCANNER",fg="white",bg="green",activebackground="red",padx=30,pady=20, command=WebVulnerabilityScanner).pack(anchor="center")
Button(window, text="WEB SCRAPER",fg="white",bg="green",activebackground="red",padx=30,pady=20,command=WebScraper).pack(anchor="center")
Button(window, text="PASSWORD CRACKER",fg="white",bg="green",activebackground="red",padx=30,pady=20,command=Password_Cracker).pack(anchor="center")
Button(window, text="EXIT",fg="white",bg="green",activebackground="red",padx=30,pady=20,command=Exit).pack(anchor="center")
window.mainloop()