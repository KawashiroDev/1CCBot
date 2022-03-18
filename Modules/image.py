#1CCBot Image module v3

import discord
import requests
import aiohttp
#import praw
import lxml
import random
import asyncio
import twitter
import re

from discord.ext import commands
from bs4 import BeautifulSoup

#ignore certificate errors
#applies to the imagefetch function
ignorebadssl = True

#booru URL, used for touhou images and safebooru command
booru = 'gelbooru.com'

#booru rating
#options are: safe, questionable, explicit
#affects the safebooru command only
boorurating = 'safe'

#booru tag blacklist
#results which have these tags won't be shown in the touhou commands
#does not affect the safebooru command
#huge filesize is blacklisted to help fix some images not embedding

#if adding stuff to the blacklist, add it to the v2 section and not this
boorublacklist = 'rating:safe+-underwear+-sideboob+-pov_feet+-underboob+-upskirt+-sexually_suggestive+-ass+-bikini+-6%2Bgirls+-comic+-greyscale+-bdsm+-huge_filesize+-lovestruck+-absurdres+-artificial_vagina+-swimsuit+-covering_breasts+-huge_breasts+-blood+-penetration_gesture+-animated+-audio+-webm+rating:safe+-seductive_smile+-no_bra+-off_shoulder+-breast_hold+-cleavage+-nori_tamago+-nude+-butt_crack+-naked_apron'

boorublacklistgif = 'rating:safe+-underwear+-sideboob+-pov_feet+-underboob+-upskirt+-sexually_suggestive+-ass+-bikini+-6%2Bgirls+-comic+-greyscale+-bdsm+-huge_filesize+-lovestruck+-absurdres+-artificial_vagina+-swimsuit+-covering_breasts+-huge_breasts+-blood+-penetration_gesture+-audio+-webm+rating:safe+-seductive_smile+-no_bra+-off_shoulder+-breast_hold+-cleavage+-nori_tamago+-nude+-butt_crack+-naked_apron'

#tag blacklist v2

#base tags to apply to all levels (except gifs)
boorutags_base = 'rating:safe+-huge_filesize+-animated+-audio+-webm+-absurdres+-monochrome'
#artists whose works slip by the tag filters
badartists = '+-nori_tamago+-shiraue_yuu+-hammer_(sunset_beach)+-roke_(taikodon)+-guard_bento_atsushi+-kushidama_minaka+-manarou+-shounen_(hogehoge)+-fusu_(a95101221)+-guard_vent_jun+-teoi_(good_chaos)+-wowoguni+-yadokari_genpachirou+-hydrant_(kasozama)+-e.o.+-fusu_(a95101221)+-nishiuri+-freeze-ex+-yuhito_(ablbex)+-koto_inari+-kurogarasu+-pokio'
#base tags for gif command
boorutags_gif = 'rating:safe+-6%2Bgirls+-comic+-greyscale+-huge_filesize+-audio+-webm+-absurdres'
#default blacklisted tags (full SFW mode)
badtags_strict = "-underwear+-sideboob+-pov_feet+-underboob+-upskirt+-sexually_suggestive+-ass+-bikini+-spread_legs+-bdsm+-lovestruck+-artificial_vagina+-swimsuit+-covering_breasts+-huge_breasts+-blood+-penetration_gesture+-seductive_smile+-no_bra+-off_shoulder+-breast_hold+-cleavage+-nude+-butt_crack+-naked_apron+-convenient_censoring+-bra+-trapped+-restrained+-skirt_lift+-open_shirt+-underwear+-evil_smile+-evil_grin+-choker+-head_under_skirt+-skeleton+-open_fly+-o-ring_bikini+-middle_finger+-white_bloomers+-hot+-tank_top_lift+-short_shorts+-alternate_breast_size+-belly+-wind_lift+-you_gonna_get_raped+-convenient_leg+-convenient_arm+-downblouse+-torn_clothes+-sweater_lift+-open-chest_sweater+-bunnysuit+-gag+-gagged+-ball_gag+-hanging+-erect_nipples+-head_out_of_frame+-covering+-skirt_around_ankles+-furry+-shirt_lift+-vest_lift+-lifted_by_self+-when_you_see_it+-feet+-thighs+-skirt_hold+-open_dress+-open_clothes+-naked_shirt+-shirt_tug+-hip_vent+-no_panties+-surprised+-onsen+-naked_towel+-have_to_pee+-skirt_tug+-pole_dancing+-stripper_pole+-dimples_of_venus+-topless+-trembling+-no_humans+-creepy+-showgirl_skirt+-cookie_(touhou)+-pov+-fusion+-drugs+-weed+-forced_smile+-mouth_pull+-groin+-corruption+-dark_persona+-arms_behind_head+-crop_top+-gluteal_fold+-pregnant+-younger+-white_swimsuit+-tsundere+-crying+-naked_sheet+-undressing+-parody+-under_covers+-genderswap+-real_life_insert+-what+-confession+-race_queen+-naked_cloak+-latex+-bodysuit+-nazi+-swastika+-strap_slip+-chemise+-see-through+-dark+-bad_anatomy+-poorly_drawn+-messy+-you're_doing_it_wrong+-midriff+-large_breasts+-embarrassed+-smelling+-chains+-collar+-arms_up+-blurry_vision+-obese+-miniskirt+-leg_hold+-knees_to_chest+-knees_up+-clothes_pull+-giantess+-stepping+-shirtless+-3d+-smoking+-wall_slam+-noose+-4chan+-sheet_grab+-m_legs+-magnifying_glass+-fingering+-bandaid_on_pussy+-bandaids_on_nipples+-censored+-double_penetration+-erection+-group_sex+-double_handjob+-naizuri+-pasties+-penis+-sex+-pussy+-vaginal+-anal+-nipples+-aerolae+-large_areolae+-breasts_out+-breast_grab+-futanari+-implied_futanari+-condom+-condom_in_mouth+-cum+-used_condom"
#tags to blacklist in TenshiBot Hangout
badtags_hangout = '-sideboob+-pov_feet+-upskirt+-sexually_suggestive+-bdsm+-lovestruck+-artificial_vagina+-covering_breasts+-huge_breasts+-blood+-penetration_gesture+-seductive_smile+-no_bra+-breast_hold+-nude+-butt_crack+-naked_apron'
#tags to blacklist in moderate mode
badtags_moderate = '-sideboob+-pov_feet+-underboob+-upskirt+-sexually_suggestive+-bdsm+-lovestruck+-artificial_vagina+-covering_breasts+-huge_breasts+-blood+-penetration_gesture+-no_bra+-nude+-butt_crack+-naked_apron'
#tags to blacklist in an NSFW channel
badtags_nsfwmode = ''

#image shuffler queries (experimental!, may return questionable images)
last_updated = "+sort:updated:desc"
random_hq = "+sort:random+score:>=10"

#not used
randomsort = "+sort:random"
minscore = "score:>=0"
sorting = "sort:updated:desc"
startpage = "&pid=42"
#+sort:random:123

#rng stuff
score_rng_max = "5"
#score_rng = random.randint(0,5)

#append text to the start of booru url output
#change this if the bot is sending malformed booru urls
#safebooru URL's used to need http added to the start but now they dont anymore
booruappend = ''

#ratelimiting options
#number of commands which can be ran in timeframe
rlimit_cmd = 3
#timeframe (seconds)
rlimit_time = 10
#

#patreon nag text
patreonnag = "patreonnag text"

#general footer
normalfooter = "todo:put something here"

footer = [
normalfooter,
normalfooter,     
normalfooter,
normalfooter,
patreonnag,
]


#text config
if booru == 'gelbooru.com':
    idtext = 'Gbooru ID'
    idtext_seija = 'pᴉ nɹooqƃ'
    idtext_sukuna = 'ᴳᵇᵒᵒʳᵘ ᴵᴰ'
if booru == 'safebooru.org':
    idtext = 'Sbooru ID'
    idtext_seija = 'pᴉ nɹooqs'
    idtext_sukuna = 'ˢᵇᵒᵒʳᵘ ᴵᴰ'

embedtitle = 'Character image'
embedtitle_jp = 'キャラクター画像'
    
keiki_title = [
"Character image",
"Create!",     
"Oh!",
]

#twitter stuff
t_api = open("Tokens/twitter_consumer.txt", "r")
tw_api = t_api.read()
t_secret = open("Tokens/twitter_consumer_secret.txt", "r")
tw_secret = t_secret.read()
t_access = open("Tokens/twitter_access.txt", "r")
tw_access = t_access.read()
t_access_secret = open("Tokens/twitter_access_secret.txt", "r")
tw_access_secret = t_access_secret.read()



api = twitter.Api(consumer_key=tw_api,
consumer_secret=tw_secret,
access_token_key=tw_access,
access_token_secret=tw_access_secret)

class ImageCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def imagefetch(self, ctx, char, em, rng=1):
        if rng==1:
            score_rng = random.randint(0, 5)
            char = char + str(score_rng)
            print(score_rng)
        # check if Tenshi has a flag enabled or not
        moderate_role = discord.utils.get(ctx.guild.roles, name="tenko_moderatemode")
        if moderate_role in ctx.guild.me.roles:
            booruurl = 'http://' + booru + '/index.php?page=dapi&s=post&q=index&tags=' + boorutags_base + badtags_moderate + '+' + char
            embed_name = 'Arcade image'
            em.set_footer(text="Moderate mode is enabled on this server, image may not be SFW")
        else:
            booruurl = 'http://' + booru + '/index.php?page=dapi&s=post&q=index&tags=' + boorutags_base + badtags_strict + badartists + '+' + char
            embed_name = 'Arcade image'
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            async with session.get(booruurl) as r:
                # print(booruurl)
                if r.status == 200:
                    soup = BeautifulSoup(await r.text(), "lxml")
                    num = int(soup.find('posts')['count'])
                    maxpage = int(round(num / 100))
                    page = random.randint(0, maxpage)
                    t = soup.find('posts')
                    p = t.find_all('post')
                    source = ((soup.find('post'))('source'))
                    if num < 100:
                        pic = p[random.randint(0, num - 1)]
                    elif page == maxpage:
                        pic = p[random.randint(0, 99)]
                    else:
                        pic = p[random.randint(0, 99)]
                    img_url = pic('file_url')
                    #for link in img_url:
                        #print(img_url.text)
                    #and cue the jankyness
                    #bs4 does have a way to do this
                    url_strip_start = str(img_url).strip('[<file_url>')
                    raw_url = str(url_strip_start).strip('</file_url>]')
                    #print(raw_url)
                    
                    img_id = pic('id')
                    id_strip_start = str(img_id).strip('[<id>')
                    sbooru_id = str(id_strip_start).strip('</id>]')
                    #print(sbooru_id)
                    
                    img_tags = pic('tags')
                    
                    img_sauce = pic('source')
                    if img_sauce == '':
                        img_sauce = '[<source>No source listed</source>]'
                    source_strip_start = str(img_sauce).strip('[<source>')
                    sbooru_sauce = str(source_strip_start).strip('</source>]')
                    #print(sbooru_sauce)
                    
                    # sbooru_sauce = "https://i.pximg.net/img-original/img/2020/12/25/18/14/37/86528174_p0.png"
                    img_width = pic('width')
                    
                    width_strip_start = str(img_width).strip('[<width>')
                    width = str(width_strip_start).strip('</width>]')
                    
                    img_height = pic('height')
                    height_strip_start = str(img_height).strip('[<height>')
                    height = str(height_strip_start).strip('</height>]')
                    
                    #creator = pic('creator_id')
                    if sbooru_sauce == '':
                        sbooru_sauce = 'No source listed'
                    if "hentai" in sbooru_sauce:
                        sbooru_sauce = "Source hidden\n(NSFW website)"
                    if "pixiv" in sbooru_sauce:
                        # if "img" in sbooru_sauce:
                        # extract pixiv id
                        # pixivid = re.search('(?<!\d)(\d{8})(?!\d)', sbooru_sauce)
                        # print (pixivid)
                        # reconstruct pixiv url
                        # sbooru_sauce = "[Pixiv](http://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + pixivid.group(1) + ")"
                        # else:
                        # sbooru_sauce = "[Pixiv](" + sbooru_sauce + ")"
                        sbooru_sauce = "[Pixiv](" + sbooru_sauce + ")"
                    if "twitter" in sbooru_sauce:
                        sbooru_sauce = "[Twitter](" + sbooru_sauce + ")"
                    if "nicovideo" in sbooru_sauce:
                        sbooru_sauce = "[NicoNico](" + sbooru_sauce + ")"
                    if "deviantart" in sbooru_sauce:
                        sbooru_sauce = "[DeviantArt](" + sbooru_sauce + ")"
                    # try to detect pixiv direct image links
                    # if "img" in sbooru_sauce:
                    # extract pixiv id
                    # pixivid = re.search('(?<!\d)(\d{8})(?!\d)', sbooru_sauce)
                    # check if there's an actual pixiv id in the source link or not
                    # if pixivid == "":
                    # sbooru_sauce = "[Source](" + sbooru_sauce + ")"
                    # else:
                    # reconstruct pixiv url
                    # sbooru_sauce = "[Pixiv](http://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + pixivid.group(1) + ")"
                    # else:
                    # sbooru_sauce = "[Source](" + sbooru_sauce + ")"
                    # em.set_author(name='Character Image', icon_url=bot.user.avatar_url)
                    em.set_author(name=embed_name)
                    em.set_image(url=booruappend + str(raw_url))
                    em.add_field(name="Image source", value=sbooru_sauce, inline=False)
                    em.add_field(name=idtext, value=sbooru_id, inline=True)
                    em.add_field(name="Dimensions", value=str(width) + "x" + str(height), inline=True)
                    # em.add_field(name="RNG", value=score_rng, inline=True)
                    await asyncio.sleep(0.15)
                    sbooru_img = await ctx.send(embed=em)



    @commands.command()
    async def genquery(self, ctx, char):
        booruurl = 'http://' + booru + '/index.php?page=post&s=list&q=index&tags=' + boorutags_base + badtags_strict + badartists + '+' + char
        await ctx.send(booruurl)

    @commands.command()
    async def genquery2(self, ctx, char):
        booruurl = 'http://' + booru + '/index.php?page=dapi&s=post&q=index&tags=' + boorutags_base + badtags_strict + badartists + '+' + char
        print(booruurl)
        #await ctx.send(booruurl)

    @commands.command()
    @commands.cooldown(rlimit_cmd, rlimit_time, commands.BucketType.user)
    async def arcade(self, ctx):
        em = discord.Embed(title='', description=' ', colour=0xb50404)
        char = 'arcade'
        await self.imagefetch(ctx, char, em)
					
def setup(bot):
    bot.add_cog(ImageCog(bot))
