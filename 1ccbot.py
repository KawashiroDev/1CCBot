#1ccbot created by KawashiroDev
#based on TB 2.0.9

##Parameters##

#Version
bot_version = '1.6.8'

#owner id
ownerid = 166189271244472320

#debug switch
debugmode = False

#Spicetools URL
spiceURL = "http://onlyone.cab/downloads/spicetools-latest.zip"

#Spicetools URL
spiceURL2 = "https://spice2x.github.io/"

#Bemanitools URL
btoolURL = "http://tools.bemaniso.ws/"

#segatools URL
stoolURL = "http://example.com"

#asphyxia URL
asphURL = "http://example.com"

#April fools mode
aprilfools=False

#Account age options for links application
#How many days old the account needs to be 
dayspassed = 5

#How many days since Tenshi was added to the server
tenkojoin = 7

#How many days since user joined the server
userjoin = 30

import discord
import requests
import aiohttp
import random
import asyncio
import os
import subprocess
import time
import zipfile
import shutil
import hashlib
import setproctitle
import lxml
import base64

from discord.ext import commands
from random import randint
from datetime import datetime, timedelta, date
from zipfile import ZipFile
from urlextract import URLExtract
from profanityfilter import ProfanityFilter
from bs4 import BeautifulSoup

#Gelbooru API keys
gbooru_api = open("Tokens/gelbooru_api.txt", "r")
g_api = gbooru_api.read()
gbooru_user = open("Tokens/gelbooru_userid.txt", "r")
g_user = gbooru_user.read()

Roles = [
"Ꮐrееn",     
"ӏight Ꮐrееn",    
"‌ԁаrk Ꮐrееn",
"Ꮲυrplе",
"ⅿɑɡentɑ",
"р﻿е﻿n﻿ѕ﻿і﻿ ʙluе",
"ріnk",
"ⅽγαɴ",
"g﻿о﻿l﻿d",
"у﻿е﻿l﻿l﻿о﻿w",
"Օrä﻿n﻿ɡ﻿е",
"r﻿е﻿d",
]

Roles_special = [
"pale green",     
"sky blue",    
"neon pink",
"peach",
"silver",
]

spicetools_response = [
"Funny human",     
"Am i a joke to you?",    
"Bruh",
"Can someone kick the wannabe 1CCBot?",
"Shush",
"You do not spark joy",
"Who is this guy?",
"Silence, human",
]

_1984_response_generic = [
"Literally 2023",    
"Still better than this year",
"1CC members when they get automodded for the 69th time:",
"LiTeRaLlY 1984",
"https://cdn.discordapp.com/attachments/273459263471484928/1062320840550658078/image.png",

]

atrfate_quote = [
"Play better games",    
"lifes way of telling you to play better games",
"it says download and play better games",
"play better games best option",
"its gods way of saying play better games",


]

#url extractor stuff
extractor = URLExtract()

pf = ProfanityFilter()

acc_age = datetime.now() - timedelta(days=dayspassed)
tenko_join = datetime.now() - timedelta(days=tenkojoin)
user_join = datetime.now() - timedelta(days=userjoin)

print('Please wait warmly...')

#change process title
setproctitle.setproctitle('1CCBot')

initial_extensions = ['Modules.twitter']
client = discord.Client()

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.message_content = True

if debugmode == True:
    bot = commands.Bot(command_prefix=("1c."), case_insensitive=True)
    print ("debug")
else:
    bot = commands.Bot(command_prefix=commands.when_mentioned, case_insensitive=True, intents=intents)
    
bot.remove_command("help")


st = time.time()
secure_random = random.SystemRandom()

user_blacklist = open("txt/badactors.txt", "r")
badactors = user_blacklist.read()

user_tinfoil = open("txt/tinfoil.txt", "r")
tinfoil = user_tinfoil.read()

user_blacklist_main = open("txt/badactors_m.txt", "r")
badactors_m = user_blacklist_main.read()

badfiles = open("txt/badfiles.txt", "r")
badfilenames = badfiles.read()

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


#ready status display
@bot.event
async def on_ready():
    print(' ')
    print('Username - ' + bot.user.name)
    print('Version - ' + bot_version)
    await bot.change_presence(activity=discord.Game(name="/"))
    await asyncio.sleep(3)
    await bot.change_presence(activity=discord.Game(name="/"))
    #await bot.change_presence(activity=discord.Streaming(name="/1CC/", url='https://twitch.tv/99710'))

    
#error event code
#print the error to the console and inform the user   
@bot.event
async def on_command_error(ctx, error):
    #command not found
    if isinstance(error, commands.CommandNotFound):
#        await ctx.send("Error: Invalid command")        
        return
    #user failed check
    if isinstance(error, commands.CheckFailure):       
        await ctx.send("Error: Only the owner can use this command")
    else:
        await ctx.send(error)
        print(error)
        return

@bot.event
async def on_member_update(before, after):
    modrole = discord.utils.get(after.roles, name="Moderator")
    lockednick = discord.utils.get(after.roles, name="NoNickname")
    #print(after.nick)
    nickname = str(after.nick)
    
    crappynick = nickname.startswith('!')
    crappynick2 = nickname.startswith('(')
    crappynick3 = nickname.startswith('"')
    crappynick4 = nickname.startswith('#')
    crappynick5 = nickname.startswith("'")
    crappynick6 = nickname.startswith("-")
    crappynick7 = nickname.startswith(".")
    crappynick8 = nickname.startswith("*")
    
    name = str(after.name)
    crappyname = name.startswith('!')
    if modrole in after.roles:
        return
    if lockednick in after.roles:
        await after.edit(nick = None, reason = "NoNickname role")
        return
    if crappyname == True:
        newname = (name.replace('!', ''))
        await after.edit(nick = newname)
        return
    if crappynick == True:
        newnick = (nickname.replace('!', '឵!'))
        await after.edit(nick = newnick)
        #await after.edit(nick = "\U0001F4A9")
        return
    if crappynick2 == True:
        newnick = (nickname.replace('(', '឵('))
        await after.edit(nick = newnick)
        return
    if crappynick3 == True:
        newnick = (nickname.replace('"', '឵"'))
        await after.edit(nick = newnick)
        return
    if crappynick4 == True:
        newnick = (nickname.replace('#', '឵#'))
        await after.edit(nick = newnick)
        return
    if crappynick5 == True:
        newnick = (nickname.replace("'", "឵'"))
        await after.edit(nick = newnick)
        return
    if crappynick6 == True:
        newnick = (nickname.replace("-", "឵-"))
        await after.edit(nick = newnick)
        return
    if crappynick7 == True:
        newnick = (nickname.replace(".", "឵."))
        await after.edit(nick = newnick)
        return
    if crappynick8 == True:
        newnick = (nickname.replace("*", "឵*"))
        await after.edit(nick = newnick)
        return
    if "1ccbot" in nickname.lower():
        await after.edit(nick = "\U0001F4A9")
    else:
        return

@bot.event
async def on_guild_update(before, after):
    mentions = discord.NotificationLevel.only_mentions
    await asyncio.sleep(3)
    image = "Avatars/" + random.choice(os.listdir("Avatars"))
    newavatar = open(image, 'rb')
    banner = "Banners/" + random.choice(os.listdir("Banners"))
    newbanner = open(banner, 'rb')
    await after.edit(name="/1CC/ - Arcade and Doujin", icon = newavatar.read(), banner = newbanner.read(), default_notifications = mentions)
    return

#@bot.event
#async def on_member_unban(guild, user):
#    print(user.id)

@bot.event
async def on_member_join(member):
    #channel = member.guild.get_channel("162861213309599744")
    pb = open("txt/permaban.txt", "r")
    permaban = pb.read()
    if str(member.id) in permaban:
        await member.ban(reason='permaban')
        return

    print(member.name)
    if "h0nde" in member.name.lower():
        await member.ban(reason='autoban (join spam)')
        #await channel.send("<@166189271244472320>")
    return

@bot.event
async def on_message(message):
    emoji = '\U0001F6AB'
    contents = message.content
    hdd = open("txt/hddtext.txt", "r")
    hddtext = hdd.read()
    history = (await message.guild.get_channel(message.channel.id).history(limit=5).flatten())
    history_hdd = (await message.guild.get_channel(message.channel.id).history(limit=10).flatten())
    
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    if "https://bemaniso.ws/freeinvite.php" in contents.lower():
        await message.channel.send("^Bait")
        return

    if "http://bemaniso.ws/freeinvite.php" in contents.lower():
        await message.channel.send("^Bait")
        return

    if "<http://bemaniso.ws/freeinvite.php>" in contents.lower():
        await message.channel.send("^Bait")
        return

    if "<https://bemaniso.ws/freeinvite.php>" in contents.lower():
        await message.channel.send("^Bait")
        return

    if "<http://www.bemaniso.ws/freeinvite.php>" in contents.lower():
        await message.channel.send("^Bait")
        return

    if "<https://www.bemaniso.ws/freeinvite.php>" in contents.lower():
        await message.channel.send("^Bait")
        return
    
    if "ligma" in contents.lower() and str(message.channel) == "invites":
        await message.delete()
        return
    
    if "onlyfans" in contents.lower() and str(message.channel) == "invites":
        await message.delete()
        return

    if ", spicetools can be downloaded from " in contents.lower():
        if str(message.guild.me.id) in str(history):
            #await message.channel.purge(limit=1)
            #print ("iidx hdd")
            await message.add_reaction('\U0001F99C')
            return

        else:
            await message.channel.trigger_typing()
            await asyncio.sleep(1.7)
            await message.channel.send(secure_random.choice(spicetools_response))
            return
        

#role giving thingy, Removes the new guy role from a new user and assigns them a new role at random when they send a message
    role = discord.utils.get(message.guild.roles, name="new guy")
    badrole = discord.utils.get(message.guild.roles, name="role")
    nointro = discord.utils.get(message.guild.roles, name="NoIntroductions")
    user=message.author
    if role in message.author.roles and str(message.channel) == "introductions":

        name = message.author.name
        asciitext = strip_non_ascii(contents)
        nr = open("txt/nointro.txt", "r")
        norole = nr.read()
    
        if "test jconfig" in contents.lower():
            return

        if " uwu " in contents.lower():
            #await user.add_roles(nointro, reason='cringe intro')
            await message.channel.send(name + ", Your introduction is too cringe")
            return

        #if "ccp" in contents.lower():
            #await user.add_roles(nointro, reason='Shit intro')
            #return

        if "streancommunuty" in contents.lower():
            await message.author.ban(reason='Autoban: fake URL trade scam)', delete_message_days=1)
            return

        if len(message.content) < 7:
            await message.channel.send(name + ", Your introduction is too short")
            return

        if extractor.has_urls(asciitext):
            await message.channel.send(name + ", Ask a moderator for a role")
            return

        if pf.is_profane(asciitext) == True:
            if badrole in message.author.roles:
                await message.author.kick(reason="Can't read")
                return
            else:
                await message.channel.send(name + ", Introduce yourself properly!")
                await user.add_roles(badrole, reason='idk')
                return

        if str(message.author.id) in norole:
            #await message.channel.send(name + ", Ask a moderator for a role")
            return


        #if message.author.created_at > acc_age:
            #await ctx.send('<@' + message.author.id + '>' + 'Your Discord account is too new, Wait for a role\n(Account created: ' + str(message.author.created_at) + ')')
            #return

        
        #print('[debug] User has new guy role, giving a role')
        user=message.author
        newrole=discord.utils.get(message.guild.roles, name=secure_random.choice(Roles))
        
        if str(newrole) == "None":
            #print('[Debug] Random Broke, going to plan B')
            newrole2=discord.utils.get(message.guild.roles, name="pensi blue")
            oldrole=discord.utils.get(message.guild.roles, name='new guy')
            await user.remove_roles(oldrole, reason='User introduced themself')
            await user.add_roles(newrole2, reason='User introduced themself')
            return

        else:
            
            oldrole=discord.utils.get(message.guild.roles, name='new guy')
            await user.remove_roles(oldrole, reason='User introduced themself')
            #print('[Debug] Giving user ' + str(newrole))
            await user.add_roles(newrole, reason='User introduced themself')
            return

    role = discord.utils.get(message.guild.roles, name="Member")
    if role in message.author.roles:
        user=message.author
        memberrole=discord.utils.get(message.guild.roles, name='Member')
        await user.remove_roles(memberrole, reason='Unnecessary role')
        return

    role = discord.utils.get(message.guild.roles, name="kickme")
    modrole = discord.utils.get(message.guild.roles, name="Moderator")
    if role in message.author.roles:
        if modrole in message.author.roles:
            return
        else:
        #user=message.author
        #print(user.id)
            await message.author.kick(reason='user had "kickme" role')
            return

    role = discord.utils.get(message.guild.roles, name="Nogifs")
    if role in message.author.roles and message.attachments:
        #print(message.attachments)
        if ".gif" in str(message.attachments):
            await message.delete()
            return
        if ".gif" in message.content:
            await message.delete()
            return

    role = discord.utils.get(message.guild.roles, name="Noimages")
    if role in message.author.roles and message.attachments:
        await message.delete()
        return

    role = discord.utils.get(message.guild.roles, name="Noimages")
    if role in message.author.roles and ".jpg" in message.content:
        await message.delete()

    role = discord.utils.get(message.guild.roles, name="Noimages")
    if role in message.author.roles and ".png" in message.content:
        await message.delete()

    role = discord.utils.get(message.guild.roles, name="Noimages")
    if role in message.author.roles and ".gif" in message.content:
        await message.delete()    
        

  
#links application
    trusted = discord.utils.get(message.guild.roles, name="Trusted")
    user=message.author
    if str(message.channel) == "apply-for-links":
        #print("A")
            #account age check
        if message.author.created_at > acc_age:
            await ctx.send('<@' + message.author.id + '>' + 'Your Discord account is too new\n(Account created: ' + str(message.author.created_at) + ')')
            return
        
        if message.author.joined_at > user_join:
            await ctx.send('<@' + message.author.id + '>' + "You have not been in this server long enough\n(Joined server at: " + str(message.author.joined_at) + ")")
            return

        await user.add_roles(trusted, reason='Links access')
        return
        
        
    
    if str(message.author.id) in badactors and "hdd" in contents.lower():
        print("user triggered HDD check but id is whitelisted")
        #await message.channel.send('id ignored')
        return

    if str(message.author.id) in badactors_m:
        return


    if "h0nde" in contents.lower() and str(message.author.id) == "155149108183695360":
        await message.delete()
        return

    #dendy antivax crap
    if "the jab doesn't work" in contents.lower() and str(message.author.id) == "252442396879486976":
        await message.channel.send('https://www.cdc.gov/coronavirus/2019-ncov/vaccines/effectiveness/why-measure-effectiveness/breakthrough-cases.html\n `"However, since vaccines are not 100% effective at preventing infection, some people who are fully vaccinated will still get COVID-19."`')
        return
    
#game hdd/ssd checks
    if "iidx hdd" in contents.lower():  
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        if modrole in message.author.roles:
            await message.channel.send("<@" + str(message.author.id) +">", file=discord.File('pics/wig2.png'))
            return
                
        if str(message.guild.me.id) in str(history_hdd):
            #await message.channel.purge(limit=1)
            #print ("iidx hdd")
            await message.add_reaction('\U0001F1E7')
            await message.add_reaction('\U0001F1F7')
            await message.add_reaction('\U0001F1FA')
            await message.add_reaction('\U0001F1ED')
            return

        else:
            await message.channel.send(file=discord.File("pics/hdd/" + random.choice(os.listdir("pics/hdd"))))
            return

    if "sdvx hdd" in contents.lower(): 
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "iidx ssd" in contents.lower():  
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'SSD' is")
        #await message.channel.send(file=discord.File("pics/hdd/" + random.choice(os.listdir("pics/hdd"))))
        return

    if "sdvx ssd" in contents.lower(): 
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'SSD' is")
        return

    if "ddr hdd" in contents.lower():   
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "popn hdd" in contents.lower():   
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "jubeat hdd" in contents.lower():   
        #await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "hdd dump crack" in contents.lower():   
        #check if it's in CN channel
            if str(message.channel) == '中文':
                #await message.channel.send("<@" + str(message.author.id) +">" + ' <:cirblech:415143187762511872> 社会信用已被扣除', file=discord.File('pics/socialcredit.jpg'))
                #await message.channel.send("<@" + str(message.author.id) +">" + ' <:cirComfy:393180740608589834> 你已经获得了社会信用', file=discord.File('pics/socialcredit2.jpg'))
                await message.channel.send("<@" + str(message.author.id) +">" + ' 那不是德州的方式', file=discord.File('pics/texas.png'))
                return

            if modrole in message.author.roles:
                await message.channel.send("<@" + str(message.author.id) +">", file=discord.File('pics/wig2.png'))
                return

            else:

                if str(message.guild.me.id) in str(history_hdd):
                    #await message.channel.purge(limit=1)

                    #bruh
                    #await message.add_reaction('\U0001F1E7')
                    #await message.add_reaction('\U0001F1F7')
                    #await message.add_reaction('\U0001F1FA')
                    #await message.add_reaction('\U0001F1ED')

                    #no
                    await message.add_reaction('\U0001F1F3')
                    await message.add_reaction('\U0001F1F4')
                    
                    return
                
                else:
                    await message.channel.send("<@" + str(message.author.id) +">" + " **No**", file=discord.File('pics/brazil.png'))
                    return

    if "literally 1984" in contents.lower():
        noimages = discord.utils.get(message.guild.roles, name="Noimages")
        nogifs = discord.utils.get(message.guild.roles, name="Nogifs")
        _1984 = discord.utils.get(message.guild.roles, name="1984")

        if modrole in message.author.roles:
            return

        if str(message.guild.me.id) in str(history):
            return
                
        if noimages in message.author.roles:
            await message.channel.trigger_typing()
            await asyncio.sleep(1.1)
            await message.channel.send("<@" + str(message.author.id) +">" + " I'm very sorry that the direct and predictable results of your actions happened to you")
            return

        if nogifs in message.author.roles:
            await message.channel.trigger_typing()
            await asyncio.sleep(1.1)
            await message.channel.send("<@" + str(message.author.id) +">" + " I'm very sorry that the direct and predictable results of your actions happened to you")
            return
        
        if _1984 in message.author.roles:
            await message.channel.trigger_typing()
            await asyncio.sleep(1.1)
            await message.channel.send("<@" + str(message.author.id) +">" + " I'm very sorry that the direct and predictable results of your actions happened to you")
            return

        else:
            await message.channel.trigger_typing()
            await asyncio.sleep(1.1)
            await message.channel.send(secure_random.choice(_1984_response_generic))
            return
            
                
#    if "generic hdd" in contents.lower():   
#        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
#        return


#@everyone links autodetect
    #check if channel is links
    if str(message.channel) == "links":
        print(message.content)
        #check if user is a mod
        if modrole in message.author.roles:
            print("modrole")
            #check if user has typed @everyone
            if "<@&1049091051647926312>" in message.content:
                ateveryone = contents.replace("<@&1049091051647926312>", "@everyone")
                
                #ping everyone
                await message.channel.send(ateveryone)
                await message.delete()
                return

#@everyone links autodetect
    #check if channel is links
    if str(message.channel) == "news":
        print(message.content)
        #check if user is a mod
        if modrole in message.author.roles:
            print("modrole")
            #check if user has typed @everyone
            if "<@&1049091051647926312>" in message.content:
                ateveryone = contents.replace("<@&1049091051647926312>", "@everyone")
                
                #ping everyone
                await message.channel.send(ateveryone)
                await message.delete()
                return
            
        
    
    await bot.process_commands(message)

#command printing to console
@bot.event
async def on_command(ctx):
    print("[command] " + ctx.message.content[len("="):].strip() + " / " + str(ctx.guild))
    return


@bot.event
async def on_member_remove(member):
    #print(member.name)
    return

#owner check
def is_owner():
    async def predicate(ctx):
        return ctx.author.id == ownerid
    return commands.check(predicate)

#TenshiBot Hangout check
def is_hangout():
    async def predicate(ctx):
        return ctx.guild.id == 273086604866748426
    return commands.check(predicate)
    
#help command
@bot.command()
async def help(ctx):
    hlp = open("txt/help.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

#misc commands

@bot.command()
@is_owner()
async def ateveryone(ctx):
    await ctx.message.delete()
    await ctx.send('@everyone')


@bot.command()
async def restart(ctx):
    if ctx.author.id != ownerid:
        return
    else:
        await ctx.send("Restarting...")
        os.system("chmod +x reboot.sh")        
        os.system("./reboot.sh")
        return
    
@bot.command()
@commands.cooldown(1, 99999, commands.BucketType.default)
async def kickme(ctx):
    kicktime = randint(5,500)
    role = discord.utils.get(ctx.guild.roles, name="Moderator")
    if role in ctx.author.roles:
        await ctx.send('No')
        return

    else:
        await ctx.send('You will be kicked in ' + str(kicktime) + ' seconds')
        await asyncio.sleep(kicktime)
        #await ctx.author.send('https://discord.gg/UypwQ3R')
        await ctx.author.kick(reason='asked for it')

@bot.command()
@is_owner()
async def rpurge(ctx, chanid, number):
    yuyuko = bot.get_channel(int(chanid))
    print (yuyuko)
    await yuyuko.purge(limit=int(number))

@bot.command()
@is_owner()
async def rdel(ctx, msgid):
    yuyuko = await ctx.fetch_message(int(msgid))
    print (yuyuko)
    await yuyuko.delete()

@bot.command()
async def blech(ctx):
    await ctx.send('<:cirblech:415143187762511872>')

@bot.command()
@is_owner()
async def getrole(ctx):
    print ('[Debug] Giving user role')
    user=ctx.message.author
    newrole=discord.utils.get(ctx.guild.roles, name=secure_random.choice(Roles))
    oldrole=discord.utils.get(ctx.guild.roles, name='Test')
    await user.remove_roles(oldrole, reason='getrole')
    await user.add_roles(newrole, reason='getrole')

#loader/server info commands

@bot.command()
@is_owner()
async def gameloader(ctx):
    hlp = open("txt/gameloader_info.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

@bot.command()
@is_owner()
async def teknoparrot2(ctx):
    hlp = open("txt/tp_info.txt", "r")
    help_cmd = hlp.read()
    await ctx.send(help_cmd)

@bot.command()
async def teknoparrot(ctx):
    await ctx.send('Teknoparrot can be downloaded from https://teknoparrot.com/')
    #await ctx.send('(Check <#434222178922135553> to see if your game is supported by jconfig first)')

def retrieve_file_paths(dirName):
 
  # setup file paths variable
  filePaths = []
   
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)
         
  # return all paths
  return filePaths



@bot.command()
@commands.cooldown(1, 180, commands.BucketType.default)
async def spicetools_src(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check

    if str(ctx.channel) == '中文' or str(ctx.channel) == '日本語' or str(ctx.channel) == '한국어' or str(ctx.channel) == 'hidden_test':
        await ctx.send('Please wait')
        r = requests.get(spiceURL)
        with open('spicetools_ooc.zip', 'wb') as f:
            f.write(r.content)

        if aprilfools==True:
            await ctx.send('af')
            await asyncio.sleep(2)
            await ctx.author.send(file=discord.File('spicetools_ooc.zip'))
            return

        else:
            zf = ZipFile('spicetools_ooc.zip', 'r')
            #extract spicetools archive
            zf.extractall('spice_extracted')
            zf.close()
            #delete the exe files
            os.remove("spice_extracted/spicetools/spice.exe")
            os.remove("spice_extracted/spicetools/spice64.exe")
            os.remove("spice_extracted/spicetools/spicecfg.exe")
            #move info file to extracted spice directory
            #shutil.copyfile('txt/Spiceinfo_KR_CN_JP.txt', 'spice_extracted/spicetools/Info_KR_CN_JP.txt')
            
            #generate MD5s
            spicesrcmd5 = hashlib.md5(open('spice_extracted/spicetools/src/spicetools-master.tar.gz','rb').read()).hexdigest()

            #create md5 folder and write md5's of exe files to txt files
            os.mkdir("spice_extracted/spicetools/md5")
            ssrc = open("spice_extracted/spicetools/md5/spice_src.txt", "a")
            ssrc.write(spicesrcmd5)
            
            #close md5 txt files           
            ssrc.close()
            
            #define directory for rezipping
            dir_name = 'spice_extracted/spicetools'
            filePaths = retrieve_file_paths(dir_name)
            newspice = zipfile.ZipFile('Spicetools_src.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools_src.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("Spicetools_src.zip")
            return

    else:
        await ctx.send('Spicetools source code is included in the zip file')
        

@bot.command()
async def spicetools(ctx):
    name = ctx.author.name
    await ctx.send("Hi " + name + ", Spicetools can be downloaded from " + spiceURL2)


@bot.command()
@commands.cooldown(1, 90, commands.BucketType.default)
async def spicetools1(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check
    #asciinick = strip_non_ascii(ctx.author.nick)
    #asciiusername = strip_non_ascii(ctx.author.name)

#CN
    if str(ctx.channel) == '中文':
        await ctx.send('请稍等片刻...')
        r = requests.get(spiceURL)
        with open('spicetools_ooc.zip', 'wb') as f:
            f.write(r.content)

        if aprilfools==True:
            await ctx.send('*玩更好的游戏*')
            await asyncio.sleep(2)
            await ctx.author.send('开玩笑...')
            await ctx.author.send(file=discord.File('spicetools_ooc.zip'))
            return

        else:
            zf = ZipFile('spicetools_ooc.zip', 'r')
            #extract spicetools archive
            zf.extractall('spice_extracted')
            zf.close()
            #delete source code file to reduce size
            os.remove("spice_extracted/spicetools/src/spicetools-master.tar.gz")
            #move info file to extracted spice directory
            shutil.copyfile('txt/Spiceinfo_KR_CN_JP.txt', 'spice_extracted/spicetools/Info_KR_CN_JP.txt')
            
            #generate MD5s
            spice32md5 = hashlib.md5(open('spice_extracted/spicetools/spice.exe','rb').read()).hexdigest()
            spice64md5 = hashlib.md5(open('spice_extracted/spicetools/spice64.exe','rb').read()).hexdigest()
            spicecfgmd5 = hashlib.md5(open('spice_extracted/spicetools/spicecfg.exe','rb').read()).hexdigest()

            #create md5 folder and write md5's of exe files to txt files
            os.mkdir("spice_extracted/spicetools/md5")
            s32 = open("spice_extracted/spicetools/md5/spice.txt", "a")
            s32.write(spice32md5)
            s64 = open("spice_extracted/spicetools/md5/spice64.txt", "a")
            s64.write(spice64md5)
            scfg = open("spice_extracted/spicetools/md5/spicecfg.txt", "a")
            scfg.write(spicecfgmd5)
            
            #close md5 txt files           
            s32.close()
            s64.close()
            scfg.close()
            
            #define directory for rezipping
            dir_name = 'spice_extracted/spicetools'
            filePaths = retrieve_file_paths(dir_name)
            newspice = zipfile.ZipFile('Spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("Spicetools.zip")
            return

#JP
    if str(ctx.channel) == '日本語':
        await ctx.send('お待ちください...')
        r = requests.get(spiceURL)
        with open('spicetools_ooc.zip', 'wb') as f:
            f.write(r.content)

        if aprilfools==True:
            await ctx.send('*より良いゲームをプレイする*')
            await asyncio.sleep(2)
            await ctx.author.send('冗談だ')
            await ctx.author.send(file=discord.File('spicetools_ooc.zip'))
            return

        else:
            zf = ZipFile('spicetools_ooc.zip', 'r')
            #extract spicetools archive
            zf.extractall('spice_extracted')
            zf.close()
            #delete source code file to reduce size
            os.remove("spice_extracted/spicetools/src/spicetools-master.tar.gz")
            #move info file to extracted spice directory
            shutil.copyfile('txt/Spiceinfo_KR_CN_JP.txt', 'spice_extracted/spicetools/Info_KR_CN_JP.txt')
            
            #generate MD5s
            spice32md5 = hashlib.md5(open('spice_extracted/spicetools/spice.exe','rb').read()).hexdigest()
            spice64md5 = hashlib.md5(open('spice_extracted/spicetools/spice64.exe','rb').read()).hexdigest()
            spicecfgmd5 = hashlib.md5(open('spice_extracted/spicetools/spicecfg.exe','rb').read()).hexdigest()

            #create md5 folder and write md5's of exe files to txt files
            os.mkdir("spice_extracted/spicetools/md5")
            s32 = open("spice_extracted/spicetools/md5/spice.txt", "a")
            s32.write(spice32md5)
            s64 = open("spice_extracted/spicetools/md5/spice64.txt", "a")
            s64.write(spice64md5)
            scfg = open("spice_extracted/spicetools/md5/spicecfg.txt", "a")
            scfg.write(spicecfgmd5)
            
            #close md5 txt files           
            s32.close()
            s64.close()
            scfg.close()
            
            #define directory for rezipping
            dir_name = 'spice_extracted/spicetools'
            filePaths = retrieve_file_paths(dir_name)
            newspice = zipfile.ZipFile('Spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("Spicetools.zip")
            return

#KR
    if str(ctx.channel) == '한국어':
        await ctx.send('기다려주세요 ...')
        r = requests.get(spiceURL)
        with open('spicetools_ooc.zip', 'wb') as f:
            f.write(r.content)

        if aprilfools==True:
            await ctx.send('*접근 불가*')
            await asyncio.sleep(2)
            await ctx.author.send('만우절')
            await ctx.author.send(file=discord.File('spicetools_ooc.zip'))
            return

        else:
            zf = ZipFile('spicetools_ooc.zip', 'r')
            #extract spicetools archive
            zf.extractall('spice_extracted')
            zf.close()
            #delete source code file to reduce size
            os.remove("spice_extracted/spicetools/src/spicetools-master.tar.gz")
            #move info file to extracted spice directory
            shutil.copyfile('txt/Spiceinfo_KR_CN_JP.txt', 'spice_extracted/spicetools/Info_KR_CN_JP.txt')
            
            #generate MD5s
            spice32md5 = hashlib.md5(open('spice_extracted/spicetools/spice.exe','rb').read()).hexdigest()
            spice64md5 = hashlib.md5(open('spice_extracted/spicetools/spice64.exe','rb').read()).hexdigest()
            spicecfgmd5 = hashlib.md5(open('spice_extracted/spicetools/spicecfg.exe','rb').read()).hexdigest()

            #create md5 folder and write md5's of exe files to txt files
            os.mkdir("spice_extracted/spicetools/md5")
            s32 = open("spice_extracted/spicetools/md5/spice.txt", "a")
            s32.write(spice32md5)
            s64 = open("spice_extracted/spicetools/md5/spice64.txt", "a")
            s64.write(spice64md5)
            scfg = open("spice_extracted/spicetools/md5/spicecfg.txt", "a")
            scfg.write(spicecfgmd5)
            
            #close md5 txt files           
            s32.close()
            s64.close()
            scfg.close()
            
            #define directory for rezipping
            dir_name = 'spice_extracted/spicetools'
            filePaths = retrieve_file_paths(dir_name)
            newspice = zipfile.ZipFile('Spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("Spicetools.zip")
            return

    #TEST
    if str(ctx.channel) == 'hidden_test':
        await ctx.send('Please wait...')
        r = requests.get(spiceURL)
        with open('spicetools_ooc.zip', 'wb') as f:
            f.write(r.content)

        if aprilfools==True:
            await ctx.send('af_string')
            await asyncio.sleep(2)
            await ctx.author.send('af_jk_string')
            await ctx.author.send(file=discord.File('Spicetools.zip'))
            return

        else:
            zf = ZipFile('spicetools_ooc.zip', 'r')
            #extract spicetools archive
            zf.extractall('spice_extracted')
            zf.close()
            #delete source code file to reduce size
            os.remove("spice_extracted/spicetools/src/spicetools-master.tar.gz")
            #move info file to extracted spice directory
            shutil.copyfile('txt/Spiceinfo_KR_CN_JP.txt', 'spice_extracted/spicetools/Info_KR_CN_JP.txt')
            
            #generate MD5s
            spice32md5 = hashlib.md5(open('spice_extracted/spicetools/spice.exe','rb').read()).hexdigest()
            spice64md5 = hashlib.md5(open('spice_extracted/spicetools/spice64.exe','rb').read()).hexdigest()
            spicecfgmd5 = hashlib.md5(open('spice_extracted/spicetools/spicecfg.exe','rb').read()).hexdigest()

            #create md5 folder and write md5's of exe files to txt files
            os.mkdir("spice_extracted/spicetools/md5")
            s32 = open("spice_extracted/spicetools/md5/spice.txt", "a")
            s32.write(spice32md5)
            s64 = open("spice_extracted/spicetools/md5/spice64.txt", "a")
            s64.write(spice64md5)
            scfg = open("spice_extracted/spicetools/md5/spicecfg.txt", "a")
            scfg.write(spicecfgmd5)
            
            #close md5 txt files           
            s32.close()
            s64.close()
            scfg.close()
            
            #define directory for rezipping
            dir_name = 'spice_extracted/spicetools'
            filePaths = retrieve_file_paths(dir_name)
            newspice = zipfile.ZipFile('Spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("Spicetools.zip")
            return

    else:
        if aprilfools==True:
            await ctx.send('<@' + str(ctx.author.id) + '>' + ' Play better games')
            await asyncio.sleep(3)
            await ctx.author.send('April fools!. Spicetools can be downloaded from ' + spiceURL)
            return
        else:
            print (ctx.author.nick)
            nick = ctx.author.nick
            name = ctx.author.name
            
            if nick == None:
                await ctx.send("Hi " + name + ", Spicetools can be downloaded from " + spiceURL)
                return
            
            if "@everyone" in nick:
                await ctx.send("Hi `" + nick + "`, Spicetools can be downloaded from " + spiceURL)
                return
            if "@here" in nick:
                await ctx.send("Hi `" + nick + "`, Spicetools can be downloaded from " + spiceURL)
                return
            else:
                await ctx.send("Hi " + asciinick + ", Spicetools can be downloaded from " + spiceURL)   
                return


@bot.command()
async def bemanitools(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check

    #CN
    if str(ctx.channel) == '中文':
        #await ctx.send('您可以从下载 ' + spiceURL)
        await ctx.send('您可以从 ' + btoolURL + ' 下载')
        return
    #JP
    if str(ctx.channel) == '日本語':
        await ctx.send(btoolURL + ' からダウンロードできます')
        return
    #KR
    if str(ctx.channel) == '한국어':
        await ctx.send(btoolURL +' 에서 얻을 수 있습니다')
        return
    else:
        await ctx.send('Bemanitools can be downloaded from ' + btoolURL)
        return     

#@bot.command()
#async def xrpcv(ctx):
#    await ctx.send('Xrpcv can be downloaded from http://193.70.38.209/file/xrpcv_2202.7z')
#    await ctx.send('Consider using asphyxia instead')

@bot.command()
async def jconfig(ctx):
    await ctx.send('Jconfig can be downloaded from wherever. Be sure to read the readme')

#owner commands
@bot.command()
@is_owner()  
async def setstatus_stream(ctx, *, args):
    await bot.change_presence(activity=discord.Streaming(name= args, url='https://twitch.tv/99710'))

@bot.command()
@is_owner()  
async def setstatus(ctx, *, args):
    await bot.change_presence(activity=discord.Game(name= args))

@bot.command()
@is_owner()    
async def vpsreboot(ctx):
    #os.system("sudo reboot")
    os.system("shutdown -r -t 30")
    await ctx.send('Rebooting the VPS')

#console command
@bot.command()
@is_owner()
#freezes the bot!
async def console(ctx):
    cmd=ctx.message.content[len("<@571094749537239042> console"):].strip()
    result = subprocess.check_output([cmd], stderr=subprocess.STDOUT)
    #os.system(ctx.message.content)
    await ctx.send(result)    

#debug commands    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def rs(ctx):
    if ctx.author.id == ownerid:
        
        image = "Avatars/" + random.choice(os.listdir("Avatars"))
        newavatar = open(image, 'rb')
        await ctx.guild.edit(name="/1CC/ - Arcade and Doujin", icon = newavatar.read())
        await ctx.send("ok")
        return
    else:
        await ctx.send("ok")
    
@bot.command()
async def errortest(ctx):
    await()

#about
@bot.command()
async def about(ctx):
    second = time.time() - st
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)

    uptime='%dw,' % (week) + ' %dd,' % (day) + ' %dh,' % (hour) + ' %dm,' % (minute) + ' and %ds.' % (second)
    servercount=str(len(bot.guilds))
    buildinfo="%s" % time.ctime(os.path.getmtime("1ccbot.py"))

    em=discord.Embed(colour=0xff0000)
    em.set_author(name= bot.user.name + ' info')
    em.add_field(name="Version", value=bot_version, inline=False)
    em.add_field(name="Uptime", value=uptime, inline=False)
    em.add_field(name="1ccbot.py timestamp", value=buildinfo, inline=False)
    em.set_footer(text="Created by KawashiroDev")
    await ctx.send(embed=em)

@bot.command()
async def rate(ctx):
    if int(ctx.channel.id) != int("240170132104675328"):
        await ctx.send("Go to <#240170132104675328>")
        return
    await ctx.send("I rate it " + str(randint(0,10)) + "/10")

@bot.command()
async def md(ctx, arg):
    await ctx.send("`" + arg + "`")

@bot.command()
async def encode(ctx, arg):
    trusted = discord.utils.get(ctx.guild.roles, name="trusted")
    message = arg
    message_bytes = message.encode('ascii')
    base64_message = base64.b64encode(message_bytes)
    b64string = base64_message.decode("ascii")
    #print(base64_message)
    if str(ctx.channel) == 'links':
        if trusted in ctx.author.roles:
            await ctx.send(b64string)
            await ctx.message.delete()
        else:
            await ctx.send("This command can only be used by trusted people")
            return
    else:
        await ctx.send("This command can only be used in links channel")
        return

@bot.command()
async def emote(ctx, arg):
    await ctx.send("<" + arg + ">")

@bot.command()
@is_owner()
async def say(ctx, *, args):
    await ctx.send(args)

@bot.command()
@is_owner()
async def dsay(ctx, *, args):
    await ctx.send(args)
    await ctx.message.delete()

@bot.slash_command(name="givemesocialcredits", description="这个命令是做什么的")
@commands.cooldown(1, 5, commands.BucketType.default)
async def socialcredit_slash(ctx):
    #await ctx.respond("You have gained social credits", file=discord.File("pics/socialcredit2.jpg" ))
    await ctx.respond(" ", file=discord.File("pics/no_u.png" ))

@bot.slash_command(name="atrfate_quote", description="Quotes from the #1 rhythm game fan")
@commands.cooldown(1, 10, commands.BucketType.default)
async def atrfatequote_slash(ctx):
    await ctx.respond(file=discord.File("pics/atrquote/" + random.choice(os.listdir("pics/atrquote"))))

@bot.slash_command(name="arcade_image", description="Get an arcade related image")
@commands.cooldown(1, 90, commands.BucketType.default)
async def arcadeimg_slash(ctx):

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get('http://' + "gelbooru.com" + '/index.php?page=dapi&s=post&q=index&api_key=' + g_api + '&user_id=' + g_user + '&tags=rating:general+-animated+arcade') as r:
            if r.status == 200:
                soup = BeautifulSoup(await r.text(), "lxml")
                num = int(soup.find('posts')['count'])
                #print ('[Debug] num = ' + str(num))
                maxpage = int(round(num/100))
                #print ('[Debug] maxpage = ' + str(maxpage))
                page = random.randint(0, maxpage)
                #print ('[Debug] page = ' + str(page))
                t = soup.find('posts')
                p = t.find_all('post')
                if num == 0: 
                    #msg = "**No posts found, Try:**\nChecking the tags are spelt correctly\nChanging your search query\nSearching with the Gelbooru command"
                    #await ctx.respond(msg)
                    return

                else:
                    source = ((soup.find('post'))('source'))
                    if num < 100:
                        pic = p[random.randint(0,num-1)]
                    elif page == maxpage:
                        pic = p[random.randint(0,99)]
                    else:
                        pic = p[random.randint(0,99)]
                    img_url = pic('file_url')
                    url_strip_start = str(img_url).strip('[<file_url>')
                    raw_url = str(url_strip_start).strip('</file_url>]')
                    img_id = pic('id')
                    id_strip_start = str(img_id).strip('[<id>')
                    sbooru_id = str(id_strip_start).strip('</id>]')

                    #sbooru_tags = pic['tags']
                    img_sauce = pic('source')
                    if img_sauce == '':
                        img_sauce = '[<source>No source listed</source>]'
                    source_strip_start = str(img_sauce).strip('[<source>')
                    sbooru_sauce = str(source_strip_start).strip('</source>]')
                           
                    img_width = pic('width')
                
                    width_strip_start = str(img_width).strip('[<width>')
                    width = str(width_strip_start).strip('</width>]')

                    img_height = pic('height')
                    height_strip_start = str(img_height).strip('[<height>')
                    height = str(height_strip_start).strip('</height>]')
                            
                    #creator = pic['creator_id']
                    if sbooru_sauce == '':
                        sbooru_sauce = 'No source listed'
                    em = discord.Embed(title='', description='', colour=0x42D4F4)
                    em.set_author(name='Arcade image')
                    em.set_image(url=str(raw_url))
                    #em.add_field(name="Image Source", value=sbooru_sauce, inline=False)    
                    em.add_field(name="Number", value=sbooru_id, inline=True)
                    em.add_field(name="Dimensions", value=width + "x" + height, inline=True)
                    #em.add_field(name="Query", value="`" + tags + "`", inline=False)
                    #em.set_image(url=booruappend + msg)
                    await ctx.respond(embed=em)
                    return

            msg = 'This command is unavailable at this time'
            await ctx.respond(msg)
            return


#@bot.slash_command(name="ooc info", description="Triggering Joh any% speedrun")
#async def oocinfo_slash(ctx):
    #hlp = open("txt/ooc_info.txt", "r")
    #help_cmd = hlp.read()
    #await ctx.respond(help_cmd)

#@bot.slash_command(name="bemaniso info", description="Triggering Corin any% speedrun")
#async def bemanisoinfo_slash(ctx):
    #hlp = open("txt/bemaniso_info.txt", "r")
    #help_cmd = hlp.read()
    #await ctx.respond(help_cmd)


#tkn = open("Tokens/tenshi_debug.txt", "r")
tkn = open("Tokens/tenshi_production.txt", "r")
token = tkn.read()
tkn.close()    
bot.run(token, reconnect=True)

