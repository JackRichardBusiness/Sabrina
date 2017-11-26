from firebase import firebase
import os
database = firebase.FirebaseApplication('https://sabrina-415a1.firebaseio.com/')
version = int(database.get('houseOS/', 'version'))
currentVersion = open('houseOSver.txt', 'r+')
if not int(currentVersion.read()) == version:
	print('Updating from '+currentVersion+' to '+version+'...')
	os.system('sudo git clone https://www.github.com/JackRichardBusiness/Sabrina')
	os.system('python3 Sabrina/sabrina.py')
while True:
	inputstr = input('>>> ')
	output = database.get('conversation/', inputstr)
	if output == None:
		print("Sorry, I didn't get that.")
		database.put('unknown/', inputstr, '?')
	else:
		print(output)
