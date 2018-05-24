import time
import requests
from colorama import init, Fore, Back, Style
import random
import string 

init()

def main():
	print(Fore.RED + "---------------------------------------------------\n")
	print(Fore.CYAN + "::               NIKE ACCOUNT GEN                ::")
	print(Fore.CYAN + "::               IF U KNOW U KNOW                ::")
	print(Fore.RED + "\n---------------------------------------------------")
	time.sleep(2)
	print(Fore.YELLOW + "Getting nike.com...")
	time.sleep(1)
	print(Fore.YELLOW + "Entering Random Account info...")
	time.sleep(2)
	print(Fore.CYAN + "{}@fuckass.com:{}".format(random.randint(111,999999999), ''.join(random.choice(string.ascii_letters) for x in range(9))))
	time.sleep(3)
	print(Fore.YELLOW + "Submitting Account Data and making account....")
	time.sleep(2)
	print("Wait, have to generate sensor data, fuck")
	time.sleep(2)
	count = 0
	sens = []
	while count < 100:
		data = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(2))
		sens.append(data)
		count +=1
	print(sens)
	print(Fore.YELLOW + "Got Sensor Data. Making Account...")
	time.sleep(2)
	print(Fore.GREEN +"Made that fucking account, now to verify this fucker, im using CN because im a cheap fuck and I like making money")
	time.sleep(2)
	pnum = "+86" + str(random.randint(11111111111,99999999999))
	print(Fore.GREEN +"Got the fucking number: {}".format(pnum))
	time.sleep(2)
	print(Fore.YELLOW +"Verifying account...")
	time.sleep(3)
	print(Fore.CYAN + "The fucking account is VERIFIED BITCH.")
	time.sleep(3)
	print(Fore.RED + "TIME TO SELL FOR $0.50/EA TO SOME STUPID FUCKER ON TWIITER FOR TRAVIS SCOOT AND VIRGIL BLOWASS DROPS")
	time.sleep(3)
	print(Fore.RED + "DM FOR BUlK PRICing")
	time.sleep(10)

if __name__ == '__main__':
	main()