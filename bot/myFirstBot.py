#catch and log reactions

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
   #a = discord.utils.get(client.get_all_members(),name="Test-User", discriminator="9635").id  #GetUserID
    print('Bot is ready.')


"""  crawl message
@client.event
async def on_message(message):
    if str(message.author) == 'Test-user#111':
         print(f'{message.content} RECEIVED!.')
    else:
        print(f'{message.content} wrong User!.')
"""

#get reaction an log it on another channel crawl message with some condition as an example
@client.event
async def on_reaction_add(reaction, user):
    channel = client.get_channel(6637461198)
    print(f'{reaction}')
    if str(reaction.message.author.id) == '579155970803':
        if str(user.id) != '57915597803':
            await channel.send('[{0.display_name}] -  {0} has reacted with {1.emoji}!; ID = {1.message.id} '.format(user, reaction))
client.run(' some API-DiscordServer String here ')
