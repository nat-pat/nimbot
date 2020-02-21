import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name = "average")
async def average (ctx, a , b):
    await ctx.send [(a +b)/2]

@bot.command(name= 'shower_thoughts')
async def shower_thoughts():
    await ctx.send(random.choice(["Your belly button is just your old mouth.",
                          "Whenever you buy and eat half a chicken,you are secretly sharing a meal with a stranger.",
                          "In sign language, arthiritis is a speech impediment.",
                          "If two people on opposite sides of the world each drop a piece of bread, the Earth briefly becomes a sandwich.",
                          "Maybe superheroes wear capes to hide the zipper on the back of their onesie",
                          "At some point, we have all kicked a pregnant woman.",
                          "Alarm clocks are the most hated objects. If they don't do their job correctly, they are hated. But if they do their job correctly, they are hated.",
                          "Someone has your dream job and hates going to work everyday.",
                          "Making a typo in an online argument is the equivalent of voice cracking in a verbal argument.",
                          "A different version of you exists in the minds of everyone who knows you.",
                          "Theme parks get a crystal clear picture of you on a roller coaster at 70 mph, but bank cameras can't get a clear shot of a robber standing still.",
                          "If you had $1 for every year the universe has existed, you wouldn't even make top 50 on the Forbes list.",
                          "Lawyers hope you get sued, cops hope you're a criminal, mechanics hope you have car trouble, but only a thief wishes prosperity for you.",
                          "Remember that every corpse on Everest was once a highly motivated person.",
                          "The engineer who invented automatic doors is eternally the greatest gentleman.",
                          "When you say 'Forward' or 'Back', your lips move in those directions",
                          "If humans could fly, we'd consider it exercise and never do it.",
                          "Clapping is just hitting yourself because you like something.",
                          "In order to fall asleep, you have to pretend to be asleep.",
                          "Maybe plants are really farming us, giving us oxygen until we eventually expire and turn into mulch which they can consume",
                          "Aliens invaded the Moon on July 20th, 1969."]))
bot.run(token)



