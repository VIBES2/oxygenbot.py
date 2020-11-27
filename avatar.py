@client.command()
async def avatar(ctx, mem: discord.Member=None):
 mem = mem or ctx.author
 embed = discord.Embed(title=f"{mem.display_name}'s avatar", color=0xFFFF)
 embed.set_image(url=f'{mem.avatar_url}')
 await ctx.send(embed=embed)
