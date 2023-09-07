import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1,6))  # Corrected randomint to randint

    if p_message == '!help':
        return "`This is a help message you can modify to your server's needs!`"

    return "Sorry, I didn't understand that."  # Added a default response
