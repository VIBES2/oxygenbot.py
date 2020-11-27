bot.snipes = {}

@client.event
async def on_message_delete(message):
  bot.snipes[message.channel.id] = message
  if message.author.bot:
   return

@client.command()  
async def snipe(ctx, *, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  try:
    msg = bot.snipes[channel.id]
  except KeyError:
    return await ctx.send('Nothing to snipe!')
  await ctx.send(embed=discord.Embed(description=msg.content, color=0xFFFF).set_author(name=str(msg.author), icon_url=str(msg.author.avatar_url)))
