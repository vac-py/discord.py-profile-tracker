import discord
from discord.ext import commands
from modules.emb import create_embed
from modules.readj import read_json
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())




@bot.event
async def on_ready():
    print("logged in")

@bot.event
async def on_user_update(b, a):
    if b is not a:
        c = create_embed(f"moonlight name tracker", f"{b.display_name}/{b.name} has updated there profile: {a.display_name}/{a.name}", "format: displayname/name")
        channel_id = read_json("configuration/config.json", "channel-id")
        cx = bot.get_channel(channel_id)
        await cx.send(embed=c)

bot.run(read_json("configuration/config.json", "token"))