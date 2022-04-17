import subprocess
import socket
import os 
try:
	import requests
except:
	os.system("pip install requests")
	os.system("pip3 install requests")

# Modules for Windows

def WindowsPacketSender():
	host = input("Enter ip: ")
	subprocess.call("ping " + host,shell=True)


# Modules for MacOS

def PacketSender(duration,ip):
	try:
		subprocess.call('ping -t ' + duration + " " + ip,shell=True)
	except:
		print("An error occoured")


def Mac_Changer(new_mac):
	try:
		subprocess.call('ifconfig en0 ether ' + new_mac ,shell=True)
	except:
		print("An error occoured")


# Modules for Linux

def LinuxIPChanger():
	ip_ip_ip = input("Enter new ip: ")
	subprocess.call("ifconfig eth0 down",shell=True)
	subprocess.call("ifconfig inet " + ip_ip_ip,shell=True)
	subprocess.call("ifconfig eth0 up",shell=True)

def Mac_Changer(new_mac):
	try:
		subprocess.call('ifconfig en0 ether ' + new_mac ,shell=True)
	except:
		print("An error occoured")



# Modules for all OS

def VulnScannerCOMPUTER():
	ip3 = input("Enter ip: ")
	print("Starting nmap scan")
	print("=========================================================================")
	subprocess.call("nmap -O " + ip3,shell=True)
	print("=========================================================================")
	print("VULNERABILITIES")
	ssh97 = socket.socket()
	ftp97 = socket.socket()
	telnet = socket.socket()
	try:
		ssh97.connect((ip3,22))
		print('SSH IS OPEN')
	except:
		pass

	try:
		ftp97.connect((ip3,21))
		print("FTP IS OPEN")
	except:
		pass 

	try:
		telnet.connect((ip3,24))
		print("TELNET IS OPEN")
	except:
		pass
	print("=========================================================================")
	print("HOST CHECK")
	os.system('ping -t 5 ' + ip3)
	print("=========================================================================")
	print("TRACING ROUTE TO " + ip3)
	print("=========================================================================")
	os.system("traceroute -m 3 " + ip3)
	print("=========================================================================")


def DmitryPortScanner():
	host = input("Enter ip: ")
	subprocess.call("dmitry " + host,shell=True)


def NmapPortScanner():
	ip1 = input("Enter ip: ")
	subprocess.call("nmap -O " + ip1,shell=True)





