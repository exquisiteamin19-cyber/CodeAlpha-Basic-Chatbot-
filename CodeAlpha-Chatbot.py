def bot_response(user_response) :
	user_response = user_response.lower()
	
	if 'hello' in user_response :
		return 'Hi'
		
	elif 'how are you' in user_response :
		return 'Fit as a fiddle! Your side'
	
	elif "cool" in user_response :
		return 'Good to hear that! How may I help you?'
		
	elif 'tell me about yourself' in user_response :
		return 'I am a simple python chatbot'
		
	elif 'bye' in user_response :
		return 'Goodbye comrade'
		
	else :
		return "I have no idea"
		
print('Welcome comrade!')
print('Type something or type bye to exit')

while True :
	user_response = input('You : ')
	
	response = bot_response(user_response)
	
	print('Chatbot : ', response)
	
	if 'bye' in user_response.lower() :
		break