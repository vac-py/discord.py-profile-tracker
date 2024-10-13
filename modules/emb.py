import discord
def create_embed(t, d, f):
    thing = discord.Embed(title=t, description=d, colour=discord.Colour.pink())
    thing.set_footer(text=f)
    return thing
