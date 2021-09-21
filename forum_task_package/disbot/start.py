# TODO: and me
import discord

client = discord.Client()


@client.event
async def on_mess(message):
    if message.autor == client.user:
        return
    if message.content.startswith('!hello'):
        mag = 'Hello(0.author.mention)'.format(message)
        await client.send_message(message.channal, msg)


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('NDc1OTQ1NzQzNzQ4OTU2MTYw.DkmpAw.pPX7DiNqJMKGyzUD611rQ5Ws0eE')
