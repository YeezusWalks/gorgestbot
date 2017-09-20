import discord
import asyncio
from random import randint


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #if message.author.name == "niorai_nio":
    #	a = randint(0,4)
    #	if a==0:
    #		msg ="GPU leja jezit"
    #	elif a==1:
    #		msg = "GPU te du shume"
    #	elif a==2:
    #		msg = "GPU je shume kare"
    #	elif a==3:
    #		msg = "GPU a je tu ardh daddy"
    #	else:
    #		msg = "a i re sot me redo GPU?"
    #	await client.send_message(message.channel, msg)*/

    if message.content.startswith('!dhori'):
        msg = 'Ta qi zotin tat {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!metal'):
    	msg = 'Metali eshte VK!!! {0.author.mention}'.format(message)
    	await client.send_message(message.channel, msg)

    elif message.content.startswith('!pidh'):
    	msg = 'Ta hongsha lafshen {0.author.mention} \n Hajd te te qi iher fort ti dredh shalet o zhbirdi'.format(message)
    	await client.send_message(message.channel, msg)

    elif message.content.startswith('!rrock'):
    	msg = 'A don me ta thy karin o rrushi {0.author.mention}'.format(message)
    	await client.send_message(message.channel, msg)

    elif message.content.startswith('@help'):
    	msg = 'Komandat per botin {0.author.mention} :\n!dhori\n!metal\n!pidh\n!rrock\n!dele\n!rrak'.format(message)
    	await client.send_message(message.channel, msg)

    elif message.content.startswith('!dele'):
    	msg = "dy dele\ndy dele e treqind pare\nqo moj nuse\nqo moj nuse te hedhim valle".format(message);
    	await client.send_message(message.channel, msg, tts=True);

    elif message.content.startswith('!rrak'):
    	msg = "rrak tak zemra mboni";
    	await client.send_message(message.channel, msg, tts=True);

    else:
    	return


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message_delete(message):
	msg = "Mesazhi {0.content} nga {0.author.mention} u fshi".format(message)
	await client.send_message(message.channel, msg)


@client.event
async def on_reaction_add(reaction, user):
	if reaction.emoji.name=="gej":
		if reaction.count<=1:
			msg="Fillun kurvat me gay emotes"
			await client.send_message(reaction.message.channel,msg)
	

client.run(emaili, pasuordi)