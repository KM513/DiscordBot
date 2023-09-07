import random

def handle_response(message) -> str;
p_message = message.lower();

if p_message == 'hello':
return 'Hey there!'

if p_message == 'roll':
return str(random.randomint(1,6))

if p_message == '!help':
    return "`This is a help message you can modify to your servers needs!`"