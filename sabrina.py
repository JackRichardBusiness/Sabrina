from firebase import firebase
while True:
	database = firebase.FirebaseApplication('https://sabrina-415a1.firebaseio.com/')
	inputstr = input('>>> ')
	output = database.get('conversation/', inputstr)
	if output == None:
		print("Sorry, I didn't get that.")
		database.put('unknown/', inputstr, '?')
	else:
		print(output)
