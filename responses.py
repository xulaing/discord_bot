import random


def handle_response(message, user_id) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Coucou !'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    
    if p_message == 'qui a raison ?' or p_message=='qui est la plus belle ?':
        cici = '<@588096973446316038>'
        return 'c\'est %s.' % cici

    if p_message == 'qui je suis ?':
        if int(user_id) == 588096973446316038 :
            print('passed')
            return 'La petite princesse de matmat trop belle qui pipoupi la vie'
        elif int(user_id) == 184405311681986560 :
            return 'Matimatou, le petit cochonou que cici aime troooooop !!'
    
    if p_message == 'send bobi':
        index = random.randint(1, 6)
        return "file=discord.File('./bobi/bobi_%d.jpg')" % index
