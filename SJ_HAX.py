# These scripts are for LEAGAL purposes only. If you get into any trouble i am not responsible
# Our Website: https://samsploit.w3spaces.com
# GitHub: https://www.github.com/SamOBoy97
import socket
import requests
import subprocess
try:
	import OperatingSys
	from OperatingSys import WindowsPacketSender
	from OperatingSys import VulnScannerCOMPUTER
	from OperatingSys import NmapPortScanner
	from OperatingSys import Mac_Changer
except:
	print("FILES MISSING!")
	exit()
import subprocess
try:
        import scapy.all as scapy
except:
        subprocess.call("pip install scapy")
# MODULES



def Web_HTML_Extracter():
	URL = input("Enter url: ")
	html = requests.get(URL)
	print(html.text)

print("(1) Windows/packet_sender")
print("(2) MacOS/Linux packet sender")
print("(3) Windows/Vulnerability_scanner")
print("(4) MacOS/Vulnerability_scanner")
print("(5) Linux/Vulnerability_scanner")
print("(6) Nmap port scanner")
print("(7) Port Scanner")
print("(8) Website Vulnerability Scanner")
print("(9) Website/HTML_EXTRACTER")
print("(0) EXIT")
while True:
	main = input(">>> ")
	if main == '1':
		WindowsPacketSender()
	if main == '2':
		host_ip = str(input("Enter ip: "))
		duration = str(input("Enter seconds: "))
		subprocess.call("ping -t " + duration + " " + host_ip,shell=True)
	if main == '3':
		VulnScannerCOMPUTER()
	if main == '4':
		VulnScannerCOMPUTER()
	if main == '5':
		VulnScannerCOMPUTER()
	if main == '6':
		OperatingSys.NmapPortScanner()
	if main == '7':
		# PORT SCANNER
		ip_address123 = input("Enter ip: ")
		scanner = socket.socket()
		port = input("Enter port number: ")
		port_number = int(port)
		try:
			scanner.connect((ip_address123,port_number))
			print("PORT IS OPEN")
		except:
			print("PORT IS CLOSED")
	if main == '8':
		IP = input("Enter ip: ")
		print("For example: https://samsploit.w3spaces.com")
		URL = input("Enter URL: ")
		subprocess.call("nmap -O " + IP,shell=True)
		try:
			subprocess.call("ping " + IP,shell=True)
		except:
			pass
		subprocess.call("nslookup " + URL,shell=True)
		subprocess.call("traceroute -m 3 " + IP,shell=True)
		subprocess.call("tracert " + IP,shell=True)
	if main == '9':
		Web_HTML_Extracter()
	if main == '0':
		exit()



















































