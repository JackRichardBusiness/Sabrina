from firebase import firebase
while True:
	inputstr = input('>>> ')
	output = database.get('conversation/', inputstr)
	if output == None:
		print("Sorry, I didn't get that.")
		database.put('unknown/', inputstr, '?')
	else:
		print(output)
