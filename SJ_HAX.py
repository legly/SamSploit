import subprocess
import socket
import os
try:
	import requests
except:
	os.system("pip3 install requests")
	os.system("pip install requests")

def Mac_Changer(new_mac):
	try:
		subprocess.call('ifconfig en0 ether ' + new_mac ,shell=True)
	except:
		print("An error occoured")



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


print("(1) PacketSender")
print("(2) Port Scanner")
print("(3) Nmap port scanner")
print("(4) Dmitry port scanner")
print("(5) Windows Vulnerability Scanner")
print("(6) MacOS Vulnerability Scanner")
print("(7) Website Vulnerability Scanner")
print("(8) Mac Changer for Mac/Linux")
print("(9) Ip Changer for Mac/Linux")
print("(10 EXIT")

while True:
	valid_numbers = ["1","2","3","4","5","6","7","8","9","10"]
	main = input(">>> ")
	if main in valid_numbers:
		print("")
		if main == "1":
			ip_addr = input("Enter ip: ")
			dur = input("Enter duration: ")
			subprocess.call("ping -t " + dur + " " + ip_addr,shell=True)
		if main == "2":
			ip_address = input("Enter ip: ")
			port_number = input("Enter port number: ")
			port = int(port_number)
			prt_scan = socket.socket()
			try:
				prt_scan.connect(ip_address,port)
				print("PORT IS OPEN")
			except:
				print("PORT IS CLOSED")

		if main == "3":
			ip1 = input("Enter ip: ")
			subprocess.call("nmap -O " + ip1,shell=True)
		if main == "4":
			ip2 = input("Enter ip: ")
			subprocess.call("dmitry " + ip2,shell=True)
		if main == "5":
			VulnScannerCOMPUTER()
		if main == "6":
			VulnScannerCOMPUTER()
		if main == "7":
			VulnScannerCOMPUTER()

		if main == "8":
			Mac_Changer()

		if main == "9":
			ip_ip_ip = input("Enter new ip: ")
			subprocess.call("ifconfig eth0 down",shell=True)
			subprocess.call("ifconfig inet " + ip_ip_ip,shell=True)
			subprocess.call("ifconfig eth0 up",shell=True)

		if main == "10":
			exit()
	else:
		print("Invalid Number")




