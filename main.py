import discord
from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
from discord import Activity, ActivityType
import os
import requests
from keep_alive import keep_alive

# تحميل القيم من ملف .env
load_dotenv()

intents = discord.Intents.default()
intents.members = True  # تفعيل الوصول إلى معلومات الأعضاء

bot = commands.Bot(command_prefix='&', intents=intents)

# استبدل USER_ID بمعرف المستخدم الخاص بك
owner_ids = ['656871811186819082']

# معرف السيرفر والقناة
TARGET_GUILD_ID = 1238430819903737947
TARGET_CHANNEL_ID = 1259461386136715325

@bot.command()
async def set_playing(ctx, *, activity: str = None):
    if str(ctx.author.id) not in owner_ids:
        return
    if not activity:
        await ctx.send('**Activity ?**')
        return
    await bot.change_presence(activity=discord.Game(name=activity))
    await ctx.send(f'**Set Activity {activity} ✅**')

@bot.command()
async def listening(ctx, *, activity: str = None):
    if str(ctx.author.id) not in owner_ids:
        return
    if not activity:
        await ctx.send('**Activity ?**')
        return
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity))
    await ctx.send(f'**Set Activity {activity} ✅**')

@bot.command()
async def watching(ctx, *, activity: str = None):
    if str(ctx.author.id) not in owner_ids:
        return
    if not activity:
        await ctx.send('**Activity ?**')
        return
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
    await ctx.send(f'**Set Activity {activity} ✅**')

@bot.command()
async def competing(ctx, *, activity: str = None):
    if str(ctx.author.id) not in owner_ids:
        return
    if not activity:
        await ctx.send('**Activity ?**')
        return
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=activity))
    await ctx.send(f'**Set Activity {activity} ✅**')

@bot.command()
async def streaming(ctx, *, activity: str = None):
    if str(ctx.author.id) not in owner_ids:
        return
    if not activity:
        await ctx.send('**Activity ?**')
        return
    await bot.change_presence(activity=discord.Streaming(name=activity, url=f'https://www.twitch.tv/{activity}'))
    await ctx.send(f'**Set Activity {activity} ✅**')

@bot.command()
async def info(ctx, player_id: str):
    await ctx.message.add_reaction("✅")
    api_url = f'https://www.public.freefireinfo.site/api/info/sg/{player_id}?key=3skr'
    try:
        response = requests.get(api_url)
        data = response.json()
        if not data:
            await ctx.reply("يرجى تقديم ايدي صالح", delete_after=10)
            return

        await ctx.reply(f" ⧉ **Wait L3ARBI search ``12345678`` information 🔍**")
        
        # استخرج الرابطين من البيانات
        avatar_url = data.get('Account Avatar Image', 'N/A')
        banner_url = data.get('Account Banner Image', 'N/A')

        account_embed = discord.Embed(title="📋 **𝐀𝐂𝐂𝐎𝐔ℕ𝐓 ℍ𝐈𝐒𝐓𝐎𝐑𝐘**", color=0x000000)
        account_embed.add_field(name="👤 : **𝗕𝖠𝖲𝖨𝖤 𝗜𝖭𝖥𝖮𝖱𝖬𝖠𝖳𝖨𝖮𝖭𝖲**", value=f"""
        ┌─ **𝐍ame :** {data.get('Account Name', 'N/A')}
        ├─ **𝐔id :** {data.get('Account UID', 'N/A')}
        ├─ **𝐋evel :** {data.get('Account Level', 'N/A')}
        ├─ **𝐑egion :** {data.get('Account Region', 'N/A')}
        ├─ **𝐋ikes :** {data.get('Account Likes', 'N/A')}
        ├─ **𝐇onor 𝐒core :** {data.get('Account Honor Score', 'N/A')}
        ├─ **𝐄vo 𝐀ccess 𝐁adge :** {data.get('Account Evo Access Badge', 'N/A')}
        ├─ **𝐓itle :** {data.get('Equipped Title', 'N/A')}
        └─ **𝐁io :** {data.get('Account Signature', 'N/A')}
        """, inline=False)

        account_embed.add_field(name="🎮 ACCOUNT ACTIVITY", value=f"""
        ┌─ **𝐅ire 𝐏ass :** {data.get('Account Booyah Pass', 'N/A')}
        ├─ **𝐂urrent BP 𝐁adges :** {data.get('Account Booyah Pass Badges', 'N/A')}
        ├─ **BR 𝐑ank :** {data.get('BR Rank Points', 'N/A')}
        ├─ **CS 𝐏oints :** {data.get('CS Rank Points', 'N/A')}
        ├─ **𝐂reated 𝐀t :** {data.get('Account Create Time (GMT 0530)', 'N/A')}
        └─ **𝐋ast 𝐋ogin :** {data.get('Account Last Login (GMT 0530)', 'N/A')}
        """, inline=False)

        account_embed.add_field(name="👕  ACCOUNT OVERVIEW", value=f"""
            ┌─ **𝐀vatar ID  :** {avatar_url}
            └─ **𝐁anner ID :** {banner_url}
            """, inline=False)
        
        # تضمين صورة الافتار
        if avatar_url != 'N/A':
            account_embed.set_thumbnail(url=avatar_url)
        
        # تضمين صورة البانر
        if banner_url != 'N/A':
            account_embed.set_image(url=banner_url)

        # إضافة تفاصيل أخرى إذا لزم الأمر قبل إرسال الإيمبيد
        account_embed.add_field(name="🐾 PET DETAILS", value=f"""
        ┌─ **𝐄quipped :** {data.get('Equipped Pet Information', {}).get('Selected?', 'N/A')}
        ├─ **𝐏et 𝐍ame :** {data.get('Equipped Pet Information', {}).get('Pet Name', 'N/A')}
        ├─ **𝐏et 𝐓ype :** {data.get('Equipped Pet Information', {}).get('Pet Type', 'N/A')}
        ├─ **𝐏et XP :** {data.get('Equipped Pet Information', {}).get('Pet XP', 'N/A')}
        └─ **𝐏et 𝐋evel :** {data.get('Equipped Pet Information', {}).get('Pet Level', 'N/A')}
        """, inline=False)

        account_embed.add_field(name="🛡 CLAN INFO", value=f"""
        ┌ **𝐂lan 𝐍ame :** {data.get('Guild Information', {}).get('Guild Name', 'N/A')}
        ├─ **𝐂lan ID :** {data.get('Guild Information', {}).get('Guild ID', 'N/A')}
        ├─ **𝐂lan 𝐋evel :** {data.get('Guild Information', {}).get('Guild Level', 'N/A')}
        └─ **𝐌embers :** {data.get('Guild Information', {}).get('Guild Current Members', 'N/A')}
        """, inline=False)

        account_embed.add_field(name="⚔️ LEADER INFO :", value=f"""
        ┌─ **𝐍ame :** {data.get('Guild Leader Information', {}).get('Leader Name', 'N/A')}
        ├─ **𝐔id :** {data.get('Guild Leader Information', {}).get('Leader UID', 'N/A')}
        ├─ **𝐋evel :** {data.get('Guild Leader Information', {}).get('Leader Level', 'N/A')}
        ├─ **𝐂reated 𝐀t :** {data.get('Guild Leader Information', {}).get('Leader Ac Created Time (GMT 0530)', 'N/A')}
        ├─ **𝐋ast 𝐋ogin :** {data.get('Guild Leader Information', {}).get('Leader Last Login Time (GMT 0530)', 'N/A')}
        ├─ **𝐓itle :** {data.get('Guild Leader Information', {}).get('Leader Title', 'N/A')}
        ├─ **𝐄vo 𝐀ccess 𝐁adge :** {data.get('Guild Leader Information', {}).get('Leader BP Badges', 'N/A')}
        ├─ **BR 𝐑ank :** {data.get('Guild Leader Information', {}).get('Leader BR Points', 'N/A')}
        └─ **CS 𝐏oints :** {data.get('Guild Leader Information', {}).get('Leader CS Points', 'N/A')}
        """, inline=False)
        
        account_embed.set_footer(text=f"Developed By: @2b_a |")

        await ctx.send(embed=account_embed)

    except Exception as e:
        await ctx.reply(f"ERROR !: {str(e)}")

@bot.command()
async def visits(ctx, region: str, uid: str):
    await ctx.message.add_reaction("✅")

    async def send_multiple_requests(region, uid, view_count):
        success_count = 0
        for _ in range(view_count):
            url = f"https://www.public.freefireinfo.site/api/info/{region}/{uid}?key=3skr"
            response = requests.get(url)
            if response.status_code == 200:
                success_count += 1
                print(f"Sent visit for ID {uid} successfully {success_count} times")
            else:
                print("Error in sending visit")
            await asyncio.sleep(1)

    if ctx.channel.id == TARGET_CHANNEL_ID:
        # إرسال إمبيد الانتظار
        embed_wait = Embed(
            title="🔍 **Searching for ID**",
            description=f" ⧉ **Wait for the bot to search for ``{uid}``**",
            color=0x000000
        )
        await ctx.reply(embed=embed_wait)

        # إرسال إمبيد زيادة الزوار
        embed_visits = Embed(
            title="**INCREASE VISITORS**",
            description=f"""
        > **Waiting for 50 visits for this ID :``{uid}``** <a:CD_ChadwickSad:1246244023174172763>                         
        > **| BOT DEVELOPED BY :**<@656871811186819082> <a:king:1249755074931195914> **|**
        """,
            color=0x000000
        )
        await ctx.reply(embed=embed_visits)

        # إرسال الزوار للحساب
        await send_multiple_requests(region, uid, 50)

        # حذف الرسائل السابقة التي أرسلها البوت
        async for message in ctx.channel.history(limit=50):
            if message.author == bot.user:
                await message.delete()

        # إرسال إمبيد عند الانتهاء من إرسال الزوار
        embed_done = Embed(
            title="✅ **Visits Sent**",
            description=f"**Successfully sent 50 visits to ID: ``{uid}``**",
            color=0x00FF00
        )
        await ctx.reply(embed=embed_done)
    else:
        await ctx.reply("This command is not available in this channel.")

@bot.command()
async def ban(ctx, player_id: str):
    await ctx.message.add_reaction("✅")
    await ctx.reply(f"⧉ **Wait L3ARBI search ``{player_id}`` 🔍**")

    url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={player_id}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'authority': "ff.garena.com",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'referer': "https://ff.garena.com/en/support/",
        'sec-ch-ua': "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'x-requested-with': "B6FksShzIgjfrYImLpTsadjS86sddhFH",
        'Cookie': "_ga_8RFDT0P8N9=GS1.1.1706295767.2.0.1706295767.0.0.0; apple_state_key=8236785ac31b11ee960a621594e13693; datadome=bbC6XTzUAS0pXgvEs7uZOGJRMPj4wRJzOh2zJmrQaYViaPVLZOIi__jw~cnNaIU1FzrByJ_qVJa7MwmpH3Z2jjRxtDkzsy2hiDTQ4cPY_n0mAwB3seemjGYszNpsfteh; token_session=f40bfc2e69a573f3bdb597e03c81c41f9ecf255f69d086aac38061fc350315ba5d64968819fe750f19910a1313b8c19b; _ga_Y1QNJ6ZLV6=GS1.1.1707023329.1.1.1707023568.0.0.0; _ga_KE3SY7MRSD=GS1.1.1707023591.1.1.1707023591.0.0.0; _gid=GA1.2.1798904638.1707023592; _gat_gtag_UA_207309476_25=1; _ga_RF9R6YT614=GS1.1.1707023592; _ga=GA1.1.925801730.1706287088"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        is_banned = result.get('data', {}).get('is_banned', 0)
        period = result.get('data', {}).get('period', 0)
        player_name = result.get('data', {}).get('player_name')  # Assuming player_name is returned from API

        if is_banned == 1:
            embed = Embed(
                title="**Account Status**",
                description=(
                    f"**ACCOUNT ID :** {player_id}\n"
                    f"**ACCOUNT STATUS :** BANNED <a:JBF_actingSusNotMeOwO:1246243555496689675>\n"
                    f"**PERIOD 🕒 :** {period} DAY(S)\n"
                    f"**| BOT DEVELOPED BY :** <@656871811186819082> <a:king:1249755074931195914>"
                ),
                color=0xFF0000  # Red for banned status
            )
        else:
            embed = Embed(
                title="**Account Status**",
                description=(
                    f"**ACCOUNT ID :** {player_id}\n"
                    f"**ACCOUNT STATUS :** NOT BANNED <a:animVerify:1247239214228308010>\n"
                    f"**| BOT DEVELOPED BY :** <@656871811186819082> <a:king:1249755074931195914>"
                ),
                color=0x00FF00  # Green for not banned status
            )

        await ctx.reply(embed=embed)

    except requests.RequestException as e:
        await ctx.author.send("Failed to fetch data from the API. Please try again later.")

    except Exception as e:
        await ctx.author.send(f"Error: {e}")

@bot.command()
async def commands(ctx):
    # Create an Embed for help
    embed = discord.Embed(
        title="__VAMPIRES INFO__ :",
        description=("**is the perfect bot! Through it, you can view Free Fire ACCOUNT INFO, increase VISITORS to the account, and check if the account is BANNED.**"),
        colour=discord.Colour.dark_gray()  # Use dark gray color for the sidebar
    )
    embed.add_field(name="COMMANDS :", value=" ", inline=False)
    embed.add_field(name="<a:arrow1:1249755312609562705> `&info <player_id>`", value="Show account information by ID.", inline=False)
    embed.add_field(name="<a:arrow1:1249755312609562705> `&ban <player_id>`", value="Check if the account is Banned.", inline=False)
    embed.add_field(name="<a:arrow1:1249755312609562705> `&visits <region> <uid>`", value="Send 50 visitors to the account by ID.", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1245882841435471882/1268874843726807060/20240802_110319.jpg?ex=66ae0349&is=66acb1c9&hm=a419a8856733bef1adc6989cb1f67b2f2abb29cb68e1505d8743610fba95e26c&")  # Replace with your desired image URL
    embed.set_author(name="@2b_a", icon_url="https://cdn.discordapp.com/attachments/1268685758961684692/1268875809435684905/IMG_20240703_020546_393.jpg?ex=66ae042f&is=66acb2af&hm=bc7a089bfa66ac51e87106e3b24d1514b155df90970a5b005e43d3487a24a0ad&")
    
    await ctx.reply(embed=embed)

keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))