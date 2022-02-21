from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def vote(ctx, title, *select):
  if len(select) > 10:
    err = discord.Embed(title = "選択肢が多すぎます。", color = discord.Colour.red())
    await ctx.send(embed = err)
    return

  emoji_list = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣", "8⃣", "9⃣", "🔟"]

  # 縦並びの質問項目を生成
  value = ""
  for num in range(len(select)):
    value += emoji_list[num] + select[num] + "\n"
  # 全ての質問項目を1つのembed項目とする
  embed = discord.Embed(title = value, color = discord.Colour.red())
  
  msg = await ctx.send("**" + title+ "**", embed = embed)
  for i in range(len(select)):
    await msg.add_reaction(emoji_list[i])
  return

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
