import discord
import responses
import random

# Send messages
async def send_message(user_id, message, user_message, is_private):
    try:
        p_message = user_message.lower()
        if p_message == 'hello':
            response = 'Coucou !'

        elif p_message == 'roll':
            response = str(random.randint(1, 6))

        elif p_message == '!help':
            response = "`This is a help message that you can modify.`"
    
        elif p_message == 'qui a raison ?' or p_message=='qui est la plus belle ?':
            cici = '<@588096973446316038>'
            response = 'c\'est %s.' % cici

        elif p_message == 'qui je suis ?':
            if int(user_id) == 588096973446316038 :
                response = 'La petite princesse de matmat trop belle qui pipoupi la vie'
            elif int(user_id) == 184405311681986560 :
                response = 'Matimatou, le petit cochonou que cici aime troooooop !!'
    
        elif p_message == 'send bobi':
            index = random.randint(1, 6)
            bark = ["bawrf", "bwirf", 'gnrrr', "bouf"]
            bark_index = random.randint(0, 3)
            await message.author.send(file=discord.File('./bobi/bobi_%d.jpg' % index)) if is_private else await message.channel.send(file=discord.File('./bobi/bobi_%d.jpg' % index))
            response = bark[bark_index]

        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA0MjM4MzA2MDQyMDgwMDU2Mg.GywUgF.1qno6P0_sUUJJOLCEQskrsfJeVTzYoy5xILzEo'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_id = str(message.author.id)
        user_message = str(message.content)
        channel = str(message.channel)

        members = client.guilds[0].members

        member_ids = [member.id for member in members if not member.bot]

        print(member_ids)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(user_id, message, user_message, is_private=True)
        else:
            await send_message(user_id, message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
