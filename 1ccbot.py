#1ccbot created by 99710
#based on TB 2.0.9

##Parameters##

#Version
bot_version = '1.4'

#owner id
ownerid = 166189271244472320

#debug switch
debugmode = False

#Spicetools URL
spiceURL = "http://onlyone.cab/downloads/spicetools-latest.zip"

#Bemanitools URL
btoolURL = "http://tools.bemaniso.ws/bemanitools-v5.30.zip"

#segatools URL
stoolURL = "http://example.com"

#asphyxia URL
asphURL = "http://example.com"

#April fools mode
aprilfools=False

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

from discord.ext import commands
from random import randint
from datetime import datetime, timedelta, date
from zipfile import ZipFile

Roles = [
"green",     
"light green",    
"dark green",
"purple",
"magenta",
"pensi blue",
"pink",
"cyan",
"gold",
"yellow",
"orange",
"red",
]

Roles_special = [
"pale green",     
"sky blue",    
"neon pink",
"peach",
"silver",
]

print('Please wait warmly...')

#initial_extensions = ['Modules.image', 'Modules.booru']
client = discord.Client()

if debugmode == True:
    bot = commands.Bot(command_prefix=("1c."), case_insensitive=True)
    print ("debug")
else:
    bot = commands.Bot(command_prefix=commands.when_mentioned, case_insensitive=True)
    
bot.remove_command("help")


st = time.time()
secure_random = random.SystemRandom()

user_blacklist = open("txt/badactors.txt", "r")
badactors = user_blacklist.read()

user_blacklist_main = open("txt/badactors_m.txt", "r")
badactors_m = user_blacklist_main.read()

#if __name__ == '__main__':
#    for extension in initial_extensions:
#        bot.load_extension(extension)


#ready status display
@bot.event
async def on_ready():
    print(' ')
    print('Username - ' + bot.user.name)
    print('TenshiBot Ver - ' + bot_version)
    await bot.change_presence(activity=discord.Game(name="Startup complete"))
    await asyncio.sleep(7)
    await bot.change_presence(activity=discord.Streaming(name="/1CC/", url='https://twitch.tv/99710'))

    
#error event code
#print the error to the console and inform the user   
@bot.event
async def on_command_error(ctx, error):
    #command not found
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Error: Invalid command")        
        return
    #user failed check
    if isinstance(error, commands.CheckFailure):       
        await ctx.send("Error: Only the owner can use this command")
    else:
        await ctx.send(error)
        print(error)
        return

@bot.event
async def on_message(message):
    emoji = '\U0001F6AB'
    contents = message.content
    hdd = open("txt/hddtext.txt", "r")
    hddtext = hdd.read()
    if message.author == bot.user:
        return
    if message.author.bot:
        return

#role giving thingy, Removes the new guy role from a new user and assigns them a new role at random when they send a message
    role = discord.utils.get(message.guild.roles, name="new guy")
    if role in message.author.roles:
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
        
    
    if str(message.author.id) in badactors and "hdd" in contents.lower():
        print("user triggered HDD check but id is whitelisted")
        #await message.channel.send('id ignored')
        return

    if str(message.author.id) in badactors_m:
        return
    
#game hdd checks
    if "iidx hdd" in contents.lower():  
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "sdvx hdd" in contents.lower(): 
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "ddr hdd" in contents.lower():   
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "popn hdd" in contents.lower():   
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

    if "jubeat hdd" in contents.lower():   
        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
        return

#    if "generic hdd" in contents.lower():   
#        await message.channel.send("<@" + str(message.author.id) +">" + " Please google what a 'HDD' is")
#        return
    
    await bot.process_commands(message)

#command printing to console
@bot.event
async def on_command(ctx):
    print("[command] " + ctx.message.content[len("="):].strip() + " / " + str(ctx.guild))
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
@commands.cooldown(1, 99999, commands.BucketType.default)
async def kickme(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Moderator")
    if role in ctx.author.roles:
        await ctx.send('No')
        return

    else:
        await ctx.send('You will be kicked in 10 seconds')
        await asyncio.sleep(10)
        await ctx.author.send('https://discord.gg/UypwQ3R')
        await ctx.author.kick(reason='asked for it')

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
    await ctx.send('(Check <#434222178922135553> to see if your game is supported by jconfig first)')

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
@commands.cooldown(1, 90, commands.BucketType.default)
async def spicetools(ctx):
    #foreign channel checks
    #id's aren't hardcoded as the channels may be deleted and remade which would break an id check

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
            os.remove("spicetools.zip")
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
            newspice = zipfile.ZipFile('spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("spicetools.zip")
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
            newspice = zipfile.ZipFile('spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("spicetools.zip")
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
            newspice = zipfile.ZipFile('spicetools.zip', 'w')
            with newspice:
                for file in filePaths:
                    newspice.write(file, compress_type=zipfile.ZIP_DEFLATED)
            newspice.close()
            
            await ctx.send(file=discord.File('Spicetools.zip'))

            #delete files
            shutil.rmtree("spice_extracted")
            os.remove("spicetools.zip")
            return

    else:
        if aprilfools==True:
            await ctx.send('<@' + str(ctx.author.id) + '>' + ' Play better games')
            await asyncio.sleep(3)
            await ctx.author.send('April fools!. Spicetools can be downloaded from ' + spiceURL)
            return
        else:
            await ctx.send('Spicetools can be downloaded from ' + spiceURL)
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

@bot.command()
async def xrpcv(ctx):
    await ctx.send('Xrpcv can be downloaded from http://193.70.38.209/file/xrpcv_2202.7z')
    await ctx.send('Consider using asphyxia instead')

@bot.command()
async def jconfig(ctx):
    await ctx.send('Jconfig can be downloaded from <#434222178922135553>. Be sure to read the readme')

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
    em.set_author(name= bot.user.name + ' info', icon_url=bot.user.avatar_url)
    em.add_field(name="Version", value=bot_version, inline=False)
    em.add_field(name="Uptime", value=uptime, inline=False)
    em.add_field(name="1ccbot.py timestamp", value=buildinfo, inline=False)
    em.set_footer(text="Created by 99710")
    await ctx.send(embed=em)

@bot.command()
async def rate(ctx):
    await ctx.send("I rate it " + str(randint(0,10)) + "/10")

@bot.command()
async def md(ctx, arg):
    await ctx.send("`" + arg + "`")

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

#tkn = open("Tokens/tenshi_debug.txt", "r")
tkn = open("Tokens/tenshi_production.txt", "r")
token = tkn.read()
tkn.close()    
bot.run(token, bot=True, reconnect=True)

