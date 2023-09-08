import random

def handle_response(message) -> str:
    p_message = message.lower().strip()  
    if p_message == 'hello':
        return 'Hey there!'
    elif p_message == 'roll':
        return str(random.randint(1,6))
    elif p_message == '!help':
        return "`This is a help message you can modify to your server's needs!`"
    else:
        return "Sorry, I didn't understand that."
